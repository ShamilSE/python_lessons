def spin_words(sentence):
    string = ''
    i = 0
    while len(sentence) > i:
        start = i
        smbs = 0
        while sentence[i] != ' ' and i + 1 < len(sentence):
            if i + 2 > len(sentence):
                i += 1
                smbs += 1
            smbs += 1
            i += 1
        else:
            if string != '':
                string += ' '
            if smbs >= 5:
                if i + 2 > len(sentence):
                    j = i
                else:
                    j = i - 1
                while j >= start:
                    string += sentence[j]
                    j -= 1
            else:
                if i + 2 > len(sentence):
                    i += 1
                while start < i:
                    string += sentence[start]
                    start += 1
        i += 1
    return string
