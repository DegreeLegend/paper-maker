from datetime import datetime

import requests

headers = {
    'authority': 'www2.deepl.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'dnt': '1',
    'content-type': 'text/plain',
    'accept': '*/*',
    'origin': 'https://www.deepl.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.deepl.com/translator',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


def get_translation(sentence, source_lang_user_selected, target_lang, id):
    timestamp = int(datetime.now().timestamp())

    data = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":"%s","raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4,"quality":"fast"}],"lang":{"user_preferred_langs":["FR","EN","ZH"],"source_lang_user_selected":"%s","target_lang":"%s"},"priority":-1,"commonJobParams":{},"timestamp":%s},"id":%s}' % (
        sentence,
        source_lang_user_selected,
        target_lang,
        timestamp,
        id
    )

    data = data.encode('utf-8')

    response = requests.post(
        'https://www2.deepl.com/jsonrpc',
        headers=headers,
        data=data
    )
    print(response.text)

    return response.json()['result']['translations'][0]['beams'][0]['postprocessed_sentence']


if __name__ == '__main__':
    sentence = '分布式计算是一种把需要进行大量计算的工程数据分割成小块，由多台计算机分别计算，在上传运算结果后，将结果统一合并得出数据结论的科学。'

    sentence = get_translation(sentence, 'ZH', 'EN', 1)
    print(sentence)

    sentence = get_translation(sentence, 'EN', 'ZH', 2)
    print(sentence)
