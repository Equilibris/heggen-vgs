import { createContext, FC, useContext, useRef, useState } from 'react'
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
	const ref = useRef<HTMLTextAreaElement>(null)

	return (
		<div>
			<form
				onSubmit={(e) => {
					e.preventDefault()
					const data = new FormData(e.currentTarget)

					const activity = parseFloat((data.get('activity') as string) || '0')
					const intensity =
						{
							low: 0.8,
							medium: 1,
							high: 1.2,
						}[data.get('intensity') as string] || 1

					const duration = parseFloat(
						`${(data.get('duration') as string) || 0}`
					)

					if (ref.current)
						ref.current.value = `${(activity * intensity * duration) / 60}kcal`
				}}>
				<select
					onChange={(v) => console.log(v.currentTarget.value)}
					name='activity'>
					<option value='814'>Aerobics</option>
					<option value='236'>Bordtennis</option>
					<option value='510'>Fotball</option>
					<option value='244'>Golf</option>
					<option value='666'>Jogging</option>
				</select>

				<div>
					<input type='radio' name='intensity' value='low' id='low' />
					<label htmlFor='low'>Lav</label>
					<input type='radio' name='intensity' value='medium' id='medium' />
					<label htmlFor='medium'>Middels</label>
					<input type='radio' id='high' name='intensity' value='high' />
					<label htmlFor='high'>high</label>
				</div>

				<label htmlFor='duration'>Duration</label>
				<input type='number' step='0.001' name='duration' id='duration' />

				<button>Submit</button>
			</form>

			<textarea
				name='result'
				contentEditable='false'
				value='Svar'
				ref={ref}></textarea>
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
