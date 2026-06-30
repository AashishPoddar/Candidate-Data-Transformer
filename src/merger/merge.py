class MergeEngine:
    """
    Merge data coming from multiple sources into
    one canonical candidate profile.
    """

    @staticmethod
    def merge(resume_data, csv_data):

        merged = {}

        # Resume fields
        merged["full_name"] = resume_data.get("name")
        merged["email"] = resume_data.get("email")
        merged["phone"] = resume_data.get("phone")

        # CSV fields
        if len(csv_data) > 0:

            merged["current_company"] = csv_data[0].get("current_company")
            merged["title"] = csv_data[0].get("title")

        return merged