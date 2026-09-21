#!/usr/bin/env python3
"""Summarize binary judge predictions from local JSONL; never call a model or decide a gate."""
import argparse
import json
from pathlib import Path
import sys


def ratio(numerator, denominator):
    return numerator / denominator if denominator else None


def summarize(rows, positive, negative):
    if not isinstance(positive, str) or not isinstance(negative, str) or not positive or not negative or positive == negative:
        raise ValueError('positive and negative must be distinct nonempty string labels')
    counts = dict(tp=0, fp=0, fn=0, tn=0)
    invalid = []
    seen = set()
    total = 0
    labels = (positive, negative)
    for total, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f'row {total}: expected an object')
        case_id = row.get('case_id')
        if not isinstance(case_id, str) or not case_id.strip():
            raise ValueError(f'row {total}: case_id must be a nonempty string')
        if case_id in seen:
            raise ValueError(f'row {total}: duplicate case_id')
        seen.add(case_id)
        expected, actual = row.get('expected'), row.get('actual')
        if not isinstance(expected, str) or expected not in labels:
            invalid.append({'case_id': case_id, 'reason': 'invalid_expected_label'})
            continue
        if not isinstance(actual, str) or actual not in labels:
            invalid.append({'case_id': case_id, 'reason': 'invalid_actual_label'})
            continue
        cell = ('tp' if actual == positive else 'fn') if expected == positive else ('fp' if actual == positive else 'tn')
        counts[cell] += 1
    tp, fp, fn, tn = (counts[k] for k in ('tp', 'fp', 'fn', 'tn'))
    valid = tp + fp + fn + tn
    return {
        'schema_version': 1,
        'positive_label': positive,
        'negative_label': negative,
        'total_rows': total,
        'valid_rows': valid,
        'invalid_rows': len(invalid),
        'coverage': ratio(valid, total),
        'confusion_matrix': counts,
        'metrics': {
            'accuracy': ratio(tp + tn, valid),
            'precision': ratio(tp, tp + fp),
            'recall': ratio(tp, tp + fn),
            'specificity': ratio(tn, tn + fp),
            'f1': ratio(2 * tp, 2 * tp + fp + fn),
        },
        'invalid_cases': invalid,
        'notes': [
            'Labels are matched exactly; no implicit normalization is applied.',
            'Metrics exclude invalid rows; coverage and invalid counts are reported separately.',
            'Null ratios have no defined denominator. No uncertainty or release decision is computed.',
        ],
    }


def read_rows(stream):
    for line_number, line in enumerate(stream, 1):
        if line.strip():
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f'line {line_number}: invalid JSON') from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Local JSONL file, or - for stdin; each row needs case_id, expected, actual')
    parser.add_argument('--positive', required=True, help='Exact label meaning the positive class')
    parser.add_argument('--negative', required=True, help='Exact label meaning the negative class')
    args = parser.parse_args()
    try:
        if args.input == '-':
            report = summarize(read_rows(sys.stdin), args.positive, args.negative)
        else:
            with Path(args.input).open(encoding='utf-8') as stream:
                report = summarize(read_rows(stream), args.positive, args.negative)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
