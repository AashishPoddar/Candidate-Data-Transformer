import phonenumbers


class PhoneNormalizer:

    @staticmethod
    def normalize(phone):

        if phone is None:
            return None

        try:
            parsed_number = phonenumbers.parse(phone, "IN")

            return phonenumbers.format_number(
                parsed_number,
                phonenumbers.PhoneNumberFormat.E164
            )

        except:

            return None