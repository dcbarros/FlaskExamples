from flask import Blueprint,render_template


auths = Blueprint('auths', __name__)


@auths.route('login')
def login():
    return render_template('login.html')


@auths.route('logout')
def logout():
    return "<h1>Logout</h1>"


@auths.route('signIn')
def signUp():
    return render_template('signIn.html')
