from parser.csv_parser import CSVParser
from parser.resume_parser import ResumeParser
from normalizer.phone import PhoneNormalizer
from normalizer.email import EmailNormalizer
from merger.merge import MergeEngine
from confidence.confidence import ConfidenceEngine
from config_loader import ConfigLoader
from projection.projector import Projector

import json


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
    merged_profile = ConfidenceEngine.generate(
        merged_profile
    )

    config = ConfigLoader.load(
        "config/default_config.json"
    )

    final_output = Projector.project(
        merged_profile,
        config
    )

    print("\nFinal Candidate Profile\n")

    print(
        json.dumps(
            final_output,
            indent=4
        )
    )


if __name__ == "__main__":
    main()