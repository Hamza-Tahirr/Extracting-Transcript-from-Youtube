# Extracting Transcript from YouTube

A small Python command-line script that downloads the English transcript of a YouTube video and saves it as a plain text file. It uses the captions YouTube already has for the video, so no API key is needed.

## Features

- Accepts a full YouTube link (`watch?v=`, `youtu.be`, `shorts`, `embed`, `live`) or just the 11-character video ID
- Fetches the English captions, using manually added ones when they exist and YouTube's automatic captions otherwise
- Writes the transcript as plain text, one caption line per line
- Lets you choose the output file with `-o` (default: `transcript.txt`)
- Prints a readable error when a video has no transcript, is unavailable, or the request is blocked

## Tech stack

- Python 3.8+
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)

## Project structure

```
.
├── youtube.py          # command-line script
├── requirements.txt    # Python dependency
├── transcript.txt      # sample output for video jLNrvmXboj8
└── LICENSE
```

## Setup

```bash
git clone https://github.com/Hamza-Tahirr/Extracting-Transcript-from-Youtube.git
cd Extracting-Transcript-from-Youtube

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

Pass a video link or ID. Put links in quotes so the shell does not treat `?` or `&` as special characters:

```bash
python youtube.py "https://www.youtube.com/watch?v=jLNrvmXboj8"
python youtube.py jLNrvmXboj8
```

Save to a different file:

```bash
python youtube.py "https://youtu.be/jLNrvmXboj8" -o my_transcript.txt
```

The script prints the path of the saved file when it finishes. `transcript.txt` in this repo is a sample transcript saved from video `jLNrvmXboj8`.

## Limitations

- Only English transcripts are requested. Videos without English captions, or with captions turned off, will fail with an error message.
- YouTube often blocks requests coming from cloud servers, so the script works best when run from a normal home or office connection.

## License

MIT, see [LICENSE](LICENSE).
