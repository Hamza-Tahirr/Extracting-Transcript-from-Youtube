

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript('jLNrvmXboj8')

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
text_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open('transcript.text', 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)
