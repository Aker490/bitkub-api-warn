import requests

def main(message):
    url = 'https://notify-api.line.me/api/notify'
    token = ''
    header = {'content-type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
     
    response = requests.post(url, headers=header, data={'message': message})

url = 'https://api.bitkub.com/api/market/ticker'
price = 0

while True:
    req= requests.get(url)
    data = req.json()
    last = data['THB_BTC']['last']
    high = data['THB_BTC']['high24hr']
    low = data['THB_BTC']['low24hr']

    if price != last:
        msg = f"Current Bitcoin price:\n" \
                    f"ราคา: {last} THB\n" \
                    f"------------------------\n" \
                    f"24 H สูงสุด: {high} THB\n" \
                    f"24 H ต่ำสุด: {low} THB\n" \
                    f"------------------------\n"
        main({msg})
        price = last
