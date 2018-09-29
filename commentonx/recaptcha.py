import json

import requests
from commentonx import app


def is_human(response):
    secret = app.config["RECAPTCHA_SECRET"]
    payload = {'response': response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']
