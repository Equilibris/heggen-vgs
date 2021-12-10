// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

import { readFile, writeFile } from 'fs/promises'
import { root } from 'server/env'
import { join } from 'path'

export type Data = {
	artist: string
	artwork_id: number
	block_number: number
	collector: string
	date_sold: string
	description: string
	editions: number
	eth_price: number
	gallery: string
	id: number
	image: string
	mimetype: string
	name: string
	num_sold: number
	thumbnail: string
	url: string
	usd_price: number
	xtz_price: number
}[]

const getDataUrl = (page: number = 1): string =>
	`https://cryptoart.io/artworks?gallery=&price=&page=${page}&sort=usd_price`

const getData = (page: number = 1): Promise<Data> =>
	new Promise((resolve, reject) => {
		fetch(getDataUrl(page))
			.then(async (response) => {
				resolve(await response.json())
			})
			.catch(reject)
	})

const resolveData = async (page: number = 1): Promise<Data> => {
	const fsUrl = join(root, `./cache/pages/${page}.json`)

	try {
		const resolvedData: Data = JSON.parse((await readFile(fsUrl)).toString())

		return resolvedData
	} catch (_) {
		const data = await getData(page)

		await writeFile(fsUrl, JSON.stringify(data))

		await Promise.all(
			data.map((v) =>
				writeFile(
					join(root, `./cache/elements/${v.id}.json`),
					JSON.stringify(data)
				)
			)
		)

		return data
	}
}

export default async function handler(
	req: NextApiRequest,
	res: NextApiResponse<Data>
) {
	res.status(200).json(await resolveData(+(req.query['page'] || 1)))
}
