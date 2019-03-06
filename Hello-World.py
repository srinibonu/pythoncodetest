import os, csv, time, socket, ipaddress, glob, re
from os import path 
from flask import Flask, flash, request, render_template, redirect, url_for
from werkzeug import secure_filename

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

	
@app.route("/")
def index():
    return render_template("HelloWorld.html")

    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
