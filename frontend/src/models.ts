export interface Results{
    cantidad_carne : number,
    cortes: [CorteCarne]
    justificacion: string
}

export interface CorteCarne{
    nombre : string
    precio_corte: number
    precio_total: number
}
