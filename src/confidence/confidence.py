class ConfidenceEngine:
    """
    Calculates confidence score
    and stores provenance.
    """

    @staticmethod
    def generate(merged_profile):

        provenance = {

            "full_name": {
                "source": "Resume PDF",
                "method": "Regex"
            },

            "email": {
                "source": "Resume PDF",
                "method": "Regex"
            },

            "phone": {
                "source": "Resume PDF",
                "method": "Regex"
            },

            "current_company": {
                "source": "Recruiter CSV",
                "method": "CSV Column"
            },

            "title": {
                "source": "Recruiter CSV",
                "method": "CSV Column"
            }

        }

        confidence = {

            "full_name": 0.95,
            "email": 0.95,
            "phone": 0.95,
            "current_company": 0.90,
            "title": 0.90

        }

        merged_profile["provenance"] = provenance

        merged_profile["confidence"] = confidence

        return merged_profile