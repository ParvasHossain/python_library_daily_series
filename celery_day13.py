from celery import Celery

# Initialize task app with Redis as Broker & Result Backend
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def process_data_pipeline(dataset_id: str):
    # Runs asynchronously in background Celery worker process
    return f"Dataset {dataset_id} processed successfully"

# Producer code (e.g., inside a Flask/FastAPI route)
# task = process_data_pipeline.delay("DS-9082")
# print(f"Task ID queued: {task.id}")