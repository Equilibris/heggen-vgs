# Task 1

## a

Gener koder til proteiner; proeiner så utfører egenskapen. Hvis strukturen på et protein endres endres så funksjonen på det proteinet. Dermed kan det tenkes at jo nermere proteinet er dens opprinelige variant jo likere egenskap koder det muterte genet for.

<!-- TODO: EXEMPEL -->

```
[ORIGINAL]     FAR TAR SIN BLÅ BÅT MED ROR
[SUBSTITUSJON] FAR TAR DIN bLÅ BÅT MED ROR
[INSESJON]     FAR TAR hDI NBL ÅBÅ TME DRO R
```

Proteiner er bygd opp av aminosyrer. Kodoner koder til aminosyrer. Kodoner er bygd opp av 3 baser, eksempelet over viser hvordan forskjelige endringer i baserekkefølgen kan lede til større eller mindre endringer i slutt proteinet.

Derfra følger det at du kan ha en substisusjon som lager en mindre endring (og medfølgene mildtere sykdoms utslag). Eller en insesjon / delesjon som kommer til å lede til en mye mer dramatisk endring.

## b

I en gelelektroforese så skilles DNA fragmenter etter størrelse. Dette betyr så at hvis det er en tjukk linje på en strekning er det mye DNA der enn hvis det hadde vert en tynn linje.

Vi vet også at person 7 & 13 er syk. Dette kan tyde til at det syke allelet har rundt 1/3 så mange baser som det friske genet. Vi kan også se at når en person er syk har de mye tynnere linjer enn en frisk person. Dette er da grunnet det vi snakket om i §1.

Gjennom dette kan vi også anslå at person 14 har gentypen homozygote reciciv (`tt`) og dermed en frisk fenotype

## c

<details>
<summary>
Gelelektroforesen viser at det syke genet går kortere. Dette betyr det kan godt være en delesjon.
</summary>

> Det er 2 typer delesjon som kan fårekomme her:
>
> - Punkt delesjon; fjerning av en base
> - Cromosone deletion; fjerning av en sammenhengende sekvens av baser
>
> Det kan ikke vere punktmutasjon. Hvis en i 10 folk får én punktmutasjon, da er det en i 100 som får 2 punkt mutasjoner osv. Gjennom dette er det extremt få folk som får en punktmessig delesjon av 4 Megabaser (4 000 000 baser). Det er mulig men det har en sannsynlighet av 0.
>
> En kromoson mutasjon derimot er en enkel delesjon av en contiguous rekke av baser. Dette betyr da at man kan enkelt fjærne 4 Megabaser vert av informasjon. Derfor er det fult sannsynlig at det er en _kromosn_ delesjon.

</details>

## d

Vi begynner med å sette opp opplysninge vi vet.

9 mor: ttEe

mulige kjønnsceller: [te, te, tE, tE]

Vi vet også de følgenge faktaene om faren:

- han kan ikke være homozygot `EE` siden han får barn som er syk
- han kan ikke være homozygot `TT` siden han får barn som er frisk
- han kan ikke ha mer enn èn sykdom ettersom han får barn som er frisk

Dette etterlater så to genotyper, `Ttee` og `ttEe`.
Vi kan så redusere dette enda mer av å notere oss at utspatlings forholdet hadde vert feil hvis det var 2 instanser av `T` genvarianten. Da får vi:

far: Ttee

mulige kjønnsceller: [Te, Te, te, te]

| ♂,♀ | te   | te   | tE   | tE   |
| --- | ---- | ---- | ---- | ---- |
| Te  | Ttee | Ttee | TtEe | TtEe |
| Te  | Ttee | Ttee | TtEe | TtEe |
| te  | ttee | ttee | ttEe | ttEe |
| te  | ttee | ttee | ttEe | ttEe |

Som vi kan se er det mange duplikater i kryssling skjemaet. Fordi alle antallet duplikater er delelig me 2 kan vi forenkle dette kryssnings sjema.

| ♂,♀ | te   | tE   |
| --- | ---- | ---- |
| Te  | Ttee | TtEe |
| te  | ttee | ttEe |

Da kan vi se vi får 4 barn med unike fenotyper som alle er like sannsynlig å fårekomme. Dette betyr faren må ha genotypen `Ttee`

## e

