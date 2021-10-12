# NFT-viewer innlevering

## Steg 0: Data kilde

Etter undersøkning på hvilken forksjellige NFT her jeg funntet https://cryptoart.io/

## Steg 1: Figma view av siden

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FQ9jCkpPZSUZh5UeKARfkfH%2FIT-1-NFT-viewer%3Fnode-id%3D0%253A1" allowfullscreen></iframe>

## Hvorfor valgte jeg å strukturere siden slik?

Jeg tenkte hvis jeg har en landing-page og en content-page fikk jeg en fin balangse av API hentet inhold og inhold som jeg har manulet produsert. Jeg brukte en derivasjon av the holy grail layout i form av at jeg droppet reklamen og asiden for å isteden ha parallax kjørende bilder som ledet til en fin og engaging user experience.

## Hvordan strukturerte jeg API-en

Jeg designet apien runt en wrapper for `cryptoart.io` sinn api siden jeg syns den hadde alt contente jeg trengte. Jeg brukte en wrapper isteden for en direkte tilkobling for å ungå XSS beskyttelsene deres av å kunne bruke [isomorthisk-fetch](https://nextjs.org/docs/basic-features/supported-browsers-features) over vanlig [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). Enda en grunn var jeg synes API-en deres var veldig treg så jeg ville legge til et cache lag i mellom. Dette er en FS cache som gjør serveren statefull, alså den ikke kan kjøre på en stateless runner som jeg planla.

## Kilder

- https://finanssans.no/nft
- https://cryptoart.io/
- https://www.hicetnunc.xyz/cornato3ds/creations
- https://cryptoart.io/top_artists
- https://cryptoart.io/artworks?artist=beeple&gallery=&price=&page=1&sort=usd_price
- https://cryptoart.io/artworks?gallery=&price=&page=1&sort=usd_price
