import requests

headers = {
    'origin': 'https://cn.bing.com',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'cn.bing.com',
    'referer': 'https://cn.bing.com/translator/',
    'dnt': '1',
}


def get_translation(text, from_code, to_code):
    data = {
        'text': text,
        'from': from_code,
        'to': to_code
    }
    response = requests.post(
        'https://cn.bing.com/ttranslatev3', headers=headers, data=data)
    return response.json()[0]['translations'][0]['text']


while True:
    text = input('>>> ')
    text = get_translation(text, 'zh-CHS', 'en')
    text = get_translation(text, 'en', 'fr')
    text = get_translation(text, 'fr', 'ja')
    text = get_translation(text, 'ja', 'zh-CHS')
    print(text)
    print()
