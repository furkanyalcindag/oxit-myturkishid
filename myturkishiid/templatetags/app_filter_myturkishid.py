import json

from django import template

from myturkishiid.models.Language import Language
from django.conf import settings

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name='get_item_by_lang')
def get_value_by_lang(key, lang_code):
    lang = Language.objects.get(pk=lang_code)
    json_data = None

    if lang.code == 'tr':

        json_data = open(settings.BASE_DIR + '/myturkishiid/jsons/lang/tr.json', 'r',encoding='utf-8')
    elif lang.code == 'fa':
        json_data = open(settings.BASE_DIR + '/myturkishiid/jsons/lang/fa.json', 'r',encoding='utf-8')
    else:
        json_data = None
    data1 = json.load(json_data)  # deserialises it

    data2 = json.dumps(data1)  # json formatted string
    json_data.close()
    return data1[0].get(key)
