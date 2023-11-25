from MotorInferencia import MotorInferencia
from constants import *

def get_engine() -> MotorInferencia:
    motor = MotorInferencia()
    motor.reset()
    return motor


def validate_initial_values(
    platillo: str,
    cantidad_de_dinero: int,
    comensales: dict,
) -> None:
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

def get_initial_values() -> dict:
    platillo_a_preparar = MILANESA 
    cantidad_de_dinero = 15000 
    comensalesMock = {
        "cantidad_hombres_mayores": 1,
        "cantidad_hombres_menores": 0,
        "cantidad_mujeres_mayores": 0,
        "cantidad_mujeres_menores": 0,
    }
    try:
        validate_initial_values(
            platillo_a_preparar,
            cantidad_de_dinero,
            comensalesMock,
        )
    except Exception as e:
        raise Exception(e)

    return {
            "platillo_a_preparar":platillo_a_preparar,
            "cantidad_de_dinero":cantidad_de_dinero,
            "comensalesMock":comensalesMock
    }

def obtain_inference(motor: MotorInferencia,facts: dict) -> dict:
    platillo_a_preparar,cantidad_de_dinero,comensalesMock = facts.values()
    motor.add_initial_facts(platillo_a_preparar, cantidad_de_dinero, comensalesMock)
    motor.run()
    results = motor.get_results()
    print("---")
    print(motor.facts)
    print("---")
    return results

def show_results(results:dict) -> None:
    print("Recomendación")
    print(f"Se recomienda llevar {results['cantidad_carne']}g de los siguientes tipos de carne:\n")
    for corte in results["cortes_carne"]:
        precio_carne = int(corte[1] * (results['cantidad_carne']/1000))
        print(f"\t- {corte[0].capitalize()} -> ${precio_carne}")


def main():
    motor = get_engine()
    inputs_values = get_initial_values()
    results = obtain_inference(motor,inputs_values)
    show_results(results)


if __name__ == "__main__":
    main()
