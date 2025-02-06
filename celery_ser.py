from clientsService import celery_app
from botocore.exceptions import NoCredentialsError, BotoCoreError
from clientsService import ses_client

@celery_app.task
def add(x, y):
    return x + y

#@celery_app.task
def sendMail(EmailFormat,sesClient=ses_client):
        try:
            response = sesClient.send_email(**EmailFormat)
            print("Email sent! Message ID:", response["MessageId"])
            return True
        except (NoCredentialsError, BotoCoreError) as e:
            print("Error sending email:", str(e))
            return False    