from parser.csv_parser import CSVParser


def main():
    parser = CSVParser("input/recruiter.csv")

    data = parser.parse()

    print(data)


if __name__ == "__main__":
    main()