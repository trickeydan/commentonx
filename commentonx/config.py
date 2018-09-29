from commentonx.mail.sparkpost import send_email

config = {}

config["RECAPTCHA_SITE_KEY"] = "6LcEwXIUAAAAAImsYjyZlhAzbIgNlFUOnZr5fp7N"
config["RECAPTCHA_SECRET"] = "6LcEwXIUAAAAALJAISulJ7KD-9bGHMk64kB--4a3"

config["SESSION_KEY"] = "MAKE_ME_RANDOM"

config["MAIL_BACKEND"] = send_email
config["MAIL_TO"] = "contact@trickey.io"
config["MAIL_FROM"] = "feedback@trickey.io"
config["MAIL_SUBJECT"] = "CommentOnDan Feedback"

config["SPARKPOST_KEY"] = "652ee470e7c7b4103cf214960cf0492768492167"

config["VIEW_CONFIG"] = {}

config["VIEW_CONFIG"]["NAME"] = "Dan"
config["VIEW_CONFIG"]["RECAPTCHA_SITE_KEY"] = config["RECAPTCHA_SITE_KEY"]
