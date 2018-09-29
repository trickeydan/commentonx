from sparkpost import SparkPost


def send_email(app, to_address, from_address, subject, content):

    api_key = app.config["SPARKPOST_KEY"]

    sp = SparkPost(api_key)

    response = sp.transmissions.send(
        recipients=[to_address],
        html=content,
        from_email=from_address,
        subject=subject,
    )

    print(response)
    return True