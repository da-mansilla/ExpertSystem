from experta import MATCH, DefFacts, KnowledgeEngine, Fact, Field, Rule, OR, P
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
    cantidad_de_comensales = Field(Or(1,2,3,4,5))


class Presupuesto(Fact):
    """
    Concepto Presupuesto
    Representa el presupuesto que tiene el cliente para realizar su compra
    """

    monto = Field(Or(*TIPOS_DE_PRESUPUESTO))


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
        yield Cliente(platillo_a_preparar=MILANESA, cantidad_de_dinero=5001, cantidad_de_comensales=2)

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
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero <= 2000 ), cantidad_de_comensales=1),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero <= 4000 ), cantidad_de_comensales=2),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero <= 6000 ), cantidad_de_comensales=3),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero <= 8000 ), cantidad_de_comensales=4),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero <= 10000), cantidad_de_comensales=5),
        )
    )
    def regla_6(self):
        self.declare(Presupuesto(monto="Bajo"))

    @Rule(
        OR(
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero > 2000 ), cantidad_de_comensales=1),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero > 4000 ), cantidad_de_comensales=2),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero > 6000 ), cantidad_de_comensales=3),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero > 8000 ), cantidad_de_comensales=4),
            Cliente(cantidad_de_dinero=P(lambda dinero: dinero > 10000 ), cantidad_de_comensales=5),
        )
    )
    def regla_7(self):
        self.declare(Presupuesto(monto="Alto"))

    @Rule(Platillo(tipo_de_coccion=FRITA),Presupuesto(monto=MATCH.monto))
    def prueba(self,monto):
        print(f"cocina frita y tiene monto {monto}")
        # self.declare(Platillo(tipo_de_coccion=PARRILLA))


def main():
    motor = MotorInferencia()
    motor.reset()
    motor.run()


if __name__ == "__main__":
    main()
