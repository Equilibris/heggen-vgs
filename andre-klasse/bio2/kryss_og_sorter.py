def cells(a, b):
    return [a[0]+b[0], a[1]+b[0], a[0]+b[1], a[1]+b[1]]


def cross(mother_cells, father_cells):
    return [[''.join(sorted(m_cell + f_cell, key=lambda x: x.lower())) for f_cell in father_cells] for m_cell in mother_cells]


def dihaploid_complete(father, mother):
    father_cells = cells(father[:2], father[2:])
    mother_cells = cells(mother[:2], mother[2:])

    string = f'{father_cells=} from {father}\n{mother_cells=} from {mother}\n\n'

    string += '|'+'|'.join(i.center(4) for i in [''] + father_cells)+'|\n'
    string += '|'+'|'.join(':--:' for _ in [''] + father_cells)+'|\n'

    values = cross(mother_cells, father_cells)
    for ls, m in zip(values, mother_cells):
        string += '| ' + m + ' '
        for v in ls:
            string += '|' + v
        string += '|\n'

    return string

if __name__ == "__main__":
    print(dihaploid_complete("AaBB", "AAbb"))
