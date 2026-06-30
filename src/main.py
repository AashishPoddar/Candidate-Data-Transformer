from parser.csv_parser import CSVParser
from parser.resume_parser import ResumeParser
from normalizer.phone import PhoneNormalizer
from normalizer.email import EmailNormalizer
from merger.merge import MergeEngine
from confidence.confidence import ConfidenceEngine
from config_loader import ConfigLoader
from projection.projector import Projector
from validator import Validator

import argparse
import json
import os


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

    parser = argparse.ArgumentParser(
        description="Candidate Data Transformer"
    )

    parser.add_argument(
        "--config",
        default="config/default_config.json",
        help="Configuration file"
    )

    args = parser.parse_args()

    config = ConfigLoader.load(args.config)

    final_output = Projector.project(
        merged_profile,
        config
    )

    if Validator.validate(final_output):

        os.makedirs("output", exist_ok=True)

        with open(
            "output/final_output.json",
            "w"
        ) as file:

            json.dump(
                final_output,
                file,
                indent=4
            )

    print("\nFinal Candidate Profile\n")

    print(
        json.dumps(
            final_output,
            indent=4
        )
    )

    print("\nOutput saved successfully.")

    print(
        "Location: output/final_output.json"
    )


if __name__ == "__main__":
    main()