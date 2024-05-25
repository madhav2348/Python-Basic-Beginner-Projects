#pip install schedule
#textbelt.com to send message
#pip install request

from credentials import mobile_number

import schedule
import time
#mobile number is to be typeed

import requests

def send_mesaage():
    resp = requests.post('https://textbeltcom/text',{
        'phone': mobile_number,
        'message':'hey good morning',
        'key':'textbelt'
    })

    print(resp.json())

schedule.every().day.at('06:00')


#schedule.every(10).seconds.do(send_message)
# while True:
#     schedule.run_pending()
#     time.sleep(1)