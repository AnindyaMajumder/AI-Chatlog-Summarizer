from chat_parser import ChatParser
import os

if __name__ == "__main__":
    # Get the absolute path to the data directory
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(current_dir, 'data')
    chat_file = os.path.join(data_dir, 'chat.txt')
    
    # Call the ChatParser class
    parser = ChatParser(chat_file)
    
    # Print the results
    # print("Parsed chat messages:")
    # print(parser.get_messages())
    
    # Print summary
    print("\nSummary:")
    print(f"- The conversation had {parser.total_messages()} exchanges.")