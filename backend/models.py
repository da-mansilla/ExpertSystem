from pydantic import BaseModel, validator
from constants import PLATILLOS

class Comensales(BaseModel):
    cantidad_hombres_mayores: int 
    cantidad_hombres_menores: int
    cantidad_mujeres_mayores: int
    cantidad_mujeres_menores: int 

    @validator("cantidad_hombres_mayores","cantidad_hombres_menores","cantidad_mujeres_mayores","cantidad_mujeres_menores")
    def mayor_a_cero(cls,value):
        if value < 0:
            raise ValueError("Cantidad de comensales no puede ser menor a 0")
        return value

class UserInṕut(BaseModel):
    platillo_a_preparar : str 
    cantidad_de_dinero : int 
    comensales : Comensales

    @validator("platillo_a_preparar")
    def validar_platillo(cls,value):
        if value not in PLATILLOS:
            raise ValueError(f"El platillo {value} no se encuentra en la lista de platillos permitidos")
        return value

    @validator("cantidad_de_dinero")
    def mayor_a_cero_y_menor_a_30000(cls,value):
        if value < 0:
            raise ValueError("La cantidad de dinero ingresada no puede ser menor a 0")
        if value > 40000:
            raise ValueError("La cantidad de dinero ingresada no puede ser mayor a 40000")
        return value


