import sublime
import sublime_plugin

from .translit import Transliterator


class TransliterateSelectionCommand(sublime_plugin.TextCommand):

    def run(self, edit, dictionary_file, invert_mapping=True):
        """Run Sublime Text command for transliteration.

        :param edit: edit object
        :type edit: sublime.Edit
        :param dictionary_file: transliteration mapping filename (without
                                path!). It is expected to be in JSON format.
        :type dictionary_file: str
        """

        mapping_config = sublime.load_settings(dictionary_file)

        translit = Transliterator(
            mapping=mapping_config.get('chars_mapping'),
            invert=invert_mapping,
        )

        selections = self.view.sel()

        for sel in selections:
            selection_text = self.view.substr(sel)
            self.view.replace(
                edit,
                sel,
                translit.convert(selection_text)
            )
