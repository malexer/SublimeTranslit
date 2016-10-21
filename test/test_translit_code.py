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
