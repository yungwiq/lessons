import requests


def icq(phone):
    try:
        url = 'https://u.icq.net/api/v70/rapi/auth/sendCode'
        payload = {"reqId": "94446-1645359697",
                   "params": {"phone": phone,
                              "language": "ru-RU",
                              "route": "sms",
                              "devId": "ic1rtwz1s1Hj1O0r",
                              "application": "icq"}}
        a = requests.post(url, json=payload)
        print(a.text)
    except Exception as e:
        print(e)


icq(7912354823)