Amishfolket var et lite subset av en folkegruppe som så utvandret til et annet 'økosystem'. Dette er da et eksempel på grunnlegger effekten. Grunnlegger effekten er da utbrett i dette tilfellet fordi det er veldig lite genflyt gjennom hvor mye innavel det er i amishfolket.

## f

I denne oppgaven kan vi utnytte Hardey-weinberg likevekt.

<!-- $$
\large {
q^2 = \frac 1 {200} \implies
q = \sqrt \frac 1 {200} \implies
p = 1 - q = 1 - \sqrt \frac 1 {200}
}
$$ -->

<div align="center"><img style="background: white; padding: 1em;" src="https://render.githubusercontent.com/render/math?math=%5Clarge%20%7B%0Aq%5E2%20%3D%20%5Cfrac%201%20%7B200%7D%20%5Cimplies%0Aq%20%3D%20%5Csqrt%20%5Cfrac%201%20%7B200%7D%20%5Cimplies%0Ap%20%3D%201%20-%20q%20%3D%201%20-%20%5Csqrt%20%5Cfrac%201%20%7B200%7D%0A%7D"></div>

Vi søker `2pq` siden dette er delen av likevekten som representerer hetrozygote individer's sannsynlighet.

<!-- $$
2pq = 2 \sqrt \frac 1 {200} \Big(1-\sqrt \frac 1 {200}\Big)
\approx 0.1314213562373 \approx 13.14\%
$$ -->

<div align="center"><img style="background: white; padding: 1em;" src="https://render.githubusercontent.com/render/math?math=2pq%20%3D%202%20%5Csqrt%20%5Cfrac%201%20%7B200%7D%20%5CBig(1-%5Csqrt%20%5Cfrac%201%20%7B200%7D%5CBig)%20%0A%5Capprox%200.1314213562373%20%5Capprox%2013.14%5C%25"></div>

# 2

## a

For å forstå dette er det et par konsepter vi må forstå:

- Trofisk-effektivitet
- Bioakumilering

### Trofisk-effektivitet

Trofisk effektivitet er et tall som er hvor mye energi som tapes fra gjennom trofisk nivåene. For exempel kan det 'koste' 10kg mus for å produsere 1kg ugle. Dette er da fordi mye energi er tapt gjennom for eksempel å holde musen i live før den oppnår en spiselig tilstand. Dette kan for elsempel tapes gjennom varme eller lignende.

Dette ligger på snitt rundt 10% energi overført.

### Bioakumelering

Bioakumilering følger så som konsikvens av trofisk-effektiviteten. Bioakumilering er rett og slett at fordi en art med høyere trofisk nivå må den spise biomasse lik invertsen av trofisk effektiviteten. Dette kan best ilustreses med et exempel.

En mus er 1. konsument. Den spiser planter som inneholder spor av DDT. Dette gir da musen en konsentrasjon av DDT på for eksempel 9&permil; (9g/1kg). Hvis bare 10% av energien overføres da trenger en ugle på 1 kilo å spise 10kg av mus. Dette betyr da at ugla for en DDT konsentrasjon på 90&permil;

### Annvendelse

Nå som vi forstår hva disse begrepene kan vi ta for oss dem i denne sammenhengen. Vi ser at hvithodehavørnen og fiskeørnen er 3. konsumenter som etter våre tidligere utregninger setter dem sirka 10\* så høyt som Børnpelikan.

En annen faktor som må noteres er de varierende vektene på artene, dette blir da å pårivke hvordan massene deres sinn variasjon kan endre hvor stort utslag bioakumilering har effekt.

<!-- $$\frac{16000n}{\frac {5.6kg+4.1kg} 2} \approx 3299 \frac 1 {kg} $$
$$\frac{10000n}{\frac {1.6kg+1.4kg} 2} \approx 6666 \frac 1 {kg} $$
$$\frac{3000n} {\frac {3.2kg+3.7kg} 2} \approx 869 \frac 1 {kg}$$

Opphoping av miljøgjifter bioakumilering

Trofisk nivå

Trofisk -->

## b

Vi kan angripe disse punktene en etter en.

## Kongeørn innvandrer og danner en populasjon

En mulig begrunnelse bak dette er at kongeørn kan spise griseungene. Gris har også en temporaly independant fødsels-syklus. Dette betyr da griseunger er en non-intermittent resurs.

## Flekket stinkdyr thrives

Disse er da natt-aktiv med kun en naturlig predator. Detta e da kongeørnen. Nå som kongeørna er preoccupied med å spise tamgris om dagen er det et lavere selektrivt press på dem som da leder til at deres populasjon økes.

## Øyrev populasjonen reduseres kraftig

Øyrev deler mange nisjer med stinkdyr. Forskjellen mellom dissa to e da at øyreven e aktiv mens kongeørna e aktiv nokak som da lede til at de blir et prime target førr kongeørna. De dele også flere nisjer med flekket stinkdyr (note omnivority xor fruit and berrries). Disse nisjene blir da brukt opp om natten noe som lede til at de ikke får nokk mat om dagen. (og ofc blir de spist også) (interspesefik konkuranse)

<!--
HUSK GRISUNGER ER IKKE LIKE SMÅ SOM FAKTISE GRISER

PIG BIRTH IS NOT TEMPORALY DEPENDANT

Sporatisk ørn angrep reduseres

Utkonkurerer øyrev i den nischen

Interspesefik konkurasse

Ørnebestand
-->

## c

Vi begynner med å navngi mellom-artene gjennom faktumet at det ikke gjer mening å gi dem et 'gjennomsnitt navn'. Detta lar oss også si hva som kom først 'høna eller egget'

Dannelse rekkefølge er implisit bottom to top.

```mermaid
flowchart BT
  &alpha; --> &beta;
  &beta; --> Grårev
  &beta; --> &gamma;
  &gamma; --> Sørrev
  &gamma; --> Nordrev
```

Vi har navngitt elementene på følgende vis førr å kunne forklare hva hypotesene _egentlig_ sier.

Dette er gjort fordi vi får tilgang til en funksjon av to elementer, `ancestor(X, Y)`

### Hvorfor hypotese 2 er feil

<!-- Hypotese 2 er mest sannsynlig feil fordi den tilsir at Nordreven må ha blitt dannet av en migrasjon av &gamma; til en av de nordere øyene. Dette gjer ikke mening gjennom hvor mye reise som må gjøres da -->

<!-- Hypotese 2 er feil ettersom den ikke legger til rette for &gamma; å dannes. Det går serfølgelig fortsatt ann, men det har en sannsynlighet på 0. -->

<!-- **Hypotese 1**: `ancestor(Grårev) -->

<!-- Grunnlegger effekten -->

## d

ingen genflyt + flaskehals effekten

recesivitet og hvor mye vi bær på rn

## e

grunnlegger effekten og dens andregrads power

## f

Muldyr og shabby spurv

Divergent evolusjon

Disruptiv seleksjon

Alopartisk artsdannelse in progress

Darwin og galapagos https://en.wikipedia.org/wiki/Divergent_evolution

Kan inneholde flere skadelige gener enn gynstige gener

Sterilt / ikke levedyktig

# 3

## a

Områder med høy akkumelasjon

Områder som akumelerer mutasjoner over tid

Ikke kodende områder som for eksempel introner.

## b

Det er enklest å forstå denne oppgaven av å tegne et diagram.

|      | Barn | Mor  | &alpha; | &beta; |
| ---: | :--: | :--: | :-----: | :----: |
| 10Mb |      |      |         |        |
|  9Mb | ———— | ———— |  ————   |  ————  |
|  7Mb |      |      |         |        |
|  6Mb |      |      |         |        |
|  5Mb | ———— |      |  ————   |  ————  |
|  4Mb | ———— | ———— |  ————   |        |
|  3Mb |      |      |         |        |
|  2Mb |      |      |         |        |
|  1Mb | ———— |      |         |  ————  |

Av å studere dette diagramme kan vi se at &beta; må være faren. Dette er da grunnet at &alpha; ikke har 1Mb DNA fragmentet. Hvis vi ikke hadde moren sine gelelektroforese resultater hadde dette vert tvetydig. Dette er da siden begge to har 3/4 av moren av barnet sitt DNA og vi mangler informasjonen av at 4Mb kommer fra moren.

## c

Har desverre ikke tid til dette før innlevering. Ferdig resultat skal fremstilles før torsdag 19.

## d

Hvis 2 gener er koblet så vil det si at arver du den ene genvarianten fra en forelder arver du også en annen. Dette kan synes på diagramet under:

```
b    aa    a a    aa aa    a a a a
|    ||    | |    || ||    | | | |
|    \/    \ /    \/ \/    | | | |
|    /\    / \    /\ /\    | | | |
|    ||    | |    || ||    | | | |
a    bb    b b    bb bb    b b b b
```

# Kilder

- Thea Holand
