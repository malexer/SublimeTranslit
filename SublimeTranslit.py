import sublime
import sublime_plugin

from .sublime_translit import translit
from .sublime_translit.util import invert_dict


class TransliterateSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, dictionary_file):
        s = sublime.load_settings(dictionary_file)
        dictionary = s.get('chars_mapping')

        # invert dict
        # reason: it was a problem loading dict with unicode keys in sublime
        dictionary = invert_dict(dictionary)

        selections = self.view.sel()

        for sel in selections:
            selection_text = self.view.substr(sel)
            self.view.replace(edit, sel, translit(selection_text, dictionary))
