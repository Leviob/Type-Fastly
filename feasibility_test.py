from top_ten_5_or_longer import top_ten
print(len(top_ten))
homronyms = {}

def main():
    for word in top_ten:
        homerownly = spell_using_home_row(word)
        homronyms.setdefault(homerownly, [])
        homronyms[homerownly].append(word)
    test_feasibility()

def test_feasibility():
    duplicates = 0
    for k, v in homronyms.items():
        if len(v) > 1:
            duplicates += 1
            print(f'{k}, {v}')

    print(f'Results: {duplicates} duplicate(s) out of the top 10,000 words')
    print(f'{(1-(duplicates/10000))*100}%')

def spell_using_home_row(word): 
    home_row_letters = {'q': 'o',
                        'j': 'e',
                        'p': 'u',
                        'k': 'u',
                        'y': 'i',
                        'x': 'i',
                        'b': 'd',
                        'f': 'd',
                        'm': 'h',
                        'g': 'h',
                        'w': 't',
                        'c': 't',
                        'v': 'n',
                        'r': 'n',
                        'z': 's',
                        'l': 's',
                        }

    word_letters = list(word)
    for i in range(len(word_letters)):
        if word_letters[i] in home_row_letters:
            word_letters[i] = home_row_letters[word_letters[i]]
    home_row_spelling = ''.join(word_letters)
    return home_row_spelling

main()