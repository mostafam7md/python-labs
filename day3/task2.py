import re

def regex_log_cleaner():
    """ Use regex to extract
        all valid emails
    """
    # Step 1: Create access.log with 10 fake log lines
    fake_logs = [
        "User login: john.doe@example.com",
        "Invalid attempt: hello@@world",
        "Contact: alice_123@gmail.com",
        "Request from: bob.smith@yahoo.com",
        "Error log: invalid.email@.com",
        "System user: test_user@outlook.com",
        "Spam attempt: fake@domain",
        "Report: sarah-jane@company.org",
        "Another invalid: user@@domain..com",
        "Admin: admin123@mydomain.net"
    ]

    with open("./day3/access.log", "w") as log_file:
        log_file.write("\n".join(fake_logs))

    # Step 2: Regex pattern to match valid emails
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    valid_emails = set()

    # Step 3: Extract valid emails
    with open("./day3/access.log", "r") as log_file:
        for line in log_file:
            matches = re.findall(email_pattern, line)
            valid_emails.update(matches)

    # Step 4: Save to valid_emails.txt
    with open("./day3/valid_emails.txt", "w") as email_file:
        for email in sorted(valid_emails):
            email_file.write(email + "\n")
