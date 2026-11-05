import re
import os
from datetime import datetime

class EmailExtractor:
    """An automation script that extracts and isolates email addresses from raw text files."""
    
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        
        self.email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    def extract_emails(self):
        """Reads the input file and returns a list of unique email addresses."""
        if not os.path.exists(self.input_file):
            print(f"Error: The file '{self.input_file}' does not exist in this directory.")
            return []

        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                content = file.read()
                
            
            raw_emails = re.findall(self.email_pattern, content)
            
            
            unique_emails = sorted(list(set(raw_emails)))
            return unique_emails
            
        except Exception as e:
            print(f"❌ An error occurred while reading the file: {e}")
            return []

    def save_emails(self, emails: list):
        """Saves the extracted emails to the output file with a timestamp."""
        if not emails:
            print("⚠️ No emails were found to save.")
            return

        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                file.write(f"--- Email Extraction Report ---\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total Unique Emails Found: {len(emails)}\n")
                file.write("="*31 + "\n\n")
                
                for email in emails:
                    file.write(email + "\n")
                    
            print(f" Success! Extracted {len(emails)} unique emails.")
            print(f" Saved securely to: {self.output_file}")
            
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")


if __name__ == "__main__":
    print("Initializing Task Automation Script...")
    
   
    source_document = "sample_data.txt"
    destination_document = "extracted_emails.txt"
    
    
    extractor = EmailExtractor(source_document, destination_document)
    found_emails = extractor.extract_emails()
    extractor.save_emails(found_emails)