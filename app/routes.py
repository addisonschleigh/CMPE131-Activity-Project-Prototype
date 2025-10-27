from flask import render_template
from .forms import LoginForm
from app import myapp_obj

@myapp_obj.route('/')
def home():
    return '<h1>Welcome to House Rent App</h1>'

@myapp_obj.route('/listings')
def lisitings():
    return '<h1>House 1</h1>' \
    '<h1>House 2</h1>'

@myapp_obj.route('/details')
def details():
    return render_template('details.html')

@myapp_obj.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'sign in', form = form)

@myapp_obj.route('/dashboard')
def dashboard():
    return '<h1>Name</h1>' \
    '<h1>Email</h1>'