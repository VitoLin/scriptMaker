from googleapiclient.discovery import build

def get_playlist_videos(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_ids = []
    next_page_token = None

    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,  # API allows max of 50 items per request
            pageToken=next_page_token
        )

        pl_response = pl_request.execute()

        video_ids += [item['contentDetails']['videoId'] for item in pl_response['items']]

        next_page_token = pl_response.get('nextPageToken')

        if not next_page_token:
            break

    return video_ids

def get_video_title(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Make a request to the YouTube API to get video details
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )

    response = request.execute()

    # Extract the video title from the response
    if 'items' in response:
        video = response['items'][0]
        title = video['snippet']['title']
        return title
    else:
        return None
