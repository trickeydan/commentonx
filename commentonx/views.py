from commentonx import app
from commentonx.email import send_feedback
from commentonx.recaptcha import is_human
from flask import flash, redirect, render_template, request, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:

        if 'feedback' in request.form:
            if len(request.form['feedback']) >= 20:

                if 'g-recaptcha-response' in request.form:

                    if is_human(request.form['g-recaptcha-response']):

                        send_feedback(request.form['feedback'])

                        flash('Thank you! Your feedback is on it\'s way.', 'success')
                    else:
                        flash('Please verify that you are human', 'error')
                else:
                    flash('Please verify that you are human', 'error')
            else:
                flash('Please provide at least 20 characters of feedback', 'error')
        else:
            flash('You need to provide feedback!', 'error')
        return redirect(url_for('index'))
