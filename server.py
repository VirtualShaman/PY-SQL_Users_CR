from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)






@app.route('/users')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)



@app.route('/user/<int:users_id>')
def oneuser(users_id):
    data = {
        'users_id': users_id,
    }
    users = User.get_one(data)
    return render_template('therecanonlybeone.html', users=users)



@app.route('/edit/<int:users_id>', methods=["POST"])
def edit(users_id):

    data={
        'users_id': users_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.edit(data)

    return redirect(f'/user/{users_id}')

@app.route('/change/<int:users_id>', methods=["GET"])
def editP2(users_id):
    data = {
        'users_id': users_id,
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)



@app.route('/delete/<int:users_id>', methods=["GET"])
def delete(users_id):
    data = {
        'users_id': users_id,
    }
    User.get_one(data)
    User.delete(data)
    return redirect('/users')



@app.route('/add', methods=["POST"])
def form():

    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)

    return redirect('/users')


@app.route('/new', methods=["GET"])
def temp():
    return render_template('form.html')





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
