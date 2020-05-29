import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://fy.iciba.com/',
    'Origin': 'http://fy.iciba.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

params = (
    ('a', 'fy'),
)


def get_translation(f, t, w):
    data = {
        'f': f,
        't': t,
        'w': w
    }
    response = requests.post('http://fy.iciba.com/ajax.php', headers=headers, params=params, data=data)
    return response.json()['content']['out']


while True:
    w = input('\n请输入原文：\n')

    w = get_translation('zh', 'en', w)
    # print(w)

    w = get_translation('en', 'zh', w)
    # print(w)

    w = get_translation('zh', 'ja', w)
    # print(w)

    w = get_translation('ja', 'zh', w)
    print()
    print('转换结果：\n' + w)
