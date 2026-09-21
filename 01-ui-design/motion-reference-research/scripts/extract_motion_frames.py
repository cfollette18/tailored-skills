#!/usr/bin/env python3
"""Create timestamped, optionally cropped motion evidence using source frame PTS."""

import argparse
import bisect
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys


def positive(value):
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise argparse.ArgumentTypeError("must be a finite positive number")
    return result


def crop_box(value):
    try:
        width, height, x, y = (int(part) for part in value.split(":"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("crop must be width:height:x:y") from exc
    if min(width, height) <= 0 or min(x, y) < 0:
        raise argparse.ArgumentTypeError("invalid crop dimensions or origin")
    return width, height, x, y


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path, help="new or empty output directory")
    parser.add_argument("--start", type=float, default=0)
    parser.add_argument("--duration", type=positive, required=True)
    parser.add_argument("--sample-ms", type=positive, default=50)
    parser.add_argument("--crop", type=crop_box)
    parser.add_argument("--scale", type=int, choices=range(1, 5), default=2)
    parser.add_argument("--columns", type=int, choices=range(1, 17), default=8)
    parser.add_argument("--font", type=Path, help="optional font for frame timestamps")
    args = parser.parse_args()
    if not math.isfinite(args.start) or args.start < 0:
        parser.error("start must be finite and nonnegative")
    if not args.input.is_file():
        parser.error("input does not exist")
    if args.output.exists() and any(args.output.iterdir()):
        parser.error("output must be empty; existing evidence is never overwritten")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        parser.error("ffmpeg and ffprobe must be installed")
    if args.font and (not args.font.is_file() or any(c in str(args.font) for c in "':,;[]\\")):
        parser.error("font must exist and have a filter-safe path")
    steps = math.ceil(args.duration * 1000 / args.sample_ms)
    if steps > 200:
        parser.error("limit each extraction to 200 requested samples; narrow the interval")
    probe = subprocess.run([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
        "-show_entries", "frame=best_effort_timestamp_time:stream=width,height:format=duration",
        "-of", "json", str(args.input.resolve()),
    ], check=True, capture_output=True, text=True)
    info = json.loads(probe.stdout)
    frames = info.get("frames", [])
    if not frames or any("best_effort_timestamp_time" not in frame for frame in frames):
        parser.error("all decoded video frames must have presentation timestamps")
    times = [float(frame["best_effort_timestamp_time"]) for frame in frames]
    if times != sorted(times):
        parser.error("nonmonotonic timestamps require manual analysis")
    stream = info["streams"][0]
    if args.crop:
        width, height, x, y = args.crop
        if x + width > stream["width"] or y + height > stream["height"]:
            parser.error("crop exceeds the source dimensions")
    chosen = []
    end = args.start + args.duration
    for step in range(steps):
        index = bisect.bisect_left(times, args.start + step * args.sample_ms / 1000)
        if index < len(times) and times[index] < end and (not chosen or chosen[-1] != index):
            chosen.append(index)
    if not chosen:
        parser.error("no video frames in the requested interval")
    args.output.mkdir(parents=True, exist_ok=True)
    selection = "+".join(f"eq(n,{index})" for index in chosen)
    filters = [f"select='{selection}'"]
    if args.crop:
        filters.append("crop=" + ":".join(map(str, args.crop)))
    filters.append(f"scale=iw*{args.scale}:ih*{args.scale}:flags=neighbor")
    if args.font:
        filters += ["pad=iw:ih+26:0:0:white", f"drawtext=fontfile='{args.font.resolve()}':text='%{{pts\\:flt}} s':x=5:y=h-23:fontsize=16:fontcolor=black"]
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-copyts", "-i", str(args.input.resolve()),
        "-map", "0:v:0", "-an",
        "-vf", ",".join(filters), "-fps_mode", "vfr", "-start_number", "0",
        str(args.output.resolve() / "frame-%04d.png"),
    ], check=True)
    extracted = sorted(args.output.glob("frame-*.png"))
    if len(extracted) != len(chosen):
        raise RuntimeError("decoded output count differs from selected timestamps")
    rows = math.ceil(len(chosen) / args.columns)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-framerate", "1",
        "-start_number", "0", "-i", str(args.output.resolve() / "frame-%04d.png"),
        "-vf", f"tile={args.columns}x{rows}:padding=2:margin=2:color=white",
        "-frames:v", "1", str(args.output.resolve() / "contact-sheet.png"),
    ], check=True)
    with args.input.open("rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    manifest = {
        "source_sha256": digest,
        "source_dimensions": [stream["width"], stream["height"]],
        "source_duration_seconds": float(info["format"]["duration"]),
        "source_frame_count": len(frames),
        "interval_seconds": [args.start, end], "sample_interval_ms": args.sample_ms,
        "crop_width_height_x_y": args.crop, "scale": args.scale,
        "sampling": "first source frame at or after each requested time; duplicates removed",
        "frames": [{"file": path.name, "source_frame_index": index, "source_pts_seconds": times[index]}
                   for path, index in zip(extracted, chosen)],
        "privacy": "Only extracted pixels and a source hash are recorded. Review crops before sharing.",
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Extracted {len(extracted)} source frames and a contact sheet to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except (subprocess.CalledProcessError, OSError, RuntimeError) as error:
        print(f"Extraction failed: {error}", file=sys.stderr)
        sys.exit(1)
