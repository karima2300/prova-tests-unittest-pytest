videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {
            "nom": "Nintendo",
            "pais": "Japó"
        },
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {
            "nom": "CD Projekt Red",
            "pais": "Polònia"
        },
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {
            "nom": "EA Sports",
            "pais": "Estats Units"
        },
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []


def buscar_per_titol(titol, videojocs):
    """
    Busca un videojoc pel seu títol (insensible a majúscules).

    Args:
        titol (str): Títol del videojoc a buscar.
        videojocs (list): Llista de videojocs.

    Returns:
        dict or None: Diccionari del videojoc o None si no es troba.
    """
    for joc in videojocs:
        if joc["titol"].upper() == titol.upper():
            return joc
    return None


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    """
    Afegeix un videojoc a la biblioteca personal si existeix i no està repetit.

    Args:
        titol (str): Títol del videojoc.
        videojocs (list): Llista de videojocs disponibles.
        biblioteca (list): Biblioteca personal.

    Returns:
        str: Missatge indicant el resultat de l'operació.
    """
    joc = buscar_per_titol(titol, videojocs)

    if joc is None:
        return "❌ Joc no trobat"

    if joc in biblioteca:
        return "⚠️ Ja està a la biblioteca"

    biblioteca.append(joc)
    return "✅ Joc afegit!"


def joc_mes_car(videojocs):
    """
    Retorna el videojoc amb el preu més alt.

    Args:
        videojocs (list): Llista de videojocs.

    Returns:
        dict: Videojoc amb el preu més alt.
    """
    joc_mes_car = videojocs[0]

    for joc in videojocs:
        if joc["preu"] > joc_mes_car["preu"]:
            joc_mes_car = joc

    return joc_mes_car
