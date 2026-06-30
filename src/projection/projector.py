class Projector:
    """
    Creates the final output
    according to the configuration.
    """

    @staticmethod
    def project(profile, config):

        projected = {}

        fields = config.get("fields", [])

        for field in fields:

            if field in profile:

                projected[field] = profile[field]

        return projected