import React, { FC, useEffect, useMemo, useRef, useState } from 'react'
import styled from '@emotion/styled'
import { Data } from './api/catalogue'
import chunk from 'lodash/chunk'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'
import { EmphasisBox } from 'styles/boxes'
import CircularProgress from '@mui/material/CircularProgress'
import { NextPage } from 'next'
import { pathName } from 'server/env/shared'
import { useGlobalStore } from 'hooks/useStore'

const rows = 4

const size = 20

const rowExpansion = 2

const NftViewer: FC<{ data: Data[number] }> = ({ data }) => {
	const videoRef = useRef<HTMLVideoElement>(null)

	const containerRef = useRef<HTMLDivElement>(null)

	const [hasBeenVisible, setHasBeenVisible] = useGlobalStore(
		`nft-has-been-loaded-with-id-(${data.id})`,
		false
	)

	useEffect(() => {
		if (!hasBeenVisible) {
			const observer = new IntersectionObserver(async (e) => {
				for (const value of e) {
					if (value.isIntersecting) {
						setHasBeenVisible(true)
					}
				}
			}, {})

			if (containerRef.current) {
				const value = containerRef.current

				observer.observe(value)

				return () => {
					observer.unobserve(value)
				}
			}
		}
	}, [hasBeenVisible, setHasBeenVisible])

	return (
		<NftContainer
			ref={containerRef}
			onMouseEnter={() => {
				if (videoRef.current) {
					videoRef.current.play()
				}
			}}
			onMouseLeave={() => {
				requestAnimationFrame(() => {
					if (videoRef.current) {
						videoRef.current.pause()
					}
				})
			}}>
			{hasBeenVisible && (
				<video ref={videoRef} loop muted poster={data.thumbnail}>
					<source src={data.image} />
				</video>
			)}

			<Typography className='title'>
				<EmphasisBox component='span'>{data.name}</EmphasisBox> - {data.artist}
			</Typography>
		</NftContainer>
	)
}

const Catalogue: NextPage<{ hydration: Data }> = ({ hydration }) => {
	const loaderRef = useRef<HTMLDivElement>(null)

	const [data, setData] = useState<Data>(hydration)

	const index = useRef(2)

	useEffect(() => {
		const job = async (index: number): Promise<Data> =>
			(await fetch(`${pathName}/api/catalogue?page=${index}`)).json()

		const observer = new IntersectionObserver(async (e) => {
			for (const value of e) {
				if (value.isIntersecting) {
					const result = await job(index.current++)

					setData((data) => {
						console.log(data)

						return [...data, ...result]
					})

					break
				}
			}
		}, {})
		if (loaderRef.current) {
			observer.observe(loaderRef.current)
		}
	}, [])

	const chunkedData = useMemo(() => chunk(data, rows), [data])

	return (
		<MainContainer>
			<ParentStack gap={2} direction='column'>
				{chunkedData.map((subData, parentIndex) => (
					<ChildStack direction='row' key={parentIndex} gap={2}>
						{subData.map((el, index) => (
							<NftViewer data={el} key={index}></NftViewer>
						))}
					</ChildStack>
				))}
			</ParentStack>
			<ProgressContainer ref={loaderRef}>
				<CircularProgress />
			</ProgressContainer>
		</MainContainer>
	)
}

Catalogue.getInitialProps = async (ctx) => {
	const hydration: Data = await (
		await fetch(`${pathName}/api/catalogue?page=1`)
	).json()

	return { hydration }
}

const ProgressContainer = styled.div`
	display: flex;
	align-items: center;
	justify-content: center;

	padding-top: ${({ theme }) => theme.spacing(2)};
`

const MainContainer = styled.main`
	min-height: 100vh;
	width: ${({ theme }) =>
		theme.spacing(size * (rows + rowExpansion - 1) + 2 * (rows - 1))};

	position: relative;

	padding: ${({ theme }) => theme.spacing(12)};

	left: 50%;
	transform: translateX(-50%);
`

const NftContainer = styled.div`
	height: ${({ theme }) => theme.spacing(size)};
	width: ${({ theme }) => theme.spacing(size)};

	overflow: hidden;

	display: flex;
	justify-content: center;
	align-items: center;

	position: relative;

	video {
		width: 101%;
		/* min-width: 150%;
		min-height: 150%; */
	}
	.title {
		color: white;

		transition: 0.5s;

		opacity: 0;

		position: absolute;
		bottom: ${({ theme }) => theme.spacing(0.5)};
		left: ${({ theme }) => theme.spacing(0.5)};
		right: ${({ theme }) => theme.spacing(0.5)};
	}

	&::before {
		content: '';

		position: absolute;

		inset: 0;

		background: linear-gradient(#0000, #0006);

		opacity: 0;

		transition: 0.5s;
	}

	&:hover {
		&::before {
			opacity: 1;
		}

		.title {
			transition-delay: 1s;

			opacity: 1;
		}
	}
`

const ChildStack = styled(Stack)``

const ParentStack = styled(Stack)`
	${ChildStack}:nth-of-type(2n):not(:hover) {
		${NftContainer}:nth-of-type(1) {
			flex: ${rowExpansion};
		}
	}
	${ChildStack}:nth-of-type(2n + 1):not(:hover) {
		${NftContainer}:nth-last-of-type(1) {
			flex: ${rowExpansion};
		}
	}
	${NftContainer} {
		flex: 1;

		will-change: flex, height, width;

		transition: 0.5s;
	}
	${ChildStack}:hover {
		${NftContainer}:hover {
			flex: ${rowExpansion};
		}
		${NftContainer} {
			transition-delay: 0.5s;

			height: ${({ theme }) => theme.spacing(size * rowExpansion)};
			width: ${({ theme }) => theme.spacing(size * rowExpansion)};
		}
	}
`

export default Catalogue
