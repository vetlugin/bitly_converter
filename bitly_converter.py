import os
import requests
from dotenv import load_dotenv
import argparse
load_dotenv()

def cut_http_s_in_url(link):
    ''' Function cut http:// or https:// schema's from link '''
    link = link.replace('http://', '')
    link = link.replace('https://', '')
    return link

def create_shortlink(token, longurl):
    ''' Function for creating bitlinks '''

    if not longurl.startswith('http://') and not longurl.startswith('https://'):
        longurl = 'http://' + longurl

    url_bitlinks = 'https://api-ssl.bitly.com/v4/bitlinks'
    head = {"Authorization":"Bearer " + token}
    json_data = {"long_url" : longurl}
    response = requests.post(url_bitlinks, headers=head, json=json_data)

    if not response.ok:
        return

    created_short_link = response.json().get('link')
    return created_short_link

def get_number_of_shortlink_clicks(token, short_link):
    ''' Function shows click number since all time '''

    url = 'https://api-ssl.bitly.com/v4/bitlinks/' + cut_http_s_in_url(short_link) + '/clicks/summary'
    head = {"Authorization":"Bearer " + token}
    payload = {"units" : -1}

    try:
      response = requests.get(url, headers=head, params=payload)
    except ConnectionError:
      print("Проблемы соединения с сервером")
    except HTTPError:
      print("Ошибка при выполнении запроса")
    except Timeout:
      print("Превышено время ожидания запроса")

    total_clicks = response.json().get('total_clicks')
    return total_clicks

def test_url_long_or_short(token, short_link):
    ''' Function test arg is not shortrlink? '''

    url = 'https://api-ssl.bitly.com/v4/bitlinks/' + cut_http_s_in_url(short_link)
    head = {"Authorization":"Bearer " + token}
    response = requests.get(url, headers=head)
    return response.ok

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert longurl to bit.ly url')
    parser.add_argument('name', help='Long URL to convert')
    args = parser.parse_args()

    token = os.getenv("TOKEN")
    ask_url = args.name

    try:
        if test_url_long_or_short(token, ask_url):
            number_of_click = get_number_of_shortlink_clicks(token, ask_url)
            print(number_of_click)
        else:
            short_link = create_shortlink(token, ask_url)
            print (short_link)
    except TypeError:
        print("Ошибка при авторизации на сервисе Bitly")
