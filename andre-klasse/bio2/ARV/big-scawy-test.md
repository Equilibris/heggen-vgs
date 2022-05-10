# Task 1

Dom-arv skjegg (beard): B (Big beard) b (Small beard)

Co-Dom-arv Dots: D (dot big) S (dot small)

## a

### 1

a: BbDS. Fenotypen til a blir så Små+Store prikker + langt skjegg

b: bbDS. Fenotypen til b blir så Små+Store prikker + kort skjegg

### 2

Mulige kjønceller a:

```py
import itertools
print(list(itertools.product(["B",'b'],['D','S'])))
```

`['BD' 'BS' 'bD' 'bS']`

Mulige kjønceller b:

```py
import itertools
print(list(itertools.product(["b",'b'],['D','S'])))
```

`['bD' 'bS' 'bD' 'bS']`

Man krysser dihybridt:

```py

def cross_di(mother: list, father: list):
    return [[j+i for j in mother] for i in father]


def print_table(mother: list, father: list):
    table = cross_di(mother, father)
    print('mor', *(['far']*len(father)), sep=' | ')
    print('-', *(['-']*len(father)), sep=' | ')
    print(' ', *mother, sep=' | ')
    for mom, i in zip(father, table):
        print(mom, *i, sep=' | ')


print_table(['BD','BS','bD','bS'],['bD','bS','bD','bS'])
```

| mor | far  | far  | far  | far  |
| --- | ---- | ---- | ---- | ---- |
|     | BD   | BS   | bD   | bS   |
| bD  | BDbD | BSbD | bDbD | bSbD |
| bS  | BDbS | BSbS | bDbS | bSbS |
| bD  | BDbD | BSbD | bDbD | bSbD |
| bS  | BDbS | BSbS | bDbS | bSbS |

langt skjegg små prikker: BSXS: 2/16 = 1/8

## b

Bartent med bbSS må da ha:

```
| b - b |
|       |
|       |
| S - S |
```

For at dette skal kunne skje må så b og S være koblet siden de må ligge på forskjellige lokuser på same kromosom.

Da må foreldrene ha kjønnceller som er:

```
| b
|
|
| S
```

og

```
| b
|
|
| S
```

# Task 2

Colour: Pp; pp=lys; PX=mørk

Albino: X_Aa; X_a=albino; X_A=standard

## a

Mor: PpX_AX_a,
Far: PpX_AY
barn: ppX_aY

Siden vi vet at faren har normal melationin produskjon vet vi at han kan ikke bære albino genet. Gjennom dette vet vi også at de kan bare få gutter som er albino fordi hvis de var jenter hadde faren sitt melatonin gen kommet til syne over morens sitt albino gen. Barnet må da være som skrevet over.

## b

Mor: ppX_AX_a
Far: PpX_AY

Mulige kjønnceller mor:

```py
print(list(map(lambda x:"".join([*x]),itertools.product(["p","p"],["X_A","X_a"]))))
```

`['pX_A', 'pX_a', 'pX_A', 'pX_a']`

Mulige kjønnceller far:

```py
print(list(map(lambda x:"".join([*x]),itertools.product(["p","P"],["X_A","Y"]))))
```

`['pX_A', 'pY', 'PX_A', 'PY']`

kryssnings sjema:

```py
print_table(['pX_A', 'pY', 'PX_A', 'PY'],['pX_A', 'pX_a', 'pX_A', 'pX_a'])
```

| mor  |   far    |  far   |   far    |  far   |
| :--: | :------: | :----: | :------: | :----: |
|      |   pX_A   |   pY   |   PX_A   |   PY   |
| pX_A | ppX_AX_A | ppYX_A | PpX_AX_A | PpYX_A |
| pX_a | ppX_AX_a | ppYX_a | PpX_AX_a | PpYX_a |
| pX_A | ppX_AX_A | ppYX_A | PpX_AX_A | PpYX_A |
| pX_a | ppX_AX_a | ppYX_a | PpX_AX_a | PpYX_a |

Vi filtrerer med ??YX_a. Da ender vi opp med 4 elementer, 2\*ppYX_a + 2\*PpYX_a. Da ender vi opp med 4/16 = 1/4 = 25%.

<!-- | mor  |   far    |  far   |   far    |  far   |
| :--: | :------: | :----: | :------: | :----: |
|      |   pX_A   |   pY   |   PX_A   |   PY   |
| pX_A | pX_ApX_A | pYpX_A | PX_ApX_A | PYpX_A |
| pX_a | pX_ApX_a | pYpX_a | PX_ApX_a | PYpX_a |
| pX_A | pX_ApX_A | pYpX_A | PX_ApX_A | PYpX_A |
| pX_a | pX_ApX_a | pYpX_a | PX_ApX_a | PYpX_a |

Vi filtrerer med ?Y?X_a (brukte egentlig `/^.Y.X_a$/` js regexp, `.` betyr uannsett). Da ender vi opp med 4 elementer, 2\*pYpX_a + 2\*PYpX_a. Da ender vi opp med 4/16 = 1/4 = 25%. -->
