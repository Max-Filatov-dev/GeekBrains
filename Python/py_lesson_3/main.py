def first(word: str):
    """ """
    alphabets = {'rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'eng': 'abcdefghijklmnopqrstuvwxyz'}
    eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
    rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
    language = [l for i in word for l, v in alphabets.items() if i in v][0]

    if language == 'rus':
        return language, sum([r for i in word for r, v in rus.items() if i.upper() in v])
    elif language == 'eng':
        return language, sum([e for i in word for e, v in eng.items() if i.upper() in v])


def main():
    """ """
    while True:
        word = input('\nВведите слово: ')
        if any(ch.isdigit() for ch in word):
            print('Ввести нужно слово!')
        else:
            return print(first(word=word))


if __name__ == '__main__':
    main()