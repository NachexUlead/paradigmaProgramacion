def parse_tokens(tokens):
    def match(expected_type):
        nonlocal index
        if index < len(tokens) and tokens[index][0] == expected_type:
            index += 1
        else:
            raise SyntaxError(
                f"Expected {expected_type}, got {tokens[index] if index < len(tokens) else 'EOF'}")

    def sentence():
        noun_phrase()
        verb_phrase()
        match('DOT')

    def noun_phrase():
        match('ARTICLE')
        match('NOUN')

    def verb_phrase():
        match('VERB')
        noun_phrase()
        if index < len(tokens) and tokens[index][0] == 'PREPOSITION':
            match('PREPOSITION')
            noun_phrase()

    index = 0
    sentence()
    if index != len(tokens):
        raise SyntaxError("Unexpected tokens at the end")
