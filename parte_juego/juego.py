"""Elementos y Acciones - borrador por terminal (sin graficos ni vision)."""
import random

# Counters validos: lo que la maquina juega -> respuestas que lo vencen
ELEMENTOS = {
    "Volcán": ["Marea", "Vendaval"],
    "Marea": ["Hongo", "Rayo"],
    "Vendaval": ["Marea", "Rayo"],
    "Rayo": ["Volcán", "Hongo"],
    "Hongo": ["Volcán", "Vendaval"],
}
ACCIONES = {
    "Atacar": ["Defender", "Huir"],
    "Defender": ["Curarse", "Cargar"],
    "Curarse": ["Atacar", "Cargar"],
    "Huir": ["Defender", "Curarse"],
    "Cargar": ["Atacar", "Huir"],
}

# Teclas (cada pregunta tiene su propio conjunto, asi que 'h' puede repetirse)
TECLAS_ELEMENTO = {"v": "Volcán", "m": "Marea", "e": "Vendaval", "r": "Rayo", "h": "Hongo"}
TECLAS_ACCION = {"a": "Atacar", "d": "Defender", "c": "Curarse", "h": "Huir", "g": "Cargar"}

VIDAS_INICIALES = 6


def turno_maquina(anterior):
    """Elige elemento y accion al azar, sin repetir la combinacion anterior."""
    while True:
        jugada = (random.choice(list(ELEMENTOS)), random.choice(list(ACCIONES)))
        if jugada != anterior:
            return jugada


def pedir(texto, teclas):
    opciones = ", ".join(f"{k}={v}" for k, v in teclas.items())
    while True:
        t = input(f"{texto} ({opciones}): ").strip().lower()
        if t in teclas:
            return teclas[t]
        print("Tecla no válida.")


def resolver(jugador, maquina):
    """Devuelve (puntos, vidas_perdidas, perfecto)."""
    ok_elem = jugador[0] in ELEMENTOS[maquina[0]]
    ok_acc = jugador[1] in ACCIONES[maquina[1]]
    if ok_elem and ok_acc:
        return 25, 0, True
    if ok_elem or ok_acc:
        return 5, 1, False
    return -10, 2, False


def main():
    vidas, puntos, racha = VIDAS_INICIALES, 0, 0
    anterior = None
    print("=== Elementos y Acciones ===")
    while vidas > 0:
        maquina = turno_maquina(anterior)
        anterior = maquina
        print(f"\nVidas: {vidas}  Puntos: {puntos}  Racha: {racha}")
        print(f"La máquina juega: {maquina[0]} + {maquina[1]}")
        jugador = (pedir("Tu elemento", TECLAS_ELEMENTO), pedir("Tu acción", TECLAS_ACCION))
        pts, perdidas, perfecto = resolver(jugador, maquina)
        puntos = max(0, puntos + pts)
        vidas -= perdidas
        racha = racha + 1 if perfecto else 0
        print(f"Tú: {jugador[0]} + {jugador[1]} -> {pts:+d} puntos, -{perdidas} vidas")
    print(f"\nFin de la partida. Puntuación final: {puntos}")


if __name__ == "__main__":
    main()
