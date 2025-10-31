a = {1: {'a': 11}, 2: {'b': 22}}

for key in a:
    for k in a[key]:
        if a[key][k] == 11:
            print('got it')
            break