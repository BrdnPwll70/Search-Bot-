from duckduckgo_search import DDGS


class AIBot:

    def search_web(self, query):
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=5
            )

            for result in search_results:
                results.append(
                    {
                        "title": result.get("title", "No title"),
                        "url": result.get("href", result.get("hrehf", ""))
                    }
                )

        return results

    def format_search_results(self, results):
        if not results:
            return "No search results found."

        lines = []
        for index, result in enumerate(results, start=1):
            title = result["title"].strip() if result["title"] else "No title"
            url = result["url"].strip() if result["url"] else ""
            if url:
                lines.append(f"{index}. {title}\n{url}")
            else:
                lines.append(f"{index}. {title}")

        return "\n\n".join(lines)

    def chat(self, message):
        if message.startswith("search "):
            query = message.replace("search ", "", 1).strip()
            if not query:
                return "Please provide a search query after the word 'search'."

            results = self.search_web(query)
            return self.format_search_results(results)

        return f"You said: {message}"


bot = AIBot()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = bot.chat(user_input)
    print("\nBot:")
    print(response)
    print()