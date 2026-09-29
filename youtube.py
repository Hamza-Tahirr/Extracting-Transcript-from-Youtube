from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi().fetch('jLNrvmXboj8')

text_formatted = TextFormatter().format_transcript(transcript)

with open('transcript.text', 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)
