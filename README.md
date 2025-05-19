# AI Chatlog Summarizer

AI Chatlog Summarizer is a Python tool that parses chat logs between a user and an AI, analyzes the conversation, and generates concise summaries. It extracts key statistics, identifies main topics, and highlights important keywords using NLP techniques.

## Features

- Parses chat logs and separates messages by speaker (User/AI)
- Calculates message statistics (number of exchanges, etc.)
- Extracts main conversation topics using LDA
- Identifies most common keywords using TF-IDF
- Simple command-line interface

## Project Structure

```
data/
  chat.txt                # Example chat log
src/
  __init__.py             # Main entry point
  chat_parser.py          # Chat log parsing logic
  text_analyzer.py        # Text analysis and summarization
requirements.txt          # Python dependencies
```

## Installation

1. **Clone the repository** (if not already done):

   ```sh
   git clone https://github.com/AnindyaMajumder/AI-Chatlog-Summarizer.git
   cd AI-Chatlog-Summarizer
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Add your chat logs**:  
   Place your `.txt` chat files in the `data/` directory. Each message should be prefixed with `User:` or `AI:`.

2. **Run the summarizer**:

   ```sh
   python -m src
   ```

   The script will process all `.txt` files in the `data/` folder and print summaries to the console.

## Example Output

```
Basic Summary for chat.txt:
- The conversation had 4 exchanges.
- The user asked mainly about python and development.
- Most common keywords: python, development, data, analysis, web.
_________________________
```

## License

This project is licensed under the [Apache License Version 2.0](LICENSE).
