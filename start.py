import g4f

g4f.debug.logging = True
g4f.debug.check_version = False
print(g4f.Provider.Bing.params)

promt = input()

def ask(promt:str)->str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": promt }],
    )
    return response

print(ask(promt))

