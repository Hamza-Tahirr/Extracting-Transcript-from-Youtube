import argparse
import re
import sys

from youtube_transcript_api import CouldNotRetrieveTranscript, YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Matches watch?v=, youtu.be/, /shorts/, /embed/ and /live/ links
VIDEO_ID_PATTERN = re.compile(r"(?:v=|youtu\.be/|/shorts/|/embed/|/live/)([\w-]{11})")


def get_video_id(value):
    match = VIDEO_ID_PATTERN.search(value)
    return match.group(1) if match else value


def main():
    parser = argparse.ArgumentParser(description="Save the transcript of a YouTube video as plain text.")
    parser.add_argument("video", help="YouTube video URL or ID")
    parser.add_argument("-o", "--output", default="transcript.txt", help="output file (default: transcript.txt)")
    args = parser.parse_args()

    video_id = get_video_id(args.video)

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
    except CouldNotRetrieveTranscript as error:
        sys.exit(str(error))

    text = TextFormatter().format_transcript(transcript)

    with open(args.output, "w", encoding="utf-8") as text_file:
        text_file.write(text)

    print(f"Saved transcript of {video_id} to {args.output}")


if __name__ == "__main__":
    main()
