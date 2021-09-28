import React, { useState } from 'react'

import interImg from './assets/inter.jpg'
import milanImg from './assets/milan.jpg'
import romaImg from './assets/roma.jpg'

type DataElement = {
	teamName: string
	suitColour: string
	img: string
	scream: string
}
const data: DataElement[] = [
	{ teamName: 'AC Milan', img: milanImg, scream: '', suitColour: 'Rød' },
	{ teamName: 'AS Roma', img: romaImg, scream: '', suitColour: 'Grønn' },
	{ teamName: 'FC Inter', img: interImg, scream: '', suitColour: 'Blå' },
]

export function Oppgave1() {
	const [selected, setSelected] = useState<null | DataElement>(null)

	return (
		<>
			<table>
				<thead>
					<tr>
						<th>Lag navn</th>
						<th>Drakt farge</th>
						<th>Select</th>
					</tr>
				</thead>
				<tbody>
					{data.map((x) => (
						<tr key={x.teamName}>
							<td>{x.teamName}</td>
							<td>{x.suitColour}</td>
							<td>
								{selected?.teamName !== x.teamName ? (
									<button onClick={() => setSelected(x)}>Select</button>
								) : (
									<button onClick={() => setSelected(null)}>Deselect</button>
								)}
							</td>
						</tr>
					))}
				</tbody>
			</table>
			{selected && (
				<div>
					<h1>{selected.teamName}</h1>
					<p>{selected.suitColour}</p>
					<img src={selected.img} alt={selected.teamName} />
				</div>
			)}
		</>
	)
}
