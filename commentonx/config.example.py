config = {}

config["RECAPTCHA_SITE_KEY"] = "NOT_VERY_SECRET_GOOGLE_KEY"
config["RECAPTCHA_SECRET"] = "SUPER_SECRET_GOOGLE_KEY"

config["SESSION_KEY"] = "MAKE_ME_RANDOM"

config["VIEW_CONFIG"] = {}

config["VIEW_CONFIG"]["NAME"] = "X"
config["VIEW_CONFIG"]["RECAPTCHA_SITE_KEY"] = config["RECAPTCHA_SITE_KEY"] # Copy the site key into the view_config