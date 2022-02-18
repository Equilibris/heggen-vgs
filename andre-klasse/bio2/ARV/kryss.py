def kryss(female, male):
    print(f'  {male[0]}    {male[1]} m')
    print(female[0], f'{min(female[0],male[0])}/{female[0]}{male[0]}',
          f'{min(female[0],male[1])}/{female[0]}{male[1]}')
    print(female[1], f'{min(female[1],male[0])}/{female[1]}{male[0]}',
          f'{min(female[1],male[1])}/{female[1]}{male[1]}')
    print('fm')


def pb(*args):
    import functools
    import itertools
    return [functools.reduce(lambda a, b: a + b, i) for i in itertools.product(*args)]
