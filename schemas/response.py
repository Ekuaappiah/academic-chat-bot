from pydantic import BaseModel
from typing import List, Dict


class YouTubeVideo(BaseModel):
    title: str
    url: str


class ChatbotResponse(BaseModel):
    question: str
    topic: str
    answer: str
    youtube_videos: List[YouTubeVideo]
    search_query_used: str
    conversation_history: List[Dict[str, str]]
