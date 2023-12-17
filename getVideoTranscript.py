# https://pypi.org/project/youtube-transcript-api/
from youtube_transcript_api import YouTubeTranscriptApi
import os
import json

def get_video_transcript(video_id, rootdir, filename):
    # Find valid transcript in english, prioritizing manually created subtitles
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id=video_id)

    transcript = transcript_list.find_manually_created_transcript(['en-US', 'en'])
    if transcript == None:
        transcript = transcript_list.find_generated_transcript(['en-US', 'en'])

    transcript_text = transcript.fetch()

    # Write full transcript to json file
    full_path = os.path.join(rootdir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(transcript_text, f, ensure_ascii=False, indent=4)
