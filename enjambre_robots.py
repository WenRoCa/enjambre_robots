"""
Hecho por : Rocha Cantu Nidia Wendoly  Fecha: 22  de Marzo 2026
Clase: Inteligencia artificial y su ética - Tema 4.6 Robotica - Actividad 27
MIA - Intituto Tecnológico de Nuevo Laredo - Prof. Carlos Arturo Guerrero Crespo
Titulo: Simulador de Enjambre de Robots
Descripción:
Proyecto de Inteligencia Artificial y Robótica que simula un 
enjambre de robots para búsqueda y rescate.
Los robots colaboran, se comunican y optimizan 
la cobertura del área de manera colectiva.
"""
# =========================
# CLASE BASE
# =========================
class RobotEnjambre:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo  # símbolo que representa al robot en la grilla
        self.mensajes = []
        self.celdas_exploradas = set()
        self.energia = 100  # porcentaje de energía

    def navegar_a_destino(self, x, y):
        # Simula navegación a un punto
        print(f"{self.nombre} navegando a ({x}, {y})")
        return True

    def explorar_celda(self, x, y, grilla):
        # Explora la celda y la marca en la grilla
        if (x, y) in self.celdas_exploradas:
            print(f"{self.nombre}: Celda ({x}, {y}) ya explorada")
            return False

        # Reducir energía por exploración
        self.energia -= 1
        if self.energia <= 0:
            print(f"{self.nombre} sin energía, no puede explorar más")
            return False

        self.celdas_exploradas.add((x, y))
        grilla[y][x] = self.simbolo
        mensaje = f"{self.nombre} exploró celda ({x}, {y})"
        self.mensajes.append(mensaje)
        print(mensaje)
        return True

    def comunicar(self, otros_robots):
        # Envía mensajes a todos los robots del enjambre
        for robot in otros_robots:
            if robot != self:
                robot.mensajes.extend(self.mensajes)


# =========================
# FUNCIÓN PARA IMPRIMIR GRILLA
# =========================
def mostrar_grilla(grilla):
    print("\nGrilla de Exploración:")
    for fila in grilla:
        print(" ".join(fila))
    print()


# =========================
# MAIN - SIMULACIÓN DEL ENJAMBRE
# =========================
if __name__ == "__main__":
    # Configuración de la grilla
    ancho, alto = 5, 5
    grilla = [["." for _ in range(ancho)] for _ in range(alto)]

    # Crear robots
    robot1 = RobotEnjambre("R1", "A")
    robot2 = RobotEnjambre("R2", "B")
    robot3 = RobotEnjambre("R3", "C")
    enjambre = [robot1, robot2, robot3]

    # Simular exploración de grilla
    for y in range(alto):
        for x in range(ancho):
            for robot in enjambre:
                if robot.navegar_a_destino(x, y):
                    robot.explorar_celda(x, y, grilla)

    # Mostrar grilla final
    mostrar_grilla(grilla)

    # Comunicación entre robots
    for robot in enjambre:
        robot.comunicar(enjambre)

    # =========================
    # RESUMEN FINAL
    # =========================
    print("=== Resumen de cada Robot ===")
    print(f"{'Robot':<5} | {'Celdas exploradas':<18} | {'Energía restante':<16} | {'Mensajes enviados'}")
    print("-"*70)
    for robot in enjambre:
        print(f"{robot.nombre:<5} | {len(robot.celdas_exploradas):<18} | {robot.energia:<16} | {len(robot.mensajes)}")