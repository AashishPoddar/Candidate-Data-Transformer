from parser.resume_parser import ResumeParser


def main():

    parser = ResumeParser("input/resume.pdf")

    data = parser.parse()

    print(data)


if __name__ == "__main__":
    main()