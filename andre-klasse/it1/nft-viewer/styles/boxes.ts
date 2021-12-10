import styled from '@emotion/styled'
import Box from '@mui/material/Box'

export const DisabledBox = styled(Box)`
	color: ${({ theme }) => theme.palette.text.disabled};
`

export const ColoredBox = styled(Box)`
	color: ${({ theme }) => theme.palette.primary.main};
`

export const PrimaryBox = styled(Box)`
	color: ${({ theme }) => theme.palette.text.primary};
`
export const SecondaryBox = styled(Box)`
	color: ${({ theme }) => theme.palette.text.secondary};
`

export const EmphasisBox = styled(Box)`
	font-weight: bold;
`
