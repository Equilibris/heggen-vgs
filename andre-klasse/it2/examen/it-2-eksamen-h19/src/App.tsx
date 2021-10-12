import { createContext, FC, useContext, useState } from 'react'
import kropp from './assets/kropp-cropped.gif'
import armstrekkeren from './assets/armstrekkeren-fixed.mp3'
import brede_ryggmuskel from './assets/brede_ryggmuskel.mp3'

// @ts-ignore
const ctx = createContext<
	[
		Record<string, boolean>,
		React.Dispatch<React.SetStateAction<Record<string, boolean>>>
	]
>([{}, () => null])

const Area: FC<{
	left: number
	top: number
	children: string
	audio?: string
}> = ({ left, top, children, audio }) => {
	const [c, sC] = useContext(ctx)

	const s = c[children] || false

	return (
		<div
			onClick={() => {
				if (!s && audio) {
					new Audio(audio).play()
				}
				sC({ [children]: !s })
			}}
			onMouseLeave={() => sC({ [children]: !1 })}
			style={{
				cursor: 'pointer',
				position: 'absolute',
				left,
				top,
				color: 'white',
				background: s ? 'black' : 'white',

				transition: '0.5s',

				opacity: +s,

				borderRadius: 50 * +s,
				padding: 10,
			}}>
			{children}
		</div>
	)
}

const Oppgave1 = () => {
	return (
		<ctx.Provider value={useState({})}>
			<div style={{ position: 'relative' }}>
				<Area left={370} top={160} audio={armstrekkeren}>
					Armstrekkeren
				</Area>
				<Area left={250} top={130}>
					Kappemuskelen
				</Area>

				<Area left={225} top={100}>
					De lange ryggstrekkerne
				</Area>
				<Area left={120} top={230}>
					De lange ryggstrekkerne
				</Area>
				<Area left={225} top={270}>
					De lange ryggstrekkerne
				</Area>

				<Area left={320} top={230} audio={brede_ryggmuskel}>
					Den brede ryggmuskelen
				</Area>

				<Area left={225} top={330}>
					Hofteleddsstrekkene
				</Area>

				<Area left={270} top={425}>
					Knebøyerne
				</Area>

				<Area left={260} top={525}>
					Ankelstrekkerne
				</Area>

				<img
					useMap='#infographic'
					src={kropp}
					alt='musklatur i menneskekropp'
				/>
			</div>
		</ctx.Provider>
	)
}

const Oppgave2 = () => {
	return (
		<div>
			<select onChange={(v) => console.log(v.currentTarget.value)}>
				<option value='hello'>hello</option>
				<option value='hello2'>hello2</option>
				<option value='hello3'>hello3</option>
			</select>
		</div>
	)
}

function App() {
	return (
		<main>
			<Oppgave1 />
			<Oppgave2 />
		</main>
	)
}

export default App
