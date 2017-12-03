# -*- coding: utf-8 -*-

from sublime_translit import translit


class TestGeneralTranslitTest(object):

    def test_single_char_dict_translit(self):
        translit_table = dict(a='z', s='x', d='c', f='v')
        assert translit('sdaf', dictionary=translit_table) == 'xczv'

    def test_single_cyrillic_char_dict_translit(self):
        translit_table = {u'а': 'a', u'с': 's', u'д': 'd', u'ф': 'f'}
        assert translit(u'фасад', dictionary=translit_table) == 'fasad'

    def test_multi_char_dict_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }
        assert translit('Shhuka', dictionary=translit_table) == u'Щука'

    def test_multi_char_all_upper_untranslit(self):
        translit_table = {
            'Shh': u'Щ',
            'u': u'у',
            'k': u'к',
            'l': u'л',
            'a': u'а',
        }
        assert translit('SHHuka', dictionary=translit_table) == u'Щука'
