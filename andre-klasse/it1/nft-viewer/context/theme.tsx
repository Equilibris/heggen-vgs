import { ThemeProvider as MuiTheme, Theme } from '@mui/material'
import {
	css,
	Global,
	jsx,
	ThemeProvider as EmotionThemeProvider,
} from '@emotion/react'
import { theme } from 'styles/theme'
import { FC } from 'react'
import background from 'assets/dot-grid.png'

export const ThemeProvider: FC = ({ children }) => {
	return (
		<MuiTheme theme={theme}>
			<EmotionThemeProvider theme={theme}>
				<Global
					styles={(theme) => css`
						body {
							overflow-x: hidden;
						}
						#__next {
							min-height: 100vh;
							background: url(${background.src});
						}
					`}
				/>
				{children}
			</EmotionThemeProvider>
		</MuiTheme>
	)
}
