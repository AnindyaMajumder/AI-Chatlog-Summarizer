import os
import re


class ChatParser:
    """
    A class to parse chat logs and separate messages by speaker.
    """
    
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.messages = {"User": [], "AI": []}
        self.document = ""
        self.parse()
    
    def load_file(self):
        if not self.file_path:
            raise ValueError("No file path provided.")
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Chat log file not found: {self.file_path}")
              
        return True
    
    def parse(self):
        if self.load_file() is True:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            pattern = r'(User|AI): (.*?)(?=User:|AI:|$)'
            matches = re.findall(pattern, content, re.DOTALL)
            
            for speaker, message in matches:
                clean_message = message.strip()
                self.document += clean_message + "\n"
                if clean_message:
                    self.messages[speaker].append(clean_message)
        else:
            raise ValueError("Failed to load file.")
    
    def get_messages(self):
        return self.document
    
    # Message Statistics
    def user_messages(self):
        return len(self.messages["User"])

    def ai_messages(self):
        return len(self.messages["AI"])
    
    def total_messages(self):
        return self.user_messages() + self.ai_messages()