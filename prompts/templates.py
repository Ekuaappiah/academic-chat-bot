from langchain.prompts import ChatPromptTemplate

topic_prompt = ChatPromptTemplate.from_template("""
You are a tutor assistant. Classify the topic of the question below into one word only: Math, Science, History, Tech, Literature, or Other.
Question: {question}
Topic:
""")

qa_prompt = ChatPromptTemplate.from_template("""
You are a helpful tutor. Use the chat history to answer the current educational question clearly and accurately.

{chat_history}

Current Question: {question}
Answer:
""")


yt_query_prompt = ChatPromptTemplate.from_template("""
Create a YouTube search query for this educational topic or question:
{question}
Search Query:
""")

merge_prompt = ChatPromptTemplate.from_template("""
Given the answer below and a list of YouTube links, write a well-structured educational response. 
- Begin with the answer as a concise explanation.
- Then, introduce the YouTube videos as recommended learning resources.
- Format the links with titles and bullet points, if possible.

Answer:
{answer}

YouTube Links:
{youtube_links}

Output:
""")

