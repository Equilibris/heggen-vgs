
def cross_di(mother: list, father: list):
    return [[j+i for j in mother] for i in father]


def print_table(mother: list, father: list):
    table = cross_di(mother, father)
    print('mor', *(['far']*len(father)), sep=' | ')
    print('-', *(['-']*len(father)), sep=' | ')
    print(' ', *father, sep=' | ')
    for mom, i in zip(mother, table):
        print(mom, *i, sep=' | ')


'''
Lys markering: L
Brun markering: B

Klør: K/k

Valp: BB|kk
Far : BL|Kk -> BK Bk LK Lk
Mor : BL|Kk -> BK Bk LK Lk

    BK   Bk   LK   Lk
BK  BBKK BBKk BLKK BLKk
Bk  BBKk BBkk BLKk BLkk
LK  BLKK BLKk LLKK LLKk
Lk  BLKk BLkk LLKk LLkk



'''
