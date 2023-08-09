import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "Email"
password = "Password"

imap = imaplib.IMAP4_SSL(imap_server, 993)

imap.login(email_address, password)

while True:
    imap.select('INBOX')

    _, msgnums = imap.search(None, "UNSEEN")  # Only fetch unseen (unread) messages (Do not edit this line!)

    for msgnum in msgnums[0].split():
        imap.select('INBOX')  # Make sure you're in the correct mailbox state
        _, data = imap.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])

        print(f"Message Number: {msgnum}")
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"Subject: {message.get('Subject')}")
        print("Content: ")
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                print(part.as_string())

        # Mark the email as read
        imap.store(msgnum, '+FLAGS', '\Seen')
        
    # Add a delay before checking for new messages again
    import time
    time.sleep(10)  # Sleep for 10 seconds before checking again


