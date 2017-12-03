class Transliterator(object):

    def __init__(self, mapping, invert=False):
        self.mapping = [
            (v, k) if invert else (k, v)
            for k, v in mapping.items()
        ]

        self._rules = sorted(
            self.mapping,
            key=lambda item: len(item[0]),
            reverse=True,
        )

    @property
    def rules(self):
        for r in self._rules:
            k, v = r
            if len(k) == 0:
                continue  # for case when char is removed and mapping inverted

            yield r

            # Handle the case when one source upper char is represented by
            # several latin chars, all uppercase. i.e. "CH" instead of "Ch"
            if len(k) > 1 and k[0].isupper():
                yield (k.upper(), v.upper())

    def convert(self, input_string):
        """Transliterate input string."""
        for (source_char, translit_char) in self.rules:
            input_string = input_string.replace(source_char, translit_char)

        return input_string
