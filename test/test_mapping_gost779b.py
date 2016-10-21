# -*- coding: utf-8 -*-

import json
from unittest import TestCase

from sublime_translit import translit
from sublime_translit.util import invert_dict


# Belarusian
SOURCE_BE = (
    u"У рудога вераб'я ў сховішчы пад фатэлем ляжаць нейкія гаючыя зёлкі.")
TRANSLIT_BE = (
    "U rudoga verab'ya u` sxovishchy` pad fate`lem lyazhac` nejkiya gayuchy`ya"
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
    return invert_dict(config['chars_mapping'])


class Gost779bTranslitTest(TestCase):

    def test_belarusian_translit(self):
        translit_table = load_mapping('gost779b_rus.dict')
        self.assertEqual(
            translit(SOURCE_BE, dictionary=translit_table),
            TRANSLIT_BE,
        )

    def test_russian_translit(self):
        translit_table = load_mapping('gost779b_rus.dict')
        self.assertEqual(
            translit(SOURCE_RU, dictionary=translit_table),
            TRANSLIT_RU,
        )

    def test_ukrainian_translit(self):
        translit_table = load_mapping('gost779b_ukr.dict')
        self.assertEqual(
            translit(SOURCE_UA, dictionary=translit_table),
            TRANSLIT_UA,
        )
