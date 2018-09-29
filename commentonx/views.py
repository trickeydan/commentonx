from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from commentonx import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:

        if 'feedback' in request.form:
            if len(request.form['feedback']) >= 20:

                flash('Thank you! Your feedback is on it\'s way.', 'success')
            else:
                flash('Please provide at least 20 characters of feedback', 'error')
        else:
            flash('You need to provide feedback!', 'error')
        return redirect(url_for('index'))

