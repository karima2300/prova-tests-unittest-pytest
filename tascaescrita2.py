
def crear_sequencia(inici, final):
    """
    Genera una llista amb tots els números entre inici i final (inclosos).

    Valida que inici i final siguin enters positius i que inici sigui
    menor que final. Si no es compleix, retorna una llista buida.

    Args:
        inici (int): Valor inicial.
        final (int): Valor final.

    Returns:
        list: Llista de nombres o llista buida si no és vàlid.
    """
    llista = []
    if isinstance(inici, int) and isinstance(final, int) and inici < final and inici >= 0:
        llista = [i for i in range(inici, final + 1)]
    return llista


def numeros_imparells_majors(llista, limit):
    """
    Retorna una nova llista amb els números imparells majors que limit.

    Valida que llista sigui una llista no buida i que limit sigui un enter.
    Si no es compleix, retorna una llista buida.

    Args:
        llista (list): Llista de nombres.
        limit (int): Valor límit.

    Returns:
        list: Llista de números imparells majors que limit.
    """
    resultat = []
    if isinstance(llista, list) and isinstance(limit, int) and llista:
        resultat = [i for i in llista if i % 2 != 0 and i > limit]
    return resultat


def primera_posicio(llista, element):
    """
    Retorna la posició de la primera aparició d'un element a la llista.

    Si l'element no existeix, retorna -1.
    No utilitza el mètode index().

    Args:
        llista (list): Llista on buscar.
        element: Element a buscar.

    Returns:
        int: Posició de la primera aparició o -1.
    """
    for i in range(len(llista)):
        if llista[i] == element:
            return i
    return -1


def diagonal_principal(matriu):
    """
    Retorna la diagonal principal d'una matriu quadrada.

    Valida que sigui una llista de llistes no buida, que totes les files
    tinguin la mateixa longitud i que la matriu sigui quadrada.
    Si no es compleix, retorna una llista buida.

    Args:
        matriu (list): Matriu quadrada.

    Returns:
        list: Llista amb els elements de la diagonal principal.
    """
    if not isinstance(matriu, list) or not matriu:
        return []

    if not all(isinstance(fila, list) for fila in matriu):
        return []

    if not all(len(fila) == len(matriu) for fila in matriu):
        return []

    diagonal = []
    for i in range(len(matriu)):
        diagonal.append(matriu[i][i])

    return diagonal
