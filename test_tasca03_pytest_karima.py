"""
Bateria de proves amb pytest per als exercicis 2, 3 i 4
"""
import pytest
import provaescrita03 as prova

# =========================================================
# Tests Exercici 2
# =========================================================
@pytest.mark.parametrize(
    "persones, resultat_esperat",
    [
        (
            [
                {'nom': 'Anna', 'edat': 25},
                {'nom': 'Marc', 'edat': 42},
                {'nom': 'Laura', 'edat': 35}
            ],
            42
        ),
        ([], -1),
        (
            [
                {'nom': 'Anna', 'edat': 25},
                {'nom': 'Marc'}
            ],
            -1
        ),
        (
            [
                {'nom': 'Anna', 'edat': 25},
                {'nom': 'Marc', 'edat': '42'}
            ],
            -1
        ),
    ]
)
def test_trobar_edat_maxima(persones, resultat_esperat):
    """
    Comprova el funcionament de trobar_edat_maxima.
    """
    assert prova.trobar_edat_maxima(persones) == resultat_esperat


# =========================================================
# Tests Exercici 3
# =========================================================

@pytest.mark.parametrize(
    "llista_productes, resultat_esperat",
    [
        (
            [
                {'nom': 'A', 'preu': 10},
                {'nom': 'B', 'preu': 25},
                {'nom': 'C', 'preu': 18}
            ],
            {'nom': 'B', 'preu': 25}
        ),
        ([], None),
    ]
)
def test_trobar_producte_mes_car(llista_productes, resultat_esperat):
    """
    Comprova que es retorna el producte amb el preu més alt
    o None si la llista és buida.
    """
    prova.productes = llista_productes
    assert prova.trobar_producte_mes_car() == resultat_esperat


# =========================================================
# Tests Exercici 4
# =========================================================

@pytest.mark.parametrize(
    "empresa, resultat_esperat",
    [
        (
            {
                'nom': 'Empresa X',
                'departaments': [
                    {
                        'nom': 'IT',
                        'empleats': [{'nom': 'A'}, {'nom': 'B'}]
                    },
                    {
                        'nom': 'RRHH',
                        'empleats': [{'nom': 'C'}]
                    }
                ]
            },
            {'IT': 2, 'RRHH': 1}
        ),
        (
            {
                'nom': 'Empresa Buida',
                'departaments': []
            },
            {}
        ),
    ]
)
def test_comptar_empleats_per_departament(empresa, resultat_esperat):
    """
    Comprova el recompte d'empleats per departament.
    """
    assert prova.comptar_empleats_per_departament(empresa) == resultat_esperat
