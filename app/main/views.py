from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from flask import make_response, redirect
from . import main 
# from .forms import NameForm
# from ..models import User 


@main.route('/', methods=['GET', 'POST'])
def index():
	return "<h1>Hello</h1>"

@main.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
	return render_template('user.html', name=name)

@main.route('/user_agent')
def userAgent():
	return '<p>Your browser is %s</p>' % request.headers.get("User-Agent")

@main.route("/cookie")
def setcookie():
	response = make_response("<h1>This document carries a cookies!</h1>")
	response.set_cookie("answer", "42")
	return response

@main.route('/redirect')
def myredirect():
	return redirect('http://google.com')