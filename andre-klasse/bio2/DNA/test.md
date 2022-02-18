# Oppgave 15, Replikasjon

DNA replikasjonen er delt inn i flere forkjellige enzymer som er designet for å klare spesefikke oppgaver. Disse enzymene er:

1. Helikase
2. Primase
3. DNA-syntase
4. ligase

## Heilkase

Heilkase har rollen av å spalte de antiparallele strengene i bobler som kalles replikasjons bobler, på starten ( og slutten ) av disse boblene skapes da replikasjons gafler, dette er hvor primase binner seg for lagtråden.

Disse to trådene er ikke skapt likt, det er en ledertråd (leading strand) og en lagtråd (lagging strand). Lagtråden er da tråden som spaltes der den 3' ennen er i replikasjons gaffelen. Letertråden har da den 5' enden i replikasjons gaffelen (påvirkningen av dette diskuteres i seksjon 1.3)

## Primase

Primase har rollen av å lage det som kalles RNA-primere. Primase beveger seg i 3'-5' rettning mens den setter på de komplementære basene i 5'-3' rettning. Dette gjøres bare for et par baser sånn at DNA-syntase har et grunnlag for å binde seg til templat-tråden.

## DNA-syntase

DAN-Syntase har rollen av å feste på komplementære baser litt som primase, men DNA-syntase lager DNA og ikke RNA; DNA-syntase bruker ikke ribose heller deoxyribose. Dette [som primase] beveger seg i 3'-5' rettning men syntiserer i 5'-3' retning.

Denne fartsrettningen bringer oss så tilbake til forskjellene på led- og lagtrådenene nevnt i 1.1.

```
                      /-------------------------------------------- 3'
                     /  | | | | | | | | | | | | | | | | | | | | | |      Leading strand
                    /   3' -------------------------------- <Primer
5' ----------------/                                      <-- DNA-S
   | | | | | | | |   <-- H  DNA-S -->           DNA-S -->
3' ----------------\    Okazaki fragment    Okazaki fragment
                    \   Primer> ----------- Primer> ---------------
                     \  | | | | | | | | | | | | | | | | | | | | | |      Lagging strand
                      \-------------------------------------------- 5'
```

_Figur 1, dannelsen av okazaki fragmenter på lagtråden_

Som du kan se i figur 1 så dannes såkalte okhazaki fragmenter på lagging stranden, dette er da fragmenter som ettersom at DNA-Syntase og Primase leser imot fartsrettinga så må det lages flere primere og ettersom det må så hvert Okhazakifragment ha en primer og jobbes på induviduelt.

## Ligase

Ligase exsisterer for å erstatte primere og lime sammen alle okhazaki fragmentene. Dette gjøres av å fjerne RNAet og erstatte det med DNA. Den gjør dette av å erstate ribosen i RNA primerene med dexoyribose men sørge for at besene fortsatt er satt sammen komplementært.

## Mer

Enzymene utfører oppgavene sine i avlistet rekkefølge.

Denne prossesen er også semikonservativ, alså DNA et dattercellene motar er 50% det gamle 'fra' morcellen mens 50% er syntert nytt.

# Oppgave 16, Celledeling

## Begreps forklaring

### Overkryssing

Overkryssing er bytte av DNA fra to like egenskaper en fra hvert av søsterkromanioidene. Dette øker genetisk variasjon.

## Tabel

|         Attribute | Mitose                     | Meiose                                   |
| ----------------: | -------------------------- | ---------------------------------------- |
|        Startpunkt | Diploid Morcelle           | Diploid Morcelle                         |
|          Resultat | 2 x Diploid Morcelle       | 4 x Haploid dattercelle                  |
|   DNA-Replikasjon | Ja i morcellen             | Ja i den originale morcellen             |
|      Overkrysning | Nei                        | Ja, Profase 1                            |
| Koromosonets gang | 46 &rarr; 96 &rarr; 2 x 46 | 46 &rarr; 96 &rarr; 2 x 46 &rarr; 4 x 23 |

## Faser i celledeling

### Mitose

- Profase
- Prometafase
- Metafase
- Anafase
- Cytokinesen

### Meiose

- Profase 1
- Prometafase 1
- Metafase 1
- Anafase 1
- Cytokinesen 1

* Profase 2
* Prometafase 2
* Metafase 2
* Anafase 2
* Cytokinesen 2

# Oppgave 17, Proteinsyntese

## Translasjon

mRNA går ut av nukleus og inn i et ribosom. Der binner 30s seg til AUG kodonet, etter dette komemr så tRNA for Metionin. Dette binner seg så til 30s og mRNAet, så kommer 50s og binner seg til dette og danner enzymkomplexet 70s. 70s har da 3 seter, disse er spalte setet, binne setet og akseptor setet. Nå er det et tRNA i akseptorsetet, så kommer det tRNAet og binder seg til akseptor setet, dette tRNAet sitt aminosyre binnes så til metionin og 70s skyver alle sete ett hakk til venstre og spalter Met tRNAet men binner dette til den neste aminosyren, så kommer det flere aminosyrer etter hverandre til man treffer eet stop kodon. Dette stop konoden 'tommer' setene til 70s og leder så til at den spaltes opp til 30s og 50s igjen for prosessen å gjenta nå med en polypeptid kjede.

Prosessen kan visualiseres følgende

```
Bilde 1:
mRNA    AUG GCA UCA Sto

30s 50s

Bilde 2:
mRNA    AUG GCA UCA Sto
       [30s]

50s

Bilde 3:

        t-
        Met
mRNA    AUG GCA UCA Sto
       [30s]

50s

Bilde 4:
        t-
        Met
mRNA    AUG GCA UCA Sto
       [30s]
       [50s]


Bilde 4:
        t-
        Met
mRNA    AUG GCA UCA Sto
       [70s]

Bilde 5:
mRNA    [   ] [AUG] [GCA]  UCA Sto
70s      POP   CUR   NXT
               Met.

Bilde 6:
mRNA    [AUG] [GCA] [UCA]  Sto
70s      POP   CUR   NXT
               Met.
               Ala.


Bilde 7:
mRNA    [GCA] [UCA] [Sto]
70s      POP   CUR   NXT
               Met.
               Ala.
               Ser.


Bilde 7:
mRNA    [UCA] [Sto] [   ]
70s      POP   CUR   NXT
               Met.
               Ala.
               Ser.
               ....

Bilde 8.

30s + 50s + polypeptide [ Met. Ala. Ser. ]
```

_Figur 2, en eksemelutføring av translasjonen på mRNAet [AUG GCA UCA]_

## Transkripsjon [EXTRA]

Først Kobler en generell transkripsjons faktor til DNAet, etter dette kan RNA-Syntase 1 spalte opp nøyaktig et gen. Dette er signalisert med en promotor,
