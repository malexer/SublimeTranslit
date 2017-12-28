# -*- coding: utf-8 -*-

import json

from translit import Transliterator


def load_mapping(filename):
    config = json.load(open(filename))
    return config['chars_mapping']


class TestCroatianSerbianTranslit(object):

    # see official guide here: http://zakon2.rada.gov.ua/laws/show/55-2010-п
    def test_passport2010_ua_translit(self):
        translit = Transliterator(load_mapping('passport2010_ua.json'))
        assert translit.convert('Алушта Андрій') == 'Alushta Andrii'
        assert translit.convert('Борщагівка Борисенко') == 'Borshchahivka Borysenko'
        assert translit.convert('Вінниця Володимир') == 'Vinnytsia Volodymyr'
        assert translit.convert('Гадяч Богдан Згурський') == 'Hadiach Bohdan Zhurskyi'
        assert translit.convert('Ґалаґан Ґорґани') == 'Galagan Gorgany'
        assert translit.convert('Донецьк Дмитро') == 'Donetsk Dmytro'
        assert translit.convert('Рівне Олег Есмань') == 'Rivne Oleh Esman'
        assert translit.convert('Єнакієве Гаєвич Короп\'є') == 'Yenakiieve Haievych Koropie'
        assert translit.convert('Житомир Жанна Жежелів') == 'Zhytomyr Zhanna Zhezheliv'
        assert translit.convert('Закарпаття Казимирчук') == 'Zakarpattia Kazymyrchuk'
        assert translit.convert('Медвин Михайленко') == 'Medvyn Mykhailenko'
        assert translit.convert('Іванків Іващенко') == 'Ivankiv Ivashchenko'
        assert translit.convert('Їжакевич Кадиївка Мар\'їне') == 'Yizhakevych Kadyivka Marine'
        assert translit.convert('Йосипівка Стрий Олексій') == 'Yosypivka Stryi Oleksii'
        assert translit.convert('Київ Коваленко') == 'Kyiv Kovalenko'
        assert translit.convert('Лебедин Леонід') == 'Lebedyn Leonid'
        assert translit.convert('Миколаїв Маринич') == 'Mykolaiv Marynych'
        assert translit.convert('Ніжин Наталія') == 'Nizhyn Nataliia'
        assert translit.convert('Одеса Онищенко') == 'Odesa Onyshchenko'
        assert translit.convert('Полтава Петро') == 'Poltava Petro'
        assert translit.convert('Решетилівка Рибчинський') == 'Reshetylivka Rybchynskyi'
        assert translit.convert('Суми Соломія') == 'Sumy Solomiia'
        assert translit.convert('Тернопіль Троць') == 'Ternopil Trots'
        assert translit.convert('Ужгород Уляна') == 'Uzhhorod Uliana'
        assert translit.convert('Фастів Філіпчук') == 'Fastiv Filipchuk'
        assert translit.convert('Харків Христина') == 'Kharkiv Khrystyna'
        assert translit.convert('Біла Церква Стеценко') == 'Bila Tserkva Stetsenko'
        assert translit.convert('Чернівці Шевченко') == 'Chernivtsi Shevchenko'
        assert translit.convert('Шостка Кишеньки') == 'Shostka Kyshenky'
        assert translit.convert('Щербухи Гоща Гаращенко') == 'Shcherbukhy Hoshcha Harashchenko'
        assert translit.convert('Юрій Корюківка') == 'Yurii Koriukivka'
        assert translit.convert('Яготин Ярошенко Костянтин Знам\'янка Феодосія') == 'Yahotyn Yaroshenko Kostiantyn Znamianka Feodosiia'
