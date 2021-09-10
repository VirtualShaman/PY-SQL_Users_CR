from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)


@app.route('/users')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/add', methods=["POST"])
def form():

    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.save(data)

    # User.first_name = request.form.get("first_name")

    return redirect('/users')

@app.route('/new', methods=["GET"])
def temp():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
