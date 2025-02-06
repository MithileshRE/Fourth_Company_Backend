from celery import Celery

# Define Celery app
celery_app = Celery(
    "tasks",
    broker="amqp://guest@localhost//",  # Change to "amqp://guest@localhost//" for RabbitMQ
    backend="redis://localhost:6379/0"
)

# Example Celery task
@celery_app.task
def add(x, y):
    return x + y
