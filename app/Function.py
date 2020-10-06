def reserver(word):
    Token = {'BEGIN': 'Begin', 'END': 'End', 'FOR': 'For', 'IF': 'If', 'THEN': 'Then',
             'ELSE': 'Else', ':': 'Colon', '+': 'Plus', '*': 'Star', ',': 'Comma', '(': 'LParenthesis',
             ')': 'RParenthesis', ':=': 'Assign'}
    if word in Token:
        return Token[word]
    else:
        return 'Unknown'
