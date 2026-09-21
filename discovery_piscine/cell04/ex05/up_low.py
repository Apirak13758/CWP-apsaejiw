text = str(input())
for character in text:
    if character.isupper():
        print(character.lower(), end="")
    else:
        print(character.upper(), end="")