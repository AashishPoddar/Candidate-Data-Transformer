from normalizer.phone import PhoneNormalizer


def main():

    phone = "+91-9798608038"

    normalized = PhoneNormalizer.normalize(phone)

    print(normalized)


if __name__ == "__main__":
    main()