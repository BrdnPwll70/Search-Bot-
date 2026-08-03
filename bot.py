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
                        "title": result["title"],
                        "url": result["hrehf"]
                    }
                )

    return results

def chat(self, message):

    if message.startswith("search "):
        query = message.replace("search ", "")

        return self.search_web(query)
    
    return f"You said: {message}"


bot = AIbot()

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = bot.chat(user_input)

    print("\nBot:")
    print(response)
    print()