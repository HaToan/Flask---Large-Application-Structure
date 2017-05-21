from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main 
# from .forms import NameForm
# from ..models import User 

@main.route('/', methods=['GET', 'POST'])
def index():
	return "<h1></h1>"
