# Extracting reference motion

The helper uses Python 3.11+ (`hashlib.file_digest`), ffprobe, and a recent ffmpeg supporting `-fps_mode`. It never contacts a network service or copies the original recording. A font is optional; labeled images require ffmpeg's drawtext filter.

```bash
python3 scripts/extract_motion_frames.py reference.webm /tmp/motion-evidence \
  --start 2.5 --duration 0.8 --sample-ms 50 \
  --crop 68:50:0:466 --scale 3 --columns 8 \
  --font /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
```

Run from this skill directory or use an absolute script path. Replace the input, interval, crop, and font with values for the actual recording. Crop is **width:height:x:y** in source pixels. The output must be new or empty; use another directory for another run.

The script reads decoded source timestamps, selects the first frame at or after each sample time, deduplicates selections, then labels the selected images with their original presentation timestamps when a font is supplied. It does not manufacture evenly spaced video frames. The manifest records original frame indices and times, dimensions, source duration, capture hash, and extraction settings.

The `contact-sheet.png` is read left to right, top to bottom. Trailing empty cells are padding. `frame-*.png` can be examined individually. Sampling may skip a brief overshoot, especially in a low-rate or variable-rate capture; inspect a tighter interval or smaller sample spacing when needed. No extraction can recover uncaptured frames.

The crop does not track a moving sidebar automatically. Confirm the bounding region remains correct across the interval. Review output before sharing: a crop can still contain tooltips, names, or other identifying text. Reusable research should not require a private local video path.

Do not derive trigger latency without a visible cursor/event reference. Do not divide frame count by a nominal container frame rate for a variable-rate screen capture. Source presentation times identify when frames appear in the video; they do not identify browser paint or input event times.

Errors leave any successfully generated diagnostic files in the output directory. Inspect or choose another output directory for a retry. The helper does not delete existing files or automatically publish evidence.
