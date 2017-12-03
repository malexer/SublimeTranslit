# -*- coding: utf-8 -*-

import json

from translit import Transliterator


TEXT_RS = u"Ајшо, лепото и чежњо, за љубав срца мога дођи у Хаџиће на кафу."
TEXT_HR = u"Ajšo, lepoto i čežnjo, za ljubav srca moga dođi u Hadžiće na kafu."


def load_mapping(filename):
    config = json.load(open(filename))
    return config['chars_mapping']


class TestCroatianSerbianTranslit(object):

    def test_croatian_to_serbian_translit(self):
        translit = Transliterator(load_mapping('croatian_serbian.json'))
        assert translit.convert(TEXT_HR) == TEXT_RS

    def test_serbian_to_croatian_translit(self):
        translit = Transliterator(
            load_mapping('croatian_serbian.json'), invert=True)
        assert translit.convert(TEXT_RS) == TEXT_HR
