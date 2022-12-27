from .celery import app

@app.task
def get_day_results():
    print('Print hello world')

    return 'Hello World!'