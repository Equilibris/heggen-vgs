import 'styles/global.css'
import type { AppProps } from 'next/app'
import { Nav } from 'components/Nav'
import React, { FC } from 'react'
import { ThemeProvider } from 'context/theme'
import Divider from '@mui/material/Divider'
import styled from '@emotion/styled'
import Typography from '@mui/material/Typography'

const MyApp = ({ Component, pageProps }: AppProps) => {
	return (
		<ThemeProvider>
			<Nav />
			<Main>
				<Component {...pageProps} />
			</Main>
			<Divider></Divider>
			<Footer>
				<Typography>Made by William Sørensen</Typography>
			</Footer>
		</ThemeProvider>
	)
}
export default MyApp

const Main = styled.main`
	min-height: calc(100vh - ${({ theme }) => theme.spacing(10.1)});
`

const Footer = styled.footer`
	margin-top: auto;

	height: ${({ theme }) => theme.spacing(10)};
	background-color: ${({ theme }) => theme.palette.primary.main};
	color: ${({ theme }) => theme.palette.primary.contrastText};

	display: flex;
	justify-content: center;
	align-items: center;
`
