def singulars_and_plurals(words):
    """Sort names and separate singular and plural.

    :param list words: list of words
    :rtype: dict
    :return: dict with separate words.
    """
    result = {
        'singulars': [],
        'plurals': []
    }

    for word in words:
        if word[-1] == 's':
            result['plurals'].append(word)
        else:
            result['singulars'].append(word)
    return result


if __name__ == '__main__':
    input_data = ["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"]
    print(singulars_and_plurals(input_data))