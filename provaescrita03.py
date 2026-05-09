"""
Prova escrita 03
Exercicis 2, 3 i 4 (Exercici 1 eliminat)
"""

# =========================================================
# Exercici 2
# =========================================================

def trobar_edat_maxima(persones):
    """
    Rep una llista de diccionaris amb claus 'nom' (str) i 'edat' (int)
    i retorna l'edat més alta.
    Si la llista és buida o les dades no són vàlides, retorna -1.
    """
    if not isinstance(persones, list) or not persones:
        return -1

    edats = []

    for persona in persones:
        if (
            not isinstance(persona, dict)
            or "nom" not in persona
            or "edat" not in persona
            or not isinstance(persona["edat"], int)
        ):
            return -1

        edats.append(persona["edat"])

    return max(edats)


# =========================================================
# Exercici 3
# =========================================================

productes = [
    {
        'nom': 'Portàtil Dell XPS 15',
        'preu': 1299.99,
        'categoria': 'Informàtica',
        'stock': 5
    },
    {
        'nom': 'Ratolí Logitech MX Master',
        'preu': 89.99,
        'categoria': 'Perifèrics',
        'stock': 15
    },
    {
        'nom': 'Monitor Samsung 27"',
        'preu': 349.50,
        'categoria': 'Monitors',
        'stock': 8
    }
]

def trobar_producte_mes_car():
    """
    Retorna el producte amb el preu més alt de la llista global productes.
    Si la llista està buida, retorna None.
    """
    global productes

    if not productes:
        return None

    producte_mes_car = productes[0]

    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            producte_mes_car = producte

    return producte_mes_car


# =========================================================
# Exercici 4
# =========================================================

def comptar_empleats_per_departament(empresa):
    """
    Rep un diccionari empresa amb una llista de departaments
    i retorna un diccionari amb el nombre d'empleats per departament.
    """
    resultat = {}

    if (
        not isinstance(empresa, dict)
        or "departaments" not in empresa
        or not isinstance(empresa["departaments"], list)
    ):
        return resultat

    for departament in empresa["departaments"]:
        nom = departament.get("nom")
        empleats = departament.get("empleats", [])

        if isinstance(nom, str) and isinstance(empleats, list):
            resultat[nom] = len(empleats)

    return resultat
