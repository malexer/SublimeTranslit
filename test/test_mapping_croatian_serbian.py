# -*- coding: utf-8 -*-

import json

from sublime_translit import translit
from sublime_translit.util import invert_dict


TEXT_RS = u"Ајшо, лепото и чежњо, за љубав срца мога дођи у Хаџиће на кафу."
TEXT_HR = u"Ajšo, lepoto i čežnjo, za ljubav srca moga dođi u Hadžiće na kafu."


def load_mapping(filename):
    config = json.load(open(filename))
    return config['chars_mapping']


class TestCroatianSerbianTranslit(object):

    def test_croatian_to_serbian_translit(self):
        translit_table = load_mapping('croatian_serbian.json')
        assert translit(TEXT_HR, dictionary=translit_table) == TEXT_RS

    def test_serbian_to_croatian_translit(self):
        translit_table = invert_dict(load_mapping('croatian_serbian.json'))
        assert translit(TEXT_RS, dictionary=translit_table) == TEXT_HR
