def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Attendees is not a list of dictionaries.")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        placeholders = {"name", "event_title", "event_date", "event_location"}
        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"
            else:
                value = str(value)

            invitation = invitation.replace(f"{{{placeholder}}}", value)

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
