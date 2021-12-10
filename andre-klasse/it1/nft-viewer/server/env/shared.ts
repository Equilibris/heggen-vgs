export const dev = process.env.NODE_ENV !== 'production'

export const pathName = dev ? 'http://localhost:3000' : 'http://localhost:3000'
