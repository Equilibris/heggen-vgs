import Button, { ButtonProps } from '@mui/material/Button'
import React, { FC } from 'react'
import NLink, { LinkProps } from 'next/link'

export const Link: FC<Pick<LinkProps, 'href'> & ButtonProps> = ({
	children,
	href,
	...props
}) => {
	return (
		<NLink href={href} passHref>
			<Button {...props} variant='outlined' color='inherit'>
				{children}
			</Button>
		</NLink>
	)
}
