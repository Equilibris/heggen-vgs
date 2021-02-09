from random import randint

from pylab import plot, xlabel, ylabel, grid, show

outArr = []
rowLength = 40
itemCount = rowLength ** 2
atoms = [True for i in range(itemCount)]

html = ''.join(f'<div class="{i}"></div>' for i in range(itemCount))
makeCsstemplate = lambda index, iteration: f'.{index}{{animation: animate 0s ease {iteration}s both;}}'
css = []

for i in range(10):
    outArr.append(len(list(filter(bool, atoms))))
    atoms = [randint(0, 3) or css.append(makeCsstemplate(index, i)) if item else 0 for index, item in enumerate(atoms)]

with open('index.html', 'r') as read:
    with open('out.html', 'w') as write:
        write.write(
            read.read()
                .replace('/* STYLE */', ''.join(css))
                .replace('/* BODY */', html)
        )

# wbopen('out.html')

plot(range(len(outArr)), outArr)
xlabel('halflife iteration')
ylabel('Atom count')

grid()
show()
