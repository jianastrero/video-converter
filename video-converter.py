import argparse
import glob
import os

import ffmpeg


# Function to parse command line arguments
def parse_arguments():
    """
    This function parses command line arguments using argparse module.
    It sets up the following arguments:
    --input_dir: Input directory (default is 'input')
    --output_dir: Output directory (default is 'output')
    --format: Output format (default is 'mp4')
    --quality: Output quality (default is 100)
    --codec: Video Codec (default is 'mpeg4')
    --recursive: Recursive mode (default is False)
    --overwrite: Overwrite mode (default is False)
    """
    parser = argparse.ArgumentParser(description='This script converts images to other formats using Python. It uses '
                                                 'the ffmpeg library to convert images.')

    parser.add_argument('--input_dir', type=str, default='input', help='Input directory')
    parser.add_argument('--output_dir', type=str, default='output', help='Output directory')
    parser.add_argument('--format', type=str, default='mp4', help='Output format')
    parser.add_argument('--quality', type=int, default=100, help='Output quality')
    parser.add_argument('--codec', type=str, default='mpeg4', help='Video Codec')
    parser.add_argument('--recursive', type=bool, default=False, help='Recursive mode')
    parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite mode')

    return parser.parse_args()


# Function to check if the format is supported
def is_format_supported(format: str):
    """
    This function checks if the provided format is supported.
    It currently supports 'mp4', 'avi', 'mkv', 'mov'.
    """
    return format.lower() in ['mp4', 'avi', 'mkv', 'mov']


# Function to convert video
def convert_video(input_path, output_path, format, quality, codec, overwrite):
    """
    This function converts a video from one format to another using ffmpeg.
    It takes the following parameters:
    input_path: Path to the input video
    output_path: Path to the output video
    format: Output format
    quality: Output quality
    codec: Video codec
    overwrite: If True, it will overwrite the output file if it already exists
    """
    if not is_format_supported(format):
        print(f"Format {format} is not supported.")
        return

    try:
        stream = ffmpeg.input(input_path)

        stream = ffmpeg.output(stream, output_path, format=format, vcodec=codec, crf=quality)

        if overwrite:
            stream = ffmpeg.overwrite_output(stream)

        ffmpeg.run(stream)
        return True
    except ffmpeg.Error as e:
        print(f"ffmpeg error: {e}")
        return False


# Main function
def main():
    """
    This is the main function that gets executed when the script is run.
    It parses the command line arguments, checks if the input directory exists and if the output format is supported.
    It then converts all the videos in the input directory to the specified format and saves them in the output directory.
    """
    args = parse_arguments()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    format = args.format.lower()
    quality = max(0, min(args.quality, 100))
    codec = args.codec.lower()
    recursive = bool(args.recursive)
    overwrite = bool(args.overwrite)

    if not os.path.exists(input_dir):
        print('Input directory does not exist')
        return

    if not is_format_supported(format):
        print(f'Output format "{format}" is not supported')
        return

    if not os.path.exists(output_dir):
        os.makedirs(args.output_dir)

    if recursive:
        input_paths = glob.glob(os.path.join(input_dir, '**', '*.*'), recursive=True)
    else:
        input_paths = glob.glob(os.path.join(input_dir, '*.*'))

    for input_path in input_paths:
        input_path = os.path.abspath(input_path)
        output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
        output_path = os.path.splitext(output_path)[0] + '.' + format
        output_dir = os.path.dirname(output_path)

        if os.path.exists(output_path) and not overwrite:
            print(f'Skipped: {output_path}, already exists')
            continue

        if convert_video(input_path, output_path, format, quality, codec, overwrite):
            print(f'Converted: {output_path} (quality: {quality}) (format: {format})')


# Entry point of the script
if __name__ == "__main__":
    main()
