Simple AI Search Bot

A lightweight Python chatbot that combines basic conversational functionality with web search capabilities using the DuckDuckGo Search API. Users can interact with the bot through a command-line interface and perform internet searches by prefixing their message with the search command.

Features
Interactive command-line chatbot
Web searching powered by DuckDuckGo
Retrieves and displays the top 5 search results
Clean formatting of search results with titles and URLs
Echo-response mode for non-search messages
Simple and beginner-friendly code structure
How It Works

The application creates an AIBot class that handles three primary functions:

Searching the Web

Uses the duckduckgo_search library to query DuckDuckGo.
Retrieves up to five search results.
Extracts the title and URL for each result.

Formatting Results

Converts search results into a readable numbered list.
Displays titles alongside their corresponding URLs.

Chat Interface

Messages beginning with search trigger a web search.
All other messages receive a simple echo response.
The program runs continuously until the user enters exit.
Example Usage
Plain Text
You: search python tutorials
 
Bot:
1. Python Tutorial - Official Documentation
https://docs.python.org
 
2. Learn Python
https://www.learnpython.org
Show more lines
Plain Text
You: Hello
 
Bot:
You said: Hello
Show more lines
Requirements
Shell
pip install duckduckgo-search
Show more lines
Running the Application
Shell
python main.py
Show more lines

To exit:

Plain Text
exit
Show more lines
Project Structure
Plain Text
main.py
Show more lines
search_web() - Performs DuckDuckGo searches.
format_search_results() - Formats search output.
chat() - Processes user input and routes requests.
Main loop handles continuous user interaction.
Repository Description (GitHub About)

A simple Python CLI chatbot that integrates DuckDuckGo web search, allowing users to perform internet searches and receive formatted results directly from the terminal.

Suggested GitHub Topics
Plain Text
python
chatbot
cli
duckduckgo
search-engine
command-line-tool
ai-bot
automation
beginner-project
web-search
Show more lines
Notes

This project is designed as a learning exercise and foundation for more advanced AI assistants. Future enhancements could include:

Integration with LLM APIs (OpenAI, Azure OpenAI, Ollama)
Search result summaries
Conversation history
Voice input/output
GUI or web interface
Context-aware responses
Multi-search provider support (Google, Bing, Brave, etc.)
