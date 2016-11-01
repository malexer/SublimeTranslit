# -*- coding: utf-8 -*-

from unittest import TestCase

from sublime_translit import translit


class GeneralTranslitTest(TestCase):

    def test_single_char_dict_translit(self):
        translit_table = dict(a='z', s='x', d='c', f='v')

        self.assertEqual(
            translit('sdaf', dictionary=translit_table),
            'xczv',
        )

    def test_single_cyrillic_char_dict_translit(self):
        translit_table = {u'а': 'a', u'с': 's', u'д': 'd', u'ф': 'f'}

        self.assertEqual(
            translit(u'фасад', dictionary=translit_table),
            'fasad',
        )

    def test_multi_char_dict_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }

        self.assertEqual(
            translit('Shhuka', dictionary=translit_table),
            u'Щука',
        )

    def test_multi_char_all_upper_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }

        self.assertEqual(
            translit('SHHuka', dictionary=translit_table),
            u'Щука',
        )
