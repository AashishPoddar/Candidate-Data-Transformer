import pdfplumber
import re


class ResumeParser:
    """
    Reads a resume PDF and extracts basic candidate information.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        """
        Extract all text from the PDF.
        """
        text = ""

        try:
            with pdfplumber.open(self.file_path) as pdf:

                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception as e:
            print(f"Error reading PDF: {e}")

        return text

    def parse(self):

        text = self.extract_text()

        email = self.extract_email(text)
        phone = self.extract_phone(text)
        name = self.extract_name(text)

        return {
            "name": name,
            "email": email,
            "phone": phone
        }

    def extract_email(self, text):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        if match:
            return match.group()

        return None

    def extract_phone(self, text):

        match = re.search(
            r"(\+91[- ]?)?[6-9]\d{9}",
            text,
        )

        if match:
            return match.group()

        return None

    def extract_name(self, text):

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if line != "":
                return line

        return None