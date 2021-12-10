import styled from '@emotion/styled'

export const Parallax = styled.div<{
	p: number
}>`
	perspective: ${({ p }) => p}px;
	-webkit-perspective: ${({ p }) => p}px;
	overflow-x: hidden;
	overflow-y: auto;
`

export const ParallaxLayer = styled.div`
	position: absolute;
	inset: 0;
`

export const ParallaxLayerBase = styled(ParallaxLayer)`
	transform: translateZ(0);
`

export const ParallaxLayerBack = styled(ParallaxLayer)<{
	z: number
	p: number
}>`
	transform: translateZ(-${({ z }) => z}px) scale(${({ z, p }) => (z + 1) / p});
`

export const ParallaxGroup = styled.div`
	position: relative;
	transform-style: preserve-3d;
`
