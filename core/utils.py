def format_youtube_links(videos):
    if not videos:
        return "No relevant videos found."
    return "\n\n".join([
        f"{i+1}. **{v['title']}**   Link: {v['url']}"
        for i, v in enumerate(videos)
    ])
