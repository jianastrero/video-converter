## 🎥 🔀 🎥️ Image Converter script in Python
Convert videos to other formats using Python

## 📝 Description:
This script converts videos to other formats using Python. It uses the FFmpeg library to convert videos.

## How to use:
```bash
python video_converter.py --input_dir <input_dir> \
                          --output_dir <output_dir> \
                          --format <output_format> \
                          --quality <output_quality> \
                          --codec <output_codec> \
                          --recursive <True/False> \
                          --overwrite <True/False>
```

## Parameters
| Parameter      | Default  | Description                                                          |
|:---------------|:---------|:---------------------------------------------------------------------|
| `--input_dir`  | `input`  | Input directory where the videos are located                         |
| `--output_dir` | `output` | Output directory where the converted videos will be saved            |
| `--format`     | `mp4`    | Output format of the converted videos                                |
| `--quality`    | `100`    | Output quality of the converted videos                               |
| `--codec`      | `mpeg4`  | Output codec of the converted videos                                 |
| `--recursive`  | `False`  | Recursively convert videos in subdirectories                         |
| `--overwrite`  | `False`  | Overwrite existing files in the output directory                     |

## 📝 Notes:
- The script will create the output directory if it doesn't exist.
- The script will not overwrite existing files in the output directory by default.
- The script will not convert videos in subdirectories by default.