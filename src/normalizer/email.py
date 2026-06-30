class EmailNormalizer:

    @staticmethod
    def normalize(email):

        if email is None:
            return None

        return email.strip().lower()