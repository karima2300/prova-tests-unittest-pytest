import unittest
import tascaescrita1
import tascaescrita2

# TESTS PER A TASCA ESCRITA 01
class TestProvaEscrita01(unittest.TestCase):
    """
    Tests unitaris per a la Prova Escrita 01.
    Exercicis: 2 (buscar_per_titol), 3 (afegir_a_biblioteca), 4 (joc_mes_car)
    """

    def setUp(self):
        """S'executa abans de cada test per tenir una biblioteca neta."""
        self.videojocs = tascaescrita1.videojocs
        self.biblioteca = []

    # ----- Exercici 2 -----
    def test_buscar_per_titol_existent(self):
        """Comprova que es retorna el joc correcte quan existeix."""
        joc = tascaescrita1.buscar_per_titol("Cyberpunk 2077", self.videojocs)
        self.assertIsNotNone(joc)
        self.assertEqual(joc["titol"], "Cyberpunk 2077")

    def test_buscar_per_titol_insensible_majuscules(self):
        """Comprova que la cerca no és sensible a majúscules."""
        joc = tascaescrita1.buscar_per_titol("cyberpunk 2077", self.videojocs)
        self.assertIsNotNone(joc)

    def test_buscar_per_titol_inexistent(self):
        """Comprova que retorna None si el joc no existeix."""
        joc = tascaescrita1.buscar_per_titol("Mario Kart", self.videojocs)
        self.assertIsNone(joc)

    # ----- Exercici 3 -----
    def test_afegir_joc_correctament(self):
        """Comprova que un joc existent s'afegeix correctament."""
        resultat = tascaescrita1.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "✅ Joc afegit!")
        self.assertEqual(len(self.biblioteca), 1)

    def test_afegir_joc_duplicat(self):
        """Comprova que no es poden afegir jocs duplicats."""
        tascaescrita1.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        resultat = tascaescrita1.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "⚠️ Ja està a la biblioteca")

    def test_afegir_joc_inexistent(self):
        """Comprova que retorna missatge d'error si el joc no existeix."""
        resultat =tascaescrita1.afegir_a_biblioteca("Mario Kart", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "❌ Joc no trobat")

    # ----- Exercici 4 -----
    def test_joc_mes_car(self):
        """Comprova que retorna el videojoc amb el preu més alt."""
        joc = tascaescrita1.joc_mes_car(self.videojocs)
        self.assertIsNotNone(joc)
        self.assertEqual(joc["titol"], "FIFA 24")
        self.assertEqual(joc["preu"], 69.99)
  
  
  
  
      
# TESTS PER A TASCA ESCRITA 02

class TestProvaEscrita02(unittest.TestCase):
    """
    Tests unitaris per a la Prova Escrita 02.
    Exercicis: 1 (crear_sequencia), 2 (numeros_imparells_majors),
                3 (primera_posicio), 4 (diagonal_principal)
    """

    # ----- Exercici 1 -----
    def test_crear_sequencia_valida(self):
        """Comprova la creació d'una seqüència vàlida."""
        resultat = tascaescrita2.crear_sequencia(5, 10)
        self.assertEqual(resultat, [5, 6, 7, 8, 9, 10])

    def test_crear_sequencia_invalida(self):
        """Comprova que retorna llista buida si inici >= final o negatiu."""
        self.assertEqual(tascaescrita2.crear_sequencia(10, 5), [])
        self.assertEqual(tascaescrita2.crear_sequencia(-2, 5), [])

    # ----- Exercici 2 -----
    def test_numeros_imparells_majors_valids(self):
        """Comprova que retorna només imparells majors que limit."""
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        resultat = tascaescrita2.numeros_imparells_majors(llista, 3)
        self.assertEqual(resultat, [7, 9, 7])

    def test_numeros_imparells_majors_invalids(self):
        """Comprova llista buida si la llista és buida o limit no enter."""
        self.assertEqual(tascaescrita2.numeros_imparells_majors([], 3), [])

    # ----- Exercici 3 -----
    def test_primera_posicio_present(self):
        """Comprova la posició de la primera aparició d'un element existent."""
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(tascaescrita2.primera_posicio(llista, 7), 2)

    def test_primera_posicio_inexistent(self):
        """Comprova que retorna -1 si l'element no existeix."""
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(tascaescrita2.primera_posicio(llista, 15), -1)

    def test_primera_posicio_llista_buida(self):
        """Comprova que retorna -1 si la llista està buida."""
        self.assertEqual(tascaescrita2.primera_posicio([], 5), -1)

    # ----- Exercici 4 -----
    def test_diagonal_principal_quadrada(self):
        """Comprova la diagonal d'una matriu quadrada vàlida."""
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(tascaescrita2.diagonal_principal(matriu), [1,5,9])

    def test_diagonal_principal_no_quadrada(self):
        """Comprova que retorna llista buida si la matriu no és quadrada."""
        matriu = [[1,2],[3,4,5]]
        self.assertEqual(tascaescrita2.diagonal_principal(matriu), [])

    def test_diagonal_principal_invalid(self):
        """Comprova que retorna llista buida si la matriu és invàlida."""
        self.assertEqual(tascaescrita2.diagonal_principal([]), [])
        self.assertEqual(tascaescrita2.diagonal_principal([[1,2],[3]]), [])



# EXECUCIÓ DELS TESTS
if __name__ == "__main__":
    unittest.main()




