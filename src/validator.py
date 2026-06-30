class Validator:
    """
    Validates the final output profile.
    """

    REQUIRED_FIELDS = [
        "full_name",
        "email",
        "phone"
    ]

    @staticmethod
    def validate(profile):

        missing = []

        for field in Validator.REQUIRED_FIELDS:

            if field not in profile:
                missing.append(field)

        if missing:

            print("Validation Failed")
            print("Missing Fields:", missing)

            return False

        print("Validation Successful")

        return True