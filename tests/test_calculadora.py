





import pytest

from calculadora import calcular_descuento, calcular_envio, dividir, sumar


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [(2, 3, 5), (-3, 2, -1), (0, 0, 0)],
)
def test_sumar(a: float, b: float, esperado: float) -> None:
    assert sumar(a, b) == esperado


def test_dividir() -> None:
    assert dividir(10, 2) == 5


def test_dividir_entre_cero() -> None:
    with pytest.raises(ValueError, match="dividir entre cero"):
        dividir(10, 0)


def test_calcular_descuento() -> None:
    assert calcular_descuento(200, 10) == 180
    assert calcular_descuento(100, 0) == 100
    assert calcular_descuento(100, 100) == 0


def test_rechaza_precio_negativo() -> None:
    with pytest.raises(ValueError, match="precio"):
        calcular_descuento(-100, 10)


@pytest.mark.parametrize("porcentaje", [-1, 101])
def test_rechaza_descuento_fuera_de_rango(porcentaje: float) -> None:
    with pytest.raises(ValueError, match="descuento"):
        calcular_descuento(100, porcentaje)


def test_calcular_envio_gratis() -> None:
    assert calcular_envio(1000, 10) == 0


def test_calcular_recargo_express() -> None:
    assert calcular_envio(500, 10, express=True) == 160

    
@pytest.mark.parametrize(
    ("distancia_km", "esperado"),
    [(4, 50), (10, 90), (30, 150)],
)
def test_calcular_envio_por_distancia(distancia_km: int, esperado: float) -> None:
    assert calcular_envio(500, distancia_km) == esperado


def test_rechaza_total_de_compra_negativo() -> None:
    with pytest.raises(ValueError, match="total de la compra"):
        calcular_envio(-1, 3)


def test_rechaza_distancia_negativa() -> None:
    with pytest.raises(ValueError, match="distancia"):
        calcular_envio(200, -1)
