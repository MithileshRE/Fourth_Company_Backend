import boto3
from botocore.exceptions import NoCredentialsError, BotoCoreError
from celery import Celery


ses_client = boto3.client("ses", region_name="ap-south-1",
aws_access_key_id="AKIAU5LH5ZBP2LGDDLSU",
aws_secret_access_key="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"
)


celery_app = Celery(
    "tasks",
    broker="amqp://guest@localhost//", 
    backend="redis://localhost:6379/0"
)