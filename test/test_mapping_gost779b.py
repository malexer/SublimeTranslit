# -*- coding: utf-8 -*-

import json

from translit import Transliterator


# Belarusian
SOURCE_BY = (
    u"У рудога вераб'я ў сховішчы пад фатэлем ляжаць нейкія гаючыя зёлкі.")
TRANSLIT_BY = (
    "U rudoha verab'ya u` sxovishchy` pad fate`lem lyazhac` nejkiya hayuchy`ya"
    " zyolki.")

# Russian
SOURCE_RU = (
    u"Широкая электрификация южных губерний даст мощный толчок "
    u"подъёму сельского хозяйства.")
TRANSLIT_RU = (
    "Shirokaya e`lektrifikaciya yuzhny`x gubernij dast moshhny`j tolchok "
    "pod``yomu sel`skogo xozyajstva.")

# Ukrainian
SOURCE_UA = (
    u"Гей, хлопці, не вспію - на ґанку ваша файна їжа знищується бурундучком.")
TRANSLIT_UA = (
    "Gej, xlopci, ne vspiyu - na g`anku vasha fajna yizha zny`shhuyet`sya"
    " burunduchkom.")


def load_mapping(filename):
    config = json.load(open(filename))
    return config['chars_mapping']


class TestGost779bTranslit(object):

    def test_belarusian_to_latin_translit(self):
        translit = Transliterator(load_mapping('gost779b_by.json'))
        assert translit.convert(SOURCE_BY) == TRANSLIT_BY

    def test_latin_to_belarusian_translit(self):
        translit = Transliterator(
            load_mapping('gost779b_by.json'), invert=True)
        assert translit.convert(TRANSLIT_BY) == SOURCE_BY

    def test_russian_to_latin_translit(self):
        translit = Transliterator(load_mapping('gost779b_ru.json'))
        assert translit.convert(SOURCE_RU) == TRANSLIT_RU

    def test_latin_to_russian_translit(self):
        translit = Transliterator(
            load_mapping('gost779b_ru.json'), invert=True)
        assert translit.convert(TRANSLIT_RU) == SOURCE_RU

    def test_ukrainian_to_latin_translit(self):
        translit = Transliterator(load_mapping('gost779b_ua.json'))
        assert translit.convert(SOURCE_UA) == TRANSLIT_UA

    def test_latin_to_ukrainian_translit(self):
        translit = Transliterator(
            load_mapping('gost779b_ua.json'), invert=True)
        assert translit.convert(TRANSLIT_UA) == SOURCE_UA
