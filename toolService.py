from validationLayer import EmailContent

class EmailService():
    def __init__(self, emailcontext: EmailContent):
        self.emailcontext = emailcontext

    async def EmailFormat(self):
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
