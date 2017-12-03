# -*- coding: utf-8 -*-

from translit import Transliterator


class TestGeneralTranslitTest(object):

    def test_single_char_dict_translit(self):
        translit_table = dict(a='z', s='x', d='c', f='v')
        assert Transliterator(translit_table).convert('sdaf') == 'xczv'

    def test_single_cyrillic_char_dict_translit(self):
        translit_table = {u'а': 'a', u'с': 's', u'д': 'd', u'ф': 'f'}
        assert Transliterator(translit_table).convert(u'фасад') == 'fasad'

    def test_multi_char_dict_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }
        assert Transliterator(translit_table).convert('Shhuka') == u'Щука'

    def test_multi_char_all_upper_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }
        assert Transliterator(translit_table).convert('SHHuka') == u'Щука'
