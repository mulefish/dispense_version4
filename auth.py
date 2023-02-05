from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

app = Flask(__name__)
login_manager = LoginManager(app)

# Create a fake user class for example purposes
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = id # // str(id)
        self.password = self.name
        print(f"{self.id} name={self.name} password={self.password} ")
# Create a dictionary to store our fake users
users = {}

# Create a user with the id 1
users["a"] = User("a")

# Create a login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    print("login")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            if password == users[username].password:
                login_user(users[username])
                print("work {}".format( users[username].password))
                print("URL: {} ".format( url_for('protected')))

                return redirect(url_for('protected'))
            else:
                print("ELSE")
                print("username1: " + username )
                print("password1: " + password)
                # print("username2: " + users[username].username) 
                # print("password2: " + users[username].password) 
        else:
            print("username is NOPE " + username )
            print(users)
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
            Hello
        </form>
    '''
# Create a protected route
@app.route('/protected')
@login_required
def protected():
    print("protected")
    return 'Logged in as: ' + current_user.name

# Create a logout route
@app.route('/logout')
def logout():
    print("logged out")
    logout_user()
    return 'Logged out'

# Tell Flask-Login how to load a user
@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    # return users.get(int(user_id))
    return users.get(user_id)

if __name__ == '__main__':
    print("agogo")
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
