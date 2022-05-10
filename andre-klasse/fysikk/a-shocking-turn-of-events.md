# Values

$$e = -1.60*10^{-19}C$$

Proton: $e$, electron: $-e$

Unit columb.

# Strøm

I: Strøm, Q: Ladning, t: Time.
$$I=\frac Qt$$

**It can always get worse** / electrons flow from - to plus.
$$Q = -1C$$
Unit: Ampere (A)

# Spenning

Recall
$$F_e = \frac Ws$$
Spenning:
$$U = \frac WQ$$
Unit: Volt (V)
$$Volt = \frac {Joule} {Columb}$$

# $UI=P$

EFFECT, WATT

# Resistans

Resistanslikningen

Unit Ohm $\Omega$

$$R = \frac UI$$
/
Alle elektriske komponenter har en resistans som man kan regne ut ved å bruke $R=\frac UI$

Resistence increases as temperature increases. This leads to resistnce being approximated to an exponential function.

$$R = \rho \frac lA$$

## example

```
+-----------| #----------+
|                        |
|                        |
+-----------(X)----------+
```

$$R_i = \frac UI = \frac {5V}{2A} = 2.5\Omega$$

# Example

```
+--<--<--<--+--<--<--+
|                    |
|                    A
|      +----V----+   |
|      |         |   |
+-->-->+-->R_1-->+-->+
|                    |
|      +----V----+   |
|      |         |   |
+-->-->+-->R_2-->+-->+
```

# Circits

## Seire

```
+--<--<--<--+ |---<--<--<--<--<--<-<-+
|                                    |
|                                    |
|      +----V----+   +----V----+     | 0.5A
|      | 2Ohm    |   |  4Ohm   |     |
+-->-->+-->R_1-->+-->+-->R_2-->+-----+
```

Total resistans
$$R_{tot} = R_1 + R_2$$

Total spenning
$$U_P = U_1 + U_2$$

### Regne ut strømmen

$$U_P = R_{tot}I$$
$$I = \frac {U_P}{R_{tot}}$$

$$\frac {3V}{6\Omega} = 0.5A$$

### Regner ut spenning over $R_1$ og $R_2$

$$U_I = R_II$$
$$U_1 = 2.0\Omega 0.5A = 1V$$
$$U_2 = 4.0\Omega 0.5A = 2V$$

## Parallel

```
+--<--<--+ |---<--<--+
|                    |
|  I_2               |
+-->-->+-->R_1-->+-->+
|                    |
|                    |
|  I_1               |
+-->-->+-->R_2-->+-->+
```

### Strøm i paralell kobliner

Kirchoffs 1.

$$I = I_1 + I_2$$

### Spenning over paralell kobliner

$$U_P = U_1 = U_2$$

### Regn ut $I_1$

$$U=RI$$
$$\frac{U_1}{R_1}=I_1$$
$$\frac {3.0V} {1.0\Omega} = 3.0A$$

## Regn ut $I_2$

$$U=RI$$
$$\frac{U_2}{R_2}=I_2$$
$$\frac {3.0V} {1.0\Omega} = 3.0A$$

## total resistens i en parallelkobling

# Det totale spennings fallet blir altid samme som batteri spenningen

# 10.1

## a

$$x~e=0.1C \iff x = \frac {0.1C}e$$

# 10.3

## a

$$W=QU=5V * 8~10^3C = 5\frac JC * 8~10^3C = 5 * 8 * 10^3J = 4 * 10^4J$$

## b

$$4 * 10^4 / 3600 kWh$$

## c

$$\frac{8000C}{1.6*10^{-19}}$$

# 10.4

## a

$$R = \frac{13V}{0.59A}=22.033\Omega$$

## b

$$R=\frac U I \iff I = \frac U R$$

# 10.59

## a

$$U = 30 / 300 = 0.1A$$

$$U * 120\Omega = 12V$$

## b

$$\frac 1{\frac 1{120}+\frac 1{50}}+180 = \frac{3660}{17}$$

$$U = \frac{17 * 30}{3660} = \frac{17}{122}$$

$$180\Omega * \frac{17}{122}A = \frac{1530}{61}$$

$$30 - \$LAST= \frac{300} {61}$$

# 10.60

## a

1 := E
2 := C

## b

1 := C
2 := E

# 10.61

## b

$$R_1 + R_2 + \Big(\frac 1 {R_3} + \frac 1 {R_4} \Big)^{-1}$$

$$a,b>0 \implies a + b > a , b$$
$$a,b>0 \implies \frac1{\frac1{a}+ \frac1{b}} <a,b$$

# 10.62

## a

D

## b

b,c

# 10.34

# Example

$$R = \frac 1 {\frac 1 {R_1} + \frac 1 {R_2}} + R_3 = \frac {95} 3$$
$$I = \frac UR = \frac{10 V} {\frac {95} 3\Omega} = \frac 6 {19} A$$
$$U_3 = RI = 25\Omega * \frac 6 {19}A = $$
$$U_1 = U_2 = 10V - U_3 = 2V$$
$$I_1 = \frac {U_1} {R_1}$$

# 10.30

$$U = RI$$
$$R = \frac U I = \frac {-}{.}$$

# 10.33

U: V
I: A

$$U = RI$$
$$I = \frac UR = \frac {10V}{1000 + k}$$

$$U_V = R_1I=1000\Omega I$$

```py
from fractions import Fraction

entries = [500, 200, 0]
for k in entries:
	I = Fraction(10,1000+k)
	print(f'U_V={1000*I}V I={I}A')
```

# TODO: `[10.28, 10.68]`
