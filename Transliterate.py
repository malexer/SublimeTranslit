import sublime
import sublime_plugin

import sys
ST2 = sys.version_info < (3, 3)

class TransliterateCommand(sublime_plugin.TextCommand):
    def run(self, edit, dictionary_file):
        s = sublime.load_settings(dictionary_file)
        dictionary = s.get('chars_mapping')

        # invert dict
        # reason: it was a problem loading dict with unicode keys in sublime
        dictionary = dict([[v, k] for k, v in dictionary.items()])

        selections = self.view.sel()

        for sel in selections:
            selection_text = self.view.substr(sel)
            self.view.replace(edit, sel, translit(selection_text, dictionary))

def translit(input_string, dictionary):
    translit_string = []
    for char in input_string:
        translit_string.append(dictionary.get(char, char))
    return ''.join(translit_string)
