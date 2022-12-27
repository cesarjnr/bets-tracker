from celery import Celery

app = Celery('results', broker='redis://localhost:6379', include=['results.tasks'])

if __name__ == '__main__':
    app.start()