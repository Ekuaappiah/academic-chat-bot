from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

class ChatMemory:
    def __init__(self):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    def add(self, user_message: str, assistant_message: str):
        self.memory.chat_memory.add_user_message(user_message)
        self.memory.chat_memory.add_ai_message(assistant_message)

    def get_history(self):
        messages = self.memory.chat_memory.messages
        return [
            {'role': 'user' if isinstance(m, HumanMessage) else 'assistant', 'content': m.content}
            for m in messages
        ]

    def clear(self):
        self.memory.clear()
