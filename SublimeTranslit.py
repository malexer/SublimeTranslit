import sublime
import sublime_plugin

from .sublime_translit import translit
from .sublime_translit.util import invert_dict


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
        # translit mapping file has latin as a keys
        # and target language as values
        mapping = mapping_config.get('chars_mapping')

        if invert_mapping:
            mapping = invert_dict(mapping)

        selections = self.view.sel()

        for sel in selections:
            selection_text = self.view.substr(sel)
            self.view.replace(
                edit,
                sel,
                translit(selection_text, mapping)
            )
