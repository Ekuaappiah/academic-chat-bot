from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.templates import topic_prompt, qa_prompt, yt_query_prompt, merge_prompt
from schemas.response import ChatbotResponse, YouTubeVideo
from core.memory import ChatMemory
from core.youtube import YouTubeSearcher
from core.utils import format_youtube_links


class EducationalChatbot:
    def __init__(self, google_api_key: str, youtube_api_key: str):
        self.llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)
        self.memory = ChatMemory()
        self.youtube = YouTubeSearcher(youtube_api_key)

    def invoke_prompt(self, prompt_template, **kwargs):
        messages = prompt_template.format_messages(**kwargs)
        response = self.llm.invoke(messages)
        return response.content.strip()

    def merge_response(self, answer: str, youtube_links: list[dict]) -> str:
        if not youtube_links:
            return answer

        formatted_links = format_youtube_links(youtube_links)
        return f"{answer}\n\n**Recommended YouTube Videos:**\n{formatted_links}"

    def chat(self, question: str) -> ChatbotResponse:
        conversation_history = "\n".join(
            [f"{m['role'].capitalize()}: {m['content']}" for m in self.memory.get_history()]
        )

        topic = self.invoke_prompt(topic_prompt, question=question)
        answer = self.invoke_prompt(qa_prompt, question=question, chat_history=conversation_history)
        yt_query = self.invoke_prompt(yt_query_prompt, question=question)
        yt_videos = self.youtube.search_videos(yt_query)
        final_answer = self.merge_response(answer=answer, youtube_links=yt_videos)

        self.memory.add(question, final_answer)

        return ChatbotResponse(
            question=question,
            topic=topic if topic in ["Math", "Science", "History", "Tech", "Literature"] else "Other",
            answer=final_answer,
            youtube_videos=[YouTubeVideo(**v) for v in yt_videos],
            search_query_used=yt_query,
            conversation_history=self.memory.get_history()
        )
