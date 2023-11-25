from MotorInferencia import MotorInferencia
from constants import *

def validate_initial_values(
    platillo: str,
    cantidad_de_dinero: int,
    comensales: dict,
):
    if platillo not in PLATILLOS:
        raise Exception("Platillo no encontrado")
    if cantidad_de_dinero < 0:
        raise Exception("Cantidad ingresada Inválida")
    for key in comensales.keys():
        if key not in TIPOS_COMENSALES:
            raise Exception("Tipos de comensales no validos")
    valores_validos = all(
        isinstance(valor, int) and valor >= 0 for valor in comensales.values()
    )

    if not valores_validos:
        raise Exception("Valores de tipos de comensales no validos")


def main():
    motor = MotorInferencia()
    motor.reset()

    platillo_a_preparar = ASADO
    cantidad_de_dinero = 1800
    comensalesMock = {
        "cantidad_hombres_mayores": 3,
        "cantidad_hombres_menores": 0,
        "cantidad_mujeres_mayores": 1,
        "cantidad_mujeres_menores": 0,
    }
    try:
        validate_initial_values(
            platillo_a_preparar,
            cantidad_de_dinero,
            comensalesMock,
        )
    except Exception as e:
        print(e)
        return 1

    motor.add_initial_values(platillo_a_preparar, cantidad_de_dinero, comensalesMock)
    motor.run()
    # print(motor.facts)
    motor.get_results()


if __name__ == "__main__":
    main()
