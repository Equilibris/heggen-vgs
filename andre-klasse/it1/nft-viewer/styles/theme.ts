import {
	ThemeProvider as MuiThemeProvider,
	createTheme,
	Theme,
} from '@mui/material/styles'
import React, { FC } from 'react'

export const theme = createTheme({
	palette: {
		primary: {
			main: '#d81b60',
		},
		secondary: {
			main: '#5c6bc0',
		},
	},
})
