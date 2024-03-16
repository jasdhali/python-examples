def reverse_print(str):
    nindex = len(str)-1
    while nindex >= 0:
        nletter = str[nindex]
        print( nletter)
        nindex = nindex -1

reverse_print('abc123')