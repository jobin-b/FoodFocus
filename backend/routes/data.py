from backend import create_app
app = create_app()

from db import db, get_user, update_day, insert_day
@app.route('/user/<email>', methods=['GET'])
def user(email):
    return get_user(db, email)

