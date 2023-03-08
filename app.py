import requests
from bs4 import BeautifulSoup
import telegram
import schedule
import time
import ssl
import urllib.request
import json
import urllib3
import asyncio

# Telegram
async def bot_send(msg):
    telegram_token = "5128692345:AAHkO-3JZ9tZYP2hrS5UAlnYCrO0PiO09_A"
    bot = telegram.Bot(token = telegram_token)
    async with bot:
        await bot.send_message(text=msg, chat_id="444879086")


palyload_session = {
  "captchaId": "0ebfd2967a",
  "captcha": "nhqyx",
  "userId": "goodjjt",
  "userPassword": "c7bb709bb64d3b0e753866e5e6945adf0fc2399a2010",
  "autoLogin": 0,
  "returnUrl": ""
}
session = requests.session()
response_session = session.post('https://front.wemakeprice.com/api/edge/login.json', data=palyload_session)
# print(response_session.headers) # 헤더 확인
# print(session.cookies.get_dict())  # 저장된 세션 확인

url = 'https://onestop.wemakeprice.com/proxy/onestop/api/v1/rs/seatStateInfo'
headers = {
    'Cookie': 'setGM=8acda45fe9b3042a67fc613d3253beb47c7e3b85316f4cd26d7e39987ad3199d1b9b4a23175eb6abba0ec7a48ab20ad908fc9c63789a85512378590a1d2125be4ee3c486ef1a44277212c232c446f592c1dd83b79b613814b3d9832d2b208cbb1a0957245b27a5ab7e9714d5ef07be1c05fa7abd6b8248bb61c862751172173bdea69e4307e480e90749341d92d0d4d7970f1b01c76f27c2b7caa59ae7ff1a237e1f5644b32aa16c2dd9b4fef11aed9eeef4e2d26185cd56f9e8aeaae698f677;',
    }

def message1():
    seatGradeList = ['[올빼미존] (A)오토캠핑 (전기X)', '[올빼미존] (B)오토캠핑 (전기X)', '[올빼미존] (C)오토캠핑 (전기X)', '[올빼미존] (D)오토캠핑 (전기X)', '[올빼미존] (E)오토캠핑 (전기X)', '[올빼미존] (F)오토캠핑 (전기X)'
         , '[패밀리존] (A)오토캠핑 (전기X)' , '[패밀리존] (B)구미캠핑장 평상존 (전기X)' , '[패밀리존] (B)구미캠핑장 오토캠핑, 4mX5m, 전기', '[패밀리존] (B)구미캠핑장 오토캠핑, 9mX9m, 전기O'
         , '[패밀리존] (B)구미캠핑장 B카라반, 전기O', '[패밀리존] (B)구미캠핑장 C카라반, 전기O', '[패밀리존] 개인카라반, 전기O', '방문객 입장권']
    cnt = 0
    message = "[" + "고아웃 (03월 31일)" + "] " + '\n'
    link = "https://ticket.wemakeprice.com/product/3000009272?search_keyword=%25EA%25B3%25A0%25EC%2595%2584%25EC%259B%2583&_service=5&_no=1"
    for index, value in enumerate(seatGradeList):
        response = session.post(url, data={'prodSeq': '3000009272', 'sdSeq': '1', 'seatId': str(index+1)}, headers=headers)
        jsonData = response.json()
        # print(value, " : ", jsonData)
        if jsonData.get("totVisitorCnt") != jsonData.get("visitorCnt") :
            print(value, ' : ', jsonData.get("totVisitorCnt"), "(", jsonData.get("visitorCnt"), ")")
            if value != '방문객 입장권' : 
                cnt += 1
                message = message + ' - ' + value + '\n'   
    if cnt > 0:
        message = message + link
        asyncio.run(bot_send(message)) 

# step3.실행 주기 설정
schedule.every(5).seconds.do(message1)
# schedule.every(1).minutes.do(message1)

while True:
    schedule.run_pending()
    time.sleep(1)


