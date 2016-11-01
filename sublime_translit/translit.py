"""Transliteration routines."""


def build_translit_rules(mapping):
    """Build rules for transliteration.

    Rules is returned in correct order, so applying rules one by one you will
    get correct transliteration in case of mapping between multichar symbols.

    :param mapping: transliteration mapping. i.e. ``{'f': 'ef', ...}``
    :type mapping: dict

    :return: transliteration rules as a generator of items
             ``(source, target)``.
             Note: both source/target can be a multi-char string.
    :rtype: generator
    """

    mapping_lengths = reversed(list({len(k) for k in mapping}))

    for length in mapping_lengths:
        rules = ((k, v) for k, v in mapping.items() if len(k) == length)

        for rule in rules:
            yield rule

            if length > 1:
                k, v = rule

                # for case when one source upper char is represented by
                # several latin chars, all uppercase. i.e. "CH" instead of "Ch"
                if k[0].isupper():
                    yield (k.upper(), v.upper())


def translit(input_string, dictionary):
    """Transliterate input string using provided dictionary of char's mapping.

    :param input_string: source string to transliterate
    :type input_string: str, unicode
    :param dictionary: transliteration mapping. i.e. ``{'f': 'ef', ...}``
    :type dictionary: dict

    :return: transliterated string
    :rtype: unicode
    """

    for (source_char, translit_char) in build_translit_rules(dictionary):
        input_string = input_string.replace(source_char, translit_char)

    return input_string
