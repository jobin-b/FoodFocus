from backend import app


@app.route('/')
def hello_world():
    return 'Jobin!!'