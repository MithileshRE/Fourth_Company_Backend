from validationLayer import EmailContent
from celery_ser import sendMail


class EmailService():
    def __init__(self, emailcontext: EmailContent):
        self.emailcontext = emailcontext

    def EmailFormat(self):
        return {
            "Source": self.emailcontext.SENDER,
            "Destination": {"ToAddresses": [self.emailcontext.RECIPIENT]},
            "Message": {
                "Subject": {"Data": self.emailcontext.SUBJECT},
                "Body": {
                    "Text": {"Data": self.emailcontext.BODY_TEXT},
                    "Html": {"Data": self.emailcontext.BODY_HTML},
                },
            },
        }


x = {
    "SUBJECT": "Its a subject",
    "BODY_TEXT": "Hello,\n\nThis is a test email from Amazon SES using Boto3 in Python_Application.",
    "BODY_HTML": """<head></head>
    <body>
    <h1>Hello!</h1>
    <p>This is a test email from <strong>Amazon SES</strong> using Boto3 in Python.</p>
    </body>
    </html>"""
}
obj1 = EmailService(EmailContent(**x))
result = obj1.EmailFormat()
print(sendMail.delay(result).get())
