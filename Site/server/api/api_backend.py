from server.models.model import db, User
from server.app import app

u = User(username='test', email='at')
with app.app_context():
    db.create_all()
    users = User.query.all()  # Fetch all users from the database
    result = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    print(result)

