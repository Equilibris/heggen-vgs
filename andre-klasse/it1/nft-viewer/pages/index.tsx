import styled from '@emotion/styled'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'
import { Link } from 'components/Link'
import type { NextPage } from 'next'
import React, { FC } from 'react'
import { ColoredBox, EmphasisBox, PrimaryBox } from 'styles/boxes'
import { Parallax, ParallaxLayer } from '@react-spring/parallax'
const illuminatedPath = '/front-page-nfts/illuminated-path.mp4'
const intoTheEather = '/front-page-nfts/into-the-eather.mp4'
const trippleKill = '/front-page-nfts/tripple-kill.mp4'

const NftVideoPlayer: FC<{ src: string }> = ({ src }) => (
	<EnterContainer d={Math.random() * 3}>
		<Link href='/' style={{ padding: 0 }}>
			<video autoPlay loop muted width='300'>
				<source src={src} type='video/webm' />
			</video>
		</Link>
	</EnterContainer>
)

const Home: NextPage = () => {
	return (
		<>
			<Parallax pages={2.5} style={{ top: '0', left: '0' }}>
				<ParallaxLayer offset={1.7} speed={1}>
					<div style={{ position: 'relative', left: '50vw' }}>
						<NftVideoPlayer src={illuminatedPath} />
					</div>
				</ParallaxLayer>
				<ParallaxLayer offset={1.5} speed={0.5}>
					<div style={{ position: 'relative', left: '10vw' }}>
						<NftVideoPlayer src={intoTheEather} />
					</div>
				</ParallaxLayer>
				<ParallaxLayer offset={1} speed={0.3}>
					<div style={{ position: 'relative', left: '60vw' }}>
						<NftVideoPlayer src={trippleKill} />
					</div>
				</ParallaxLayer>
				<ParallaxLayer>
					<MainContainer>
						<Typography
							variant='h1'
							style={{ zIndex: 10, textAlign: 'center' }}>
							En ny generasjon <br />
							av digital <ColoredBox component='span'>kunst</ColoredBox> .
						</Typography>

						<CardElement>
							<CardContent>
								<Stack gap={2}>
									<Typography variant='h4'>
										<EmphasisBox component='span'>
											Fårestill deg en verden: dær et mesterværk du eier, kan
											bli beundret av alle
										</EmphasisBox>
									</Typography>
									<Typography>
										I tidligere år, når man har kjøpt et verk, så kjøper man det
										for seg selv. Den eneste måten å vise det fremm er å henge
										det opp i sitt hus, men hvis du vil verden skal de noe du
										eier, kan du nå.
									</Typography>
									<Typography>
										I verdenen av NFTer kan man kjøpe et værk, og la
										internettet; la verden, vise det fram.
									</Typography>
									<Link href='/catalogue'>Se vår katalåg</Link>
								</Stack>
							</CardContent>
						</CardElement>
						<CardElement>
							<CardContent>
								<Stack gap={2}>
									<Typography variant='h4'>
										<EmphasisBox component='span'>Hva er en NFT?</EmphasisBox>
									</Typography>
									<Typography>
										En slik token er et bevis på at man eier den digitale
										eiendelen den representerer. Det kan blant annet være kunst,
										fotografier, musikk, kortsamlinger, produkter i spill og
										domenenavn.
									</Typography>
									<Typography>
										NFTer kan også knyttes til fysiske eiendeler, som for
										eksempel en rødvinsflaske fra 1787 stående i en vinkjeller i
										Bordeaux. Det gjør at teknologien i praksis kan brukes til å
										handle allslags eiendeler.
									</Typography>
									<Typography>
										Til å oppsumere en NFT et digital symbol som kan knyttes til
										en eier. Dette betyr at man kan kjøpe en NFT som klassisk
										kunst.
									</Typography>
									<Link href='/catalogue'>Se vår katalåg</Link>
								</Stack>
							</CardContent>
						</CardElement>
					</MainContainer>
				</ParallaxLayer>
			</Parallax>
		</>
	)
}

export default Home

const EnterContainer = styled.div<{ d: number }>`
	animation: enter 1.5s ease-out ${({ d }) => d}s;

	animation-fill-mode: both;

	width: 300px;

	@keyframes enter {
		0% {
			opacity: 0;
			transform: translateY(50px);
		}
		100% {
			opacity: 1;
			transform: translateY(0px);
		}
	}
`

const MainContainer = styled.div`
	position: relative;

	display: flex;
	align-items: center;
	min-height: 100vh;
	flex-direction: column;

	padding: 10vh;
	gap: 30vh;
`

const CardElement = styled(Card)`
	max-width: 60ch;

	background-color: #fff8;

	/* background-color: rgba(255, 255, 255, 0.15);
	background-color: rgba(255, 255, 255, 0.15); */
	backdrop-filter: blur(10px);
`
