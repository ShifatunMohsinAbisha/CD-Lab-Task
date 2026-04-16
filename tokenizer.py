import re

def tokenize_sentence(sentence):
    keywords = {"is", "and", "int"} 
    tokens = re.findall(r'[a-zA-Z]+|\d+|[+=]', sentence)
    
    for token in tokens:
        if token.isdigit():
            print(f"{token} -> Literal")
        elif token in keywords:
            print(f"{token} -> Keyword")
        elif token.isalpha():
            print(f"{token} -> Identifier")
        elif token in "+=":
            print(f"{token} -> Operator")

sentence = "this is a int = 10 and a+b=20"
tokenize_sentence(sentence)