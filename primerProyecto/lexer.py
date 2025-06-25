import re

token_specification = [
    ('ARTICLE',   r'the|a'),
    ('NOUN',      r'cat|dog|man|woman|telescope|park|boy|girl'),
    ('VERB',      r'saw|liked|walked'),
    ('PREPOSITION', r'in|with|on'),
    ('DOT',       r'\.'),
    ('SKIP',      r'[ \t]+'),
    ('MISMATCH',  r'.'),
]


tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name,
                     pattern in token_specification)


def tokenize(line):
    tokens = []
    for mo in re.finditer(tok_regex, line, re.IGNORECASE):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character: {value}')
        tokens.append((kind.upper(), value.lower()))
    return tokens
