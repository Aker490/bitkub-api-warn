import requests

def main(message):
    url = 'https://notify-api.line.me/api/notify'
    token = '3fZ9USSjH3l4Tp1s1w66jCAhxINsr2vUiVE6cxCQs2Q' ##ตรงนี้ใส่โทเค่น
    header = {'content-type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
     
    response = requests.post(url, headers=header, data={'message': message})

url = 'https://api.bitkub.com/api/market/ticker'
price = 0 #ตรงนี้ไม่ต้องเปลี่ยน

while True:
    req= requests.get(url)
    data = req.json()
    last = data['THB_BTC']['last']
    high = data['THB_BTC']['high24hr']
    low = data['THB_BTC']['low24hr']

    if price != last: #บอทจะไม่ส่งข้อความจนกว่าค่า (price จะเท่ากับค่า last) จะเปลี่ยน
        msg = f"Current Bitcoin price:\n" \
                    f"ราคา: {last} THB\n" \
                    f"------------------------\n" \
                    f"24 H สูงสุด: {high} THB\n" \
                    f"24 H ต่ำสุด: {low} THB\n" \
                    f"------------------------\n"
        main({msg})
        price = last #ตรงนี้มันจะตั้งค่า price ให้เท่ากับค่า last
