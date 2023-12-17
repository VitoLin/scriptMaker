from dotenv import load_dotenv
from youtubeApis import get_playlist_videos, get_video_title
from getVideoTranscript import get_video_transcript
import os
import re

# Set up your API key and playlist ID
load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY') # It's good practice to keep your API key in an environment variable

playlist_id = 'PLWDQtIyZRZu3aoUQkZ2UlkwdDM9o0If2t'

# Get all video IDs from the playlist
video_ids = get_playlist_videos(YOUTUBE_API_KEY, playlist_id)

# Get the transcript for each video and save it to a json file
rootdir = 'transcripts'

for video_id in video_ids:
    video_title = get_video_title(YOUTUBE_API_KEY, video_id)
    # Make string filename safe
    safe_title = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-", video_title)
    filename = safe_title + '.json'
    get_video_transcript(video_id, rootdir, filename)
