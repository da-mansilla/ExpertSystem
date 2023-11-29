from MotorInferencia import MotorInferencia
from constants import *
from models import UserInṕut


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
    platillo_a_preparar = ASADO 
    cantidad_de_dinero = 3000 
    comensalesMock = {
        "cantidad_hombres_mayores": 1,
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
        raise Exception(e)

    return {
            "platillo_a_preparar":platillo_a_preparar,
            "cantidad_de_dinero":cantidad_de_dinero,
            "comensalesMock":comensalesMock
    }

def obtain_inference(motor: MotorInferencia,facts: UserInṕut) -> dict:
    # platillo_a_preparar,cantidad_de_dinero,comensales = facts.model_dump().values()
    platillo_a_preparar = facts.platillo_a_preparar
    cantidad_de_dinero = facts.cantidad_de_dinero
    comensales = facts.comensales.model_dump()
    motor.add_initial_facts(platillo_a_preparar, cantidad_de_dinero, comensales)
    motor.run()
    inference = motor.get_results()
    justificacion = f"Estos cortes están re buenos porque se adaptan a un presupuesto {inference['presupuesto']}. Van de 10 para comidas {inference['tipo_coccion']}s. \n"
    if inference["presencia_hueso"]:
        justificacion += "Ademas, como contás con un buen presupuesto, estos cortes tienen huesito para agregarle mas sabor. !Va a quedar un espectaculo!\n"
    results = {
        "cantidad_carne": inference["cantidad_carne"],
        "cortes": [],
        "justificacion":justificacion
    }
    print(inference)
    for corte in inference["cortes_carne"]:
        results["cortes"].append({
                "nombre":corte[0],
                "precio_corte":corte[1],
                "precio_total":corte[1] * (results["cantidad_carne"] / 1000)
        })

    return results


def show_results(results:dict) -> None:
    print("Recomendación")
    print(f"Se recomienda llevar {results['cantidad_carne']}g de los siguientes tipos de carne:\n")
    for corte in results["cortes_carne"]:
        precio_carne = int(corte[1] * (results['cantidad_carne']/1000))
        print(f"\t- {corte[0].capitalize()} -> ${precio_carne}")
