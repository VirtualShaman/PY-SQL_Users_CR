from flask_app.controllers import user
from flask_app import app
# ...server.py

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
