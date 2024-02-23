import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import schedule
import time

def send_reminder_email():
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receivers = ["rayhanmohamedgui@gmail.com"]

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(receivers)
    message['Subject'] = "Reminder: Fill in the Namaz Sheet"

    body = "Hi Rayhan,\n\nThis is a friendly reminder to fill in the Namaz attendance Sheet.\n https://docs.google.com/spreadsheets/d/1jhjns5o8u9-bktoqhTKtrWg-YIO8qQg4-s7VtTIwVdI/edit#gid=0  Thank you!\n\nBest regards,\nMusaib Sharieff"

    message.attach(MIMEText(body, 'plain'))

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receivers, message.as_string())
        print("Reminder email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", e)

# Schedule the task to run daily at 8 PM IST
schedule.every().day.at("17:23").do(send_reminder_email)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
