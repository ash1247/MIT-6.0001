import string
shift = 12
lower_letters = string.ascii_lowercase*2
upper_letters = string.ascii_uppercase *2

punc = list(" !@#$%^&*()_+-=[]{}|\:;'\",.<>/?")
dict = {}
for i, let in enumerate(lower_letters[:26]):
    dict[let] = lower_letters[i+shift]
    print(i, let, dict[let])
for i, let in enumerate(upper_letters[:26]):
    dict[let] = upper_letters[i+shift]
    print(i, let, dict[let])
for p in punc:
    dict[p] = p
    print(p, dict[p])

print(dict)
