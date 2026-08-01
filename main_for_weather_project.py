import utils
from pywebio.input import input, input_group
from pywebio.output import put_text, put_success
from pywebio import start_server
from pywebio.session import run_js


# chi23@ukr.net
def main():

    data = input_group(
        "Запит на погодну погоду",
        [
            input(label="City", name="city", required=True),
            input(label="Email", name="email", required=True),
            input(label="Name", name="name", required=True),
        ],
    )
    current_weather = utils.get_weather_info(data["city"])
    email_body = utils.create_weather_report(current_weather)

    recipients = [  data["email"]  ]

    utils.send_email(
        recipients,
        email_body,
        mail_subject=f'Weather in {data["city"]}',
        # attachment='log.csv'
    )

    put_success("Email was sent. The page reloads in 5 seconds...")

    run_js("""
        setTimeout(() => {window.location.reload();}, 5000);
    """)
    # current_weather = utils.get_weather_info(city)
    # put_text(f"Температура у {city}: {current_weather['temperature']}")


start_server(
    main,
    host="0.0.0.0",
    port=8080,
    debug=True
)