def do_something(a, b, c, *args, **kwargs):
    print('Funkcija')
    print(a, b, c)
    print(args, type(args))

    for arg  in args:
        print(arg)

    print(kwargs, type(kwargs))


do_something(1, 2, 3, 4, z=5 ,word=9)