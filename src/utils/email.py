import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from jinja2 import Environment, FileSystemLoader, select_autoescape


# function to render email body using a template
def render_email_body(**kwargs):
    """
        
        Render HTML for email using a template.
    
    """
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html"]),
    )
    template = env.get_template("email.html")
    return template.render(**kwargs)


# Email configuration
sender_email = "SENDER_MAIL@HERE.com"
receiver_email = "RECEIVER_MAIL@HERE.com"
subject = "Currency Alert"
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Port for Gmail's SMTP server
smtp_username = "SENDER_MAIL@HERE.com"
smtp_password = ""


# Create a MIME multipart message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the HTML content as plain text
async def send_email(name, to, context):
    msg.attach(MIMEText(render_email_body(**context), "html"))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:  
        print("Email could not be sent. Error:", str(e))
