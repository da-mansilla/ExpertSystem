from experta import AND, MATCH, DefFacts, KnowledgeEngine, Fact, Field, Rule, OR, P
from schema import Or
from constants import *

PLATILLOS = [
    "Asado",
    "Hamburguesa",
    "Choripan",
    "Brochetas",
    "Churrasco",
    "Milanesa",
    "Lampreado",
    "Empanadas",
    "Albóndigas",
    "Estofado",
    "Sopa ",
    "Guiso",
    "Locro",
    "Carne a la olla",
    "Pastel de papa",
    "Arrollado de carne",
    "Pan de carne",
    "Lasaña",
    "Canelones de carne",
    "Bife",
    "Carne a la plancha",
]
TIPOS_DE_COCCION = [
    "Parrilla",
    "Frita",
    "Hervida",
    "Al horno",
    "Plancha",
]
TIPOS_DE_PRESUPUESTO = ["Bajo", "Alto"]


class Platillo(Fact):
    """
    Concepto Platillo
    Representa la comida que el cliente desea preparar
    """

    tipo = Field(Or(*PLATILLOS))
    tipo_de_coccion = Field(Or(PARRILLA, FRITA, HERVIDA, AL_HORNO, PLANCHA))


class Cliente(Fact):
    """
    Concepto Cliente
    Representa al cliente de la carniceria que pide una recomendacion
    """

    platillo_a_preparar = Field(Or(*PLATILLOS))
    cantidad_de_dinero = Field(int)
    cantidad_de_comensales = Field(Or(1, 2, 3, 4, 5))


class Presupuesto(Fact):
    """
    Concepto Presupuesto
    Representa el presupuesto que tiene el cliente para realizar su compra
    """

    monto = Field(Or(*TIPOS_DE_PRESUPUESTO))


class CorteDeCarne(Fact):
    """
    Concepto Corte de Carne
    Representa el corte de carne que tiene disponible la carniceria
    para realizar la recomendacion
    """

    nombre = Field(str)
    precio = Field(int)
    peso = Field(int)
    presencia_de_hueso = Field(bool)


class Comensal(Fact):
    """
    Concepto Comensal
    Representa la cantidad de personas para la cual el cliente necesita
    comprar carne
    """

    cantidad_hombres_mayores = Field(int)
    cantidad_hombres_menores = Field(int)
    cantidad_mujeres_mayores = Field(int)
    cantidad_mujeres_menores = Field(int)

class Recomendacion(Fact):
    """
    Concepto Recomendacion
    Representa la recomendacion que la carniceria entre al cliente
    """
    tipo_de_carne=Field(str)
    precio_total=Field(str)
    cantidad=Field(int)


# class TipoDeCoccion(Fact):
#     """
#     Concepto TipoDeCoccion
#     Representa el tipo de coccion que un platillo tiene
#     """
#
#     nombre = Field(str, mandatory=True)


class MotorInferencia(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Platillo(tipo=MILANESA)
        yield Cliente(
            platillo_a_preparar=MILANESA,
            cantidad_de_dinero=5001,
            cantidad_de_comensales=2,
        )
        yield Comensal(cantidad_hombres_mayores=2, cantidad_mujeres_mayores=1)

    @Rule(
        OR(
            Platillo(tipo=ASADO),
            Platillo(tipo=HAMBURGUESA),
            Platillo(tipo=CHORIPAN),
            Platillo(tipo=BROCHETAS),
            Platillo(tipo=CHURRASCO),
        )
    )
    def regla_1(self):
        self.declare(Platillo(tipo_de_coccion=PARRILLA))

    @Rule(
        OR(
            Platillo(tipo=MILANESA),
            Platillo(tipo=LAMPREADO),
            Platillo(tipo=EMPANADAS),
            Platillo(tipo=ALBONDIGAS),
        )
    )
    def regla_2(self):
        self.declare(Platillo(tipo_de_coccion=FRITA))

    @Rule(
        OR(
            Platillo(tipo=ESTOFADO),
            Platillo(tipo=SOPA),
            Platillo(tipo=GUISO),
            Platillo(tipo=LOCRO),
            Platillo(tipo=CARNE_A_LA_OLLA),
        )
    )
    def regla_3(self):
        self.declare(Platillo(tipo_de_coccion=HERVIDA))

    @Rule(
        OR(
            Platillo(tipo=PASTEL_DE_PAPA),
            Platillo(tipo=ARROLLADO_DE_CARNE),
            Platillo(tipo=PAN_DE_CARNE),
            Platillo(tipo=LASAÑA),
            Platillo(tipo=CANELONES_DE_CARNE),
        )
    )
    def regla_4(self):
        self.declare(Platillo(tipo_de_coccion=AL_HORNO))

    @Rule(OR(Platillo(tipo=BIFE), Platillo(tipo=CARNE_A_LA_PLANCHA)))
    def regla_5(self):
        self.declare(Platillo(tipo_de_coccion=PLANCHA))

    ####################################################

    @Rule(
        OR(
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 2000),
                cantidad_de_comensales=1,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 4000),
                cantidad_de_comensales=2,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 6000),
                cantidad_de_comensales=3,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 8000),
                cantidad_de_comensales=4,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 10000),
                cantidad_de_comensales=5,
            ),
        )
    )
    def regla_6(self):
        self.declare(Presupuesto(monto=MONTO_BAJO))

    @Rule(
        OR(
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 2000),
                cantidad_de_comensales=1,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 4000),
                cantidad_de_comensales=2,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 6000),
                cantidad_de_comensales=3,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 8000),
                cantidad_de_comensales=4,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 10000),
                cantidad_de_comensales=5,
            ),
        )
    )
    def regla_7(self):
        self.declare(Presupuesto(monto=MONTO_ALTO))

    ####################################################

    @Rule(AND(Platillo(tipo_de_coccion=PARRILLA)), Presupuesto(monto=MONTO_ALTO))
    def regla_8(self):
        self.declare(CorteDeCarne(presencia_de_hueso=True))

    @Rule(AND(Platillo(tipo_de_coccion=PARRILLA)), Presupuesto(monto=MONTO_BAJO))
    def regla_9(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=FRITA)), Presupuesto(monto=MONTO_ALTO))
    def regla_10(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=FRITA)), Presupuesto(monto=MONTO_BAJO))
    def regla_11(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=HERVIDA)), Presupuesto(monto=MONTO_ALTO))
    def regla_12(self):
        self.declare(CorteDeCarne(presencia_de_hueso=True))

    @Rule(AND(Platillo(tipo_de_coccion=HERVIDA)), Presupuesto(monto=MONTO_BAJO))
    def regla_13(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=AL_HORNO)), Presupuesto(monto=MONTO_ALTO))
    def regla_14(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=AL_HORNO)), Presupuesto(monto=MONTO_BAJO))
    def regla_15(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=PLANCHA)), Presupuesto(monto=MONTO_ALTO))
    def regla_16(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    @Rule(AND(Platillo(tipo_de_coccion=PLANCHA)), Presupuesto(monto=MONTO_BAJO))
    def regla_17(self):
        self.declare(CorteDeCarne(presencia_de_hueso=False))

    ####################################################

    @Rule(
        AND(
            Comensal(cantidad_hombres_menores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_18(self):
        self.declare(Recomendacion(cantidad=350))

    @Rule(
        AND(
            Comensal(cantidad_hombres_menores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_19(self):
        self.declare(Recomendacion(cantidad=250))

    @Rule(
        AND(
            Comensal(cantidad_hombres_mayores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_20(self):
        self.declare(Recomendacion(cantidad=500))

    @Rule(
        AND(
            Comensal(cantidad_hombres_mayores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_21(self):
        self.declare(Recomendacion(cantidad=400))

    @Rule(
        AND(
            Comensal(cantidad_mujeres_menores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_22(self):
        self.declare(Recomendacion(cantidad=350))

    @Rule(
        AND(
            Comensal(cantidad_mujeres_menores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_23(self):
        self.declare(Recomendacion(cantidad=250))

    @Rule(
        AND(
            Comensal(cantidad_mujeres_mayores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_24(self):
        self.declare(Recomendacion(cantidad=450))

    @Rule(
        AND(
            Comensal(cantidad_mujeres_mayores=P(lambda cantidad: cantidad > 0)),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_25(self):
        self.declare(Recomendacion(cantidad=450))

    ################################################

    @Rule(Presupuesto(monto=MONTO_ALTO),Platillo(tipo_de_coccion=PARRILLA),CorteDeCarne(presencia_de_hueso=True))
    def regla_26(self):
        print("recomendacion 1")

    @Rule(Presupuesto(monto=MONTO_ALTO),Platillo(tipo_de_coccion=FRITA),CorteDeCarne(presencia_de_hueso=False))
    def regla_27(self):
        print("recomendacion 2")

    @Rule(Presupuesto(monto=MONTO_ALTO),Platillo(tipo_de_coccion=HERVIDA),CorteDeCarne(presencia_de_hueso=True))
    def regla_28(self):
        print("recomendacion 3")

    @Rule(Presupuesto(monto=MONTO_ALTO),Platillo(tipo_de_coccion=AL_HORNO),CorteDeCarne(presencia_de_hueso=False))
    def regla_29(self):
        print("recomendacion 4")

    @Rule(Presupuesto(monto=MONTO_ALTO),Platillo(tipo_de_coccion=PLANCHA),CorteDeCarne(presencia_de_hueso=False))
    def regla_30(self):
        print("recomendacion 5")

    @Rule(Presupuesto(monto=MONTO_BAJO),Platillo(tipo_de_coccion=PARRILLA),CorteDeCarne(presencia_de_hueso=False))
    def regla_31(self):
        print("recomendacion 6")

    @Rule(Presupuesto(monto=MONTO_BAJO),Platillo(tipo_de_coccion=FRITA),CorteDeCarne(presencia_de_hueso=False))
    def regla_32(self):
        print("recomendacion 7")

    @Rule(Presupuesto(monto=MONTO_BAJO),Platillo(tipo_de_coccion=HERVIDA),CorteDeCarne(presencia_de_hueso=False))
    def regla_33(self):
        print("recomendacion 8")

    @Rule(Presupuesto(monto=MONTO_BAJO),Platillo(tipo_de_coccion=AL_HORNO),CorteDeCarne(presencia_de_hueso=False))
    def regla_34(self):
        print("recomendacion 9")

    @Rule(Presupuesto(monto=MONTO_BAJO),Platillo(tipo_de_coccion=PLANCHA),CorteDeCarne(presencia_de_hueso=False))
    def regla_35(self):
        print("recomendacion 10")


    @Rule(Platillo(tipo_de_coccion=FRITA), Presupuesto(monto=MATCH.monto))
    def prueba(self, monto):
        print(f"cocina frita y tiene monto {monto}")




def main():
    motor = MotorInferencia()
    motor.reset()
    motor.run()


if __name__ == "__main__":
    main()
