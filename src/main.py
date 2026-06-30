from parser.csv_parser import CSVParser
from parser.resume_parser import ResumeParser

from normalizer.phone import PhoneNormalizer
from normalizer.email import EmailNormalizer
from merger.merge import MergeEngine


def main():


    # Read CSV

    csv_parser = CSVParser("input/recruiter.csv")
    csv_records = csv_parser.parse()

    
    # Read Resume
    
    resume_parser = ResumeParser("input/resume.pdf")
    resume_data = resume_parser.parse()

    
    # Normalize Resume Data
    
    resume_data["phone"] = PhoneNormalizer.normalize(
        resume_data["phone"]
    )

    resume_data["email"] = EmailNormalizer.normalize(
        resume_data["email"]
    )

    print("\nResume Data")
    print(resume_data)

    print("\nCSV Records")
    print(csv_records)

    merged_profile = MergeEngine.merge(
    resume_data,
    csv_records
    )

    print("\nMerged Profile")
    print(merged_profile)


if __name__ == "__main__":
    main()