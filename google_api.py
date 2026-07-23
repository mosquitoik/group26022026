import requests
from pprint import pprint

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=AUkAhnTBtB6aveRoROBa31HN_m-szX0FerbUM1dQsQ3KrF7Y-mPNlP9qySvdLm5DQdf9fcBzm1U8VLcaFjzT6X8i_t_4u-473T5s4cAUkqUKbtLEHqH2W9_fsYU1hFZ1wRX5StNsfc8rpZF9U18BEbUpuqSjorkxO5wTFR6X8B1Hji5AO37HN4iBlnTSNS9VBnwik9dSKPTuHJuJ5aXkUbEfQx8LqGckvz-FVi0UkzCarMSRCLw1RdvlyouBHlK0mnG43xwUZ_IzC4BzFdLLVSZIzHzlngiWSw&lib=MXZqoPmqvFP1u4KzaYkANZKNKe58B53cM'
response = requests.get(url=url, params={})
response_json = response.json()

pprint(response_json)

trip = response_json['trip']

total_charity = 0
for row in trip:
    total_charity += row['charity']

print(f'{total_charity=}')