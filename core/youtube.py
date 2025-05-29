from googleapiclient.discovery import build


class YouTubeSearcher:
    def __init__(self, api_key: str):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search_videos(self, query: str, max_results: int = 5):
        request = self.youtube.search().list(
            part="snippet",
            q=query + " educational tutorial",
            type="video",
            maxResults=max_results,
            order="relevance",
            videoDuration="medium",
            videoDefinition="high"
        )
        response = request.execute()

        return [
            {
                'title': item['snippet']['title'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            for item in response.get('items', [])
        ]
