import requests

headers = {
    'authority': 'www.bing.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'origin': 'https://www.bing.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bing.com/translator?mkt=zh-CN',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


def get_translation(text, from_code, to_code):
    data = {
        'text': text,
        'fromLang': from_code,
        'to': to_code
    }
    response = requests.post('https://www.bing.com/ttranslatev3', headers=headers, data=data)
    return response.json()[0]['translations'][0]['text']


while True:
    text = input('>>> ')
    text = get_translation(text, 'zh-Hans', 'en')
    # print(text)
    text = get_translation(text, 'en', 'ja')
    # print(text)
    text = get_translation(text, 'ja', 'zh-Hans')
    print(text)
    print()
