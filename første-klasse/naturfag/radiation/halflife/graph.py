from random import randint

from pylab import plot, xlabel, ylabel, grid, show

outArr = []
rowLength = 40
itemCount = rowLength ** 2
atoms = [True for i in range(itemCount)]

css = []

for i in range(10):
    outArr.append(len(atoms))
    atoms = [item for item in atoms if randint(0, 3)]

plot(range(len(outArr)), outArr)
xlabel('halflife iteration')
ylabel('Atom count')

grid()
show()
