from commentonx.mail.mock import send_email

config = {}

config["RECAPTCHA_SITE_KEY"] = "NOT_VERY_SECRET_GOOGLE_KEY"
config["RECAPTCHA_SECRET"] = "SUPER_SECRET_GOOGLE_KEY"

config["SESSION_KEY"] = "MAKE_ME_RANDOM"

config["MAIL_BACKEND"] = send_email
config["MAIL_TO"] = "contact@example"
config["MAIL_FROM"] = "feedback@example.com"
config["MAIL_SUBJECT"] = "CommentOnX Feedback"

config["SPARKPOST_KEY"] = "Sparkpost Key"

config["VIEW_CONFIG"] = {}

config["VIEW_CONFIG"]["NAME"] = "X"
# Copy the site key into the view_config
config["VIEW_CONFIG"]["RECAPTCHA_SITE_KEY"] = config["RECAPTCHA_SITE_KEY"]
