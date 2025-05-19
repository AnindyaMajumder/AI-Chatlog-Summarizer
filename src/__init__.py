from chat_parser import ChatParser
from text_analyzer import TextAnalyzer
import os

if __name__ == "__main__":
    # Get the absolute path to the data directory
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(current_dir, 'data')
    chat_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.txt')]
    
    for chat_file in chat_files:
        file_name = os.path.basename(chat_file)
        print(f"\nBasic Summary for {file_name}:")    
        parser = ChatParser(chat_file)
        print(f"- The conversation had {parser.total_messages()} exchanges.")
        
        analyzer = TextAnalyzer(parser)
        print(f"- The user asked mainly about {analyzer.conversation_topic()}.")
        print(f"- Most common keywords: {analyzer.find_keywords()}.")
    print("_________________________\n")