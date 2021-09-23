import json
import sys
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from auto_purchase import buy_gpu


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print("\rWill try again in {0} seconds.".format(timer), end="", flush=True)
        time.sleep(1)
        t -= 1
    print("\rTrying again now.\n", end="", flush=True)
    time.sleep(2)
    print("\n")


def telegram_send_message(title, url):
    chat_id = '146257786'
    content = f'{title} [Click Here to Buy]({url})'
    url = f'https://api.telegram.org/bot1972668821:AAHGf7or0snwfacTkrC3FpPdlI_XHyS-FOQ/sendMessage'
    payload = {'chat_id': chat_id,
               'text': content,
               'parse_mode': 'MarkdownV2'}
    print(datetime.now(), "found something, sending message.")
    print(json.dumps(payload))
    response = requests.post(url, data=payload)
    return response.json()


if __name__ == "__main__":
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    products = (
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3070-ti-08g-p5-3797-kl/p/N82E16814487550?Description=evga%20FTW3%20RTX%203070&cm_re=evga_FTW3%20RTX%203070-_-14-487-550-_-Product&quicklink=true',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532?Description=evga%20FTW3%20RTX%203070&cm_re=evga_FTW3%20RTX%203070-_-14-487-532-_-Product',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3070-08g-p5-3767-kl/p/N82E16814487544?Description=evga%20FTW3%20RTX%203070&cm_re=evga_FTW3%20RTX%203070-_-14-487-544-_-Product',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3070-08g-p5-3765-kr/p/N82E16814487531?Description=evga%20FTW3%20RTX%203070&cm_re=evga_FTW3%20RTX%203070-_-14-487-531-_-Product',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3080-10g-p5-3897-kl/p/N82E16814487541?Description=evga%20FTW3%20RTX%203080&cm_re=evga_FTW3%20RTX%203080-_-14-487-541-_-Product&quicklink=true',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?Description=evga%20FTW3%20RTX%203080&cm_re=evga_FTW3%20RTX%203080-_-14-487-518-_-Product&quicklink=true',
    'https://www.newegg.com/global/il-en/evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519?Description=evga%20FTW3%20RTX%203080&cm_re=evga_FTW3%20RTX%203080-_-14-487-519-_-Product&quicklink=true',
    'https://www.newegg.com/global/il-en/gigabyte-geforce-rtx-3070-ti-gv-n307taorus-m-8gd/p/N82E16814932441?Item=N82E16814932441&Description=3070%20ti&cm_re=3070_ti-_-14-932-441-_-Product',
    'https://www.newegg.com/global/il-en/msi-geforce-rtx-3070-ti-rtx-3070-ti-suprim-x-8g/p/N82E16814137665?Item=N82E16814137665&Description=3070%20ti&cm_re=3070_ti-_-14-137-665-_-Product'
    )

    proxies = ('79.139.56.97:3128', '43.247.39.126:443', '51.83.134.249:3128', '168.169.96.2:8080')

    try:
        while True:
            res = ''

            for base_url in products:
                time.sleep(1)
                print(datetime.now(), "fetching page")
                res = requests.get(base_url, headers={'User-Agent': ua})

                if res.status_code != 200:
                    print(datetime.now(), res.text)

                soup = BeautifulSoup(res.text, 'html.parser')
                sold_out_tag = False
                for i in soup.select(".fa-exclamation-triangle"):
                    try:
                        sold_out_tag = i.select_one("span").contents[0]
                        print(sold_out_tag)
                    except AttributeError:
                        pass
                if sold_out_tag == 'OUT OF STOCK ':
                    pass
                else:
                    print(datetime.now(), "found item in stock")
                    print(datetime.now(), base_url, soup.select_one('title').contents[0])
                    page_title = str(soup.select_one('title').contents[0]).split('-')[0]
                    telegram_res = telegram_send_message(page_title, base_url)
                    print(telegram_res)
            print("\n")
            countdown(int(5))

    except KeyboardInterrupt:
        print(datetime.now(), "exiting")
        sys.exit()

    except requests.exceptions.ConnectionError:
        print(datetime.now(), "connection error")
        sys.exit()
