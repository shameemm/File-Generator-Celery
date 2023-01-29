from celery import shared_task
import csv
from .models import TaskLog
import random
from django.core.files.storage import default_storage

@shared_task
def generate_file(filename,count):
    
    file_path = default_storage.path(f"data/"+filename+".csv")
    file = default_storage.open(file_path, 'w')
    writer = csv.writer(file)
    
    for i in range(count):
        writer.writerow([random.randint(0,100) for _ in range(3)])
    file.close()
    return 'file created'

def run_generate_file_task(filename,count):
    task = generate_file.apply_async((filename,count))
    task_log = TaskLog(id=task.id, args=str((filename,count)), status='PENDING')
    task_log.save()
    task.wait()
    if task.successful():
        task_log.status = 'SUCCESS'
    else:
        task_log.status = 'FAILED'
    task_log.save()