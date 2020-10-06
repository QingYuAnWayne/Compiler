def reserver(word):
    Token = {'BEGIN': 'Begin', 'END': 'End', 'FOR': 'For', 'IF': 'If', 'THEN': 'Then',
             'ELSE': 'Else', ':': 'Colon', '+': 'Plus', '*': 'Star', ',': 'Comma', '(': 'LParenthesis',
             ')': 'RParenthesis'}
    if word in Token:
        return Token[word]
    else:
        return 'Unknown'
