def translit(input_string, dictionary):
    translit_string = []
    for char in input_string:
        translit_string.append(dictionary.get(char, char))
    return ''.join(translit_string)
