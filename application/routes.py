from flask import render_template, url_for, redirect, request
from application import app, db
##from application.models import arg
##from application.forms import arg, arg 


@app.route('/')
def no_url():
    return  redirect('/home')

@app.route('/home')
def home_url():
    return  "Home for future students"

@app.route('/enroll')
def enroll_url():
    return  "Hello future students"