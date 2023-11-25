from experta import (
    AND,
    AS,
    MATCH,
    W,
    DefFacts,
    KnowledgeEngine,
    Fact,
    Field,
    Rule,
    OR,
    P,
)
from schema import Or
from constants import *


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
    cantidad_de_comensales = Field(Or(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


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

    tipo_de_carne = Field(str)
    precio_total = Field(str)
    cantidad = Field(int)


# class TipoDeCoccion(Fact):
#     """
#     Concepto TipoDeCoccion
#     Representa el tipo de coccion que un platillo tiene
#     """
#
#     nombre = Field(str, mandatory=True)


class MotorInferencia(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.cantidad_carne = 0
        self.cortes_carne = []

    def get_results(self) -> dict:
        return {
            "cantidad_carne": self.cantidad_carne,
            "cortes_carne": self.cortes_carne,
        }

    def add_initial_facts(
        self,
        platillo: str,
        cantidad_de_dinero: int,
        comensales: dict,
    ):
        sumar_valores = lambda d: sum(d.values())
        cantidad_de_comensales = sumar_valores(comensales)
        self.declare(
            Cliente(
                platillo_a_preparar=platillo,
                cantidad_de_dinero=cantidad_de_dinero,
                cantidad_de_comensales=cantidad_de_comensales,
            )
        )
        self.declare(
            Comensal(
                cantidad_hombres_mayores=comensales["cantidad_hombres_mayores"],
                cantidad_hombres_menores=comensales["cantidad_hombres_menores"],
                cantidad_mujeres_mayores=comensales["cantidad_mujeres_mayores"],
                cantidad_mujeres_menores=comensales["cantidad_mujeres_menores"],
            )
        )

    # @DefFacts()
    # def _initial_action(self):
    #     # yield Platillo(tipo=ASADO)
    #     yield Cliente(
    #         platillo_a_preparar=ASADO,
    #         cantidad_de_dinero=1800,
    #         cantidad_de_comensales=1,
    #     )
    #     yield Comensal(cantidad_hombres_mayores=1)
    #     # yield Comensal(cantidad_mujeres_mayores=2,cantidad_mujeres_menores=2)
    #     # yield CorteDeCarne(presencia_de_hueso=True)

    @Rule(
        OR(
            Cliente(platillo_a_preparar=ASADO),
            Cliente(platillo_a_preparar=HAMBURGUESA),
            Cliente(platillo_a_preparar=CHORIPAN),
            Cliente(platillo_a_preparar=BROCHETAS),
            Cliente(platillo_a_preparar=CHURRASCO),
        )
    )
    def regla_1(self):
        self.declare(Platillo(tipo_de_coccion=PARRILLA))

    @Rule(
        OR(
            Cliente(platillo_a_preparar=MILANESA),
            Cliente(platillo_a_preparar=LAMPREADO),
            Cliente(platillo_a_preparar=EMPANADAS),
            Cliente(platillo_a_preparar=ALBONDIGAS),
        )
    )
    def regla_2(self):
        self.declare(Platillo(tipo_de_coccion=FRITA))

    @Rule(
        OR(
            Cliente(platillo_a_preparar=ESTOFADO),
            Cliente(platillo_a_preparar=SOPA),
            Cliente(platillo_a_preparar=GUISO),
            Cliente(platillo_a_preparar=LOCRO),
            Cliente(platillo_a_preparar=CARNE_A_LA_OLLA),
        )
    )
    def regla_3(self):
        self.declare(Platillo(tipo_de_coccion=HERVIDA))

    @Rule(
        OR(
            Cliente(platillo_a_preparar=PASTEL_DE_PAPA),
            Cliente(platillo_a_preparar=ARROLLADO_DE_CARNE),
            Cliente(platillo_a_preparar=PAN_DE_CARNE),
            Cliente(platillo_a_preparar=LASAÑA),
            Cliente(platillo_a_preparar=CANELONES_DE_CARNE),
        )
    )
    def regla_4(self):
        self.declare(Platillo(tipo_de_coccion=AL_HORNO))

    @Rule(
        OR(
            Cliente(platillo_a_preparar=BIFE),
            Cliente(platillo_a_preparar=CARNE_A_LA_PLANCHA),
        )
    )
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
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 12000),
                cantidad_de_comensales=6,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 14000),
                cantidad_de_comensales=7,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 16000),
                cantidad_de_comensales=8,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 18000),
                cantidad_de_comensales=9,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero <= 20000),
                cantidad_de_comensales=10,
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
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 12000),
                cantidad_de_comensales=6,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 14000),
                cantidad_de_comensales=7,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 16000),
                cantidad_de_comensales=8,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 18000),
                cantidad_de_comensales=9,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 20000),
                cantidad_de_comensales=10,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 22000),
                cantidad_de_comensales=11,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 24000),
                cantidad_de_comensales=12,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 26000),
                cantidad_de_comensales=13,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 28000),
                cantidad_de_comensales=14,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 30000),
                cantidad_de_comensales=15,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 32000),
                cantidad_de_comensales=16,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 34000),
                cantidad_de_comensales=17,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 36000),
                cantidad_de_comensales=18,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 38000),
                cantidad_de_comensales=19,
            ),
            Cliente(
                cantidad_de_dinero=P(lambda dinero: dinero > 40000),
                cantidad_de_comensales=20,
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
            Comensal(
                cantidad_hombres_menores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_18(self, cantidad):
        self.cantidad_carne += 350 * cantidad
        self.declare(Recomendacion(cantidad=350))

    @Rule(
        AND(
            Comensal(
                cantidad_hombres_menores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_19(self, cantidad):
        self.cantidad_carne += 250 * cantidad
        self.declare(Recomendacion(cantidad=250))

    @Rule(
        AND(
            Comensal(
                cantidad_hombres_mayores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_20(self, cantidad):
        self.cantidad_carne += 500 * cantidad
        self.declare(Recomendacion(cantidad=500))

    @Rule(
        AND(
            Comensal(
                cantidad_hombres_mayores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_21(self, cantidad):
        self.cantidad_carne += 400 * cantidad
        self.declare(Recomendacion(cantidad=400))

    @Rule(
        AND(
            Comensal(
                cantidad_mujeres_menores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_22(self, cantidad):
        self.cantidad_carne += 350 * cantidad
        self.declare(Recomendacion(cantidad=350))
        # print(f"valor de la recomendacion: {cantidad}")
        # self.declare(Fact(hacer_suma=450))

    @Rule(
        AND(
            Comensal(
                cantidad_mujeres_menores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_23(self, cantidad):
        self.cantidad_carne += 250 * cantidad
        self.declare(Recomendacion(cantidad=250))

    @Rule(
        AND(
            Comensal(
                cantidad_mujeres_mayores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=True),
        )
    )
    def regla_24(self, cantidad):
        self.cantidad_carne += 450 * cantidad
        self.declare(Recomendacion(cantidad=450))

    @Rule(
        AND(
            Comensal(
                cantidad_mujeres_mayores=P(lambda cantidad: cantidad > 0)
                & MATCH.cantidad
            ),
            CorteDeCarne(presencia_de_hueso=False),
        )
    )
    def regla_25(self, cantidad):
        self.cantidad_carne += 350 * cantidad
        self.declare(Recomendacion(cantidad=350))

    ################################################

    @Rule(
        Presupuesto(monto=MONTO_ALTO),
        Platillo(tipo_de_coccion=PARRILLA),
        CorteDeCarne(presencia_de_hueso=True),
    )
    def regla_26(self):
        self.cortes_carne += RECOMENDACION_1

    @Rule(
        Presupuesto(monto=MONTO_ALTO),
        Platillo(tipo_de_coccion=FRITA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_27(self):
        self.cortes_carne += RECOMENDACION_2

    @Rule(
        Presupuesto(monto=MONTO_ALTO),
        Platillo(tipo_de_coccion=HERVIDA),
        CorteDeCarne(presencia_de_hueso=True),
    )
    def regla_28(self):
        self.cortes_carne += RECOMENDACION_3

    @Rule(
        Presupuesto(monto=MONTO_ALTO),
        Platillo(tipo_de_coccion=AL_HORNO),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_29(self):
        self.cortes_carne += RECOMENDACION_4

    @Rule(
        Presupuesto(monto=MONTO_ALTO),
        Platillo(tipo_de_coccion=PLANCHA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_30(self):
        self.cortes_carne += RECOMENDACION_5

    @Rule(
        Presupuesto(monto=MONTO_BAJO),
        Platillo(tipo_de_coccion=PARRILLA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_31(self):
        self.cortes_carne += RECOMENDACION_6

    @Rule(
        Presupuesto(monto=MONTO_BAJO),
        Platillo(tipo_de_coccion=FRITA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_32(self):
        self.cortes_carne += RECOMENDACION_7

    @Rule(
        Presupuesto(monto=MONTO_BAJO),
        Platillo(tipo_de_coccion=HERVIDA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_33(self):
        self.cortes_carne += RECOMENDACION_8

    @Rule(
        Presupuesto(monto=MONTO_BAJO),
        Platillo(tipo_de_coccion=AL_HORNO),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_34(self):
        self.cortes_carne += RECOMENDACION_9

    @Rule(
        Presupuesto(monto=MONTO_BAJO),
        Platillo(tipo_de_coccion=PLANCHA),
        CorteDeCarne(presencia_de_hueso=False),
    )
    def regla_35(self):
        self.cortes_carne += RECOMENDACION_10

    # @Rule(Platillo(tipo_de_coccion=FRITA), Presupuesto(monto=MATCH.monto))
    # def prueba(self, monto):
    #     print(f"cocina frita y tiene monto {monto}")
