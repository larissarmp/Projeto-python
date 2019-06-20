sent1 = ['call', 'me', 'ismael','.']
for token in sent1:
    if token.islower():
        print(token, 'is a lowercase word')
    elif token.istitle():
        print(token,'is a titlecase word')
    else:
            print(token, "is puncuantion")