
def show_arguments(naam, *args, flag, **kwargs):
    print('In function "show_arguments"')
    print(f'naam: {naam}')
    print(args)
    print(f'flag: {flag}')
    print(kwargs)


if __name__ == '__main__':
    # args = [1290837, 'xyz', False]
    # kwargs = {'a': 4, 'b': 6}
    #
    # show_arguments('Peter', *args, balloon=23, flag='red', **kwargs)
    #
    # f = show_arguments
    #
    # f('Peter', *args, balloon=23, flag='red', **kwargs)

    namen = ['Arthur', 'nick', 'Bart', 'Noa', 'Cariña']

    def reverse_string(s):
        return s[::-1]

    lambda s: s[::-1]

    namen.sort(key=lambda s: s[::-1])

    for i, naam in enumerate(namen, start=1):
        print(i, naam)

    print( list(filter(lambda s: 'a' in s.lower(), namen)) )

    print( list(map(lambda s: 'a' in s.lower(), namen)) )
    print( list(map(lambda s: len(s), namen)) )
