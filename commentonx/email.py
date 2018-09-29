from commentonx import app
from flask import render_template

def send_feedback(feedback):

    send_email = app.config["MAIL_BACKEND"]

    to_address = app.config["MAIL_TO"]
    from_address = app.config["MAIL_FROM"]
    subject = app.config["MAIL_SUBJECT"]
    content = render_template("email.html", feedback=feedback)

    send_email(to_address, from_address, subject, content)
