import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_lang):

    with open(text) as f:
        text = f.read()

    params = {
            'key': API_KEY,
            'text': text,
            'lang': '{}-ru'.format(to_lang)
        }
    response = requests.get(URL, params=params)
    translation = response.json()['text'][0]

    with open(f'translation {to_lang}.txt', 'w') as f:
        f.write(translation)

    return os.path.join(translation)


translate_it('ES.txt', 'es')
