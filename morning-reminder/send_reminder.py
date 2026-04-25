import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta


def read_tasks(filepath="morning-reminder/tasks.txt"):
    with open(filepath, "r") as f:
        lines = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]
    return lines


def send_email(tasks):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    recipient = os.environ["GMAIL_USER"]

    tz = timezone(timedelta(hours=8))
    today = datetime.now(tz).strftime("%A, %d %B %Y")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Good morning! Your To-Do List for {today}"
    msg["From"] = sender
    msg["To"] = recipient

    task_plain = "\n".join(f"  {t}" for t in tasks)
    text = f"Good morning!\n\nYour tasks for {today}:\n\n{task_plain}\n\nHave a productive day!"

    task_html = "".join(
        f'<li style="padding: 6px 0;">{t}</li>' for t in tasks
    )
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 580px; margin: 0 auto; padding: 24px; color: #2c3e50;">
        <h2 style="color: #e67e22;">Good morning! &#127774;</h2>
        <p style="font-size: 14px; color: #7f8c8d;">{today}</p>
        <h3 style="border-bottom: 2px solid #e67e22; padding-bottom: 6px;">Your To-Do List</h3>
        <ul style="line-height: 1.8; font-size: 15px;">
            {task_html}
        </ul>
        <p style="margin-top: 24px; color: #27ae60; font-weight: bold;">Have a productive day!</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

    print(f"Reminder sent to {recipient}")


if __name__ == "__main__":
    tasks = read_tasks()
    send_email(tasks)
