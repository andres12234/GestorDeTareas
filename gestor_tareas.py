import json

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "incompleta"

    def marcar_como_en_proceso(self):
        self.estado = "en proceso"

    def marcar_completada(self):
        self.estado = "completa"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        nueva_tarea = Tarea(descripcion, prioridad)
        self.tareas.append(nueva_tarea)

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        for i, tarea in enumerate(self.tareas):
            print(f"{i}. {tarea.descripcion} ({tarea.prioridad}) - {tarea.estado}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
        else:
            print("Índice inválido")

    def marcar_en_proceso(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_como_en_proceso()
        else:
            print("Índice inválido")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
        else:
            print("Índice inválido")

    def guardar_tareas(self, archivo="GestorDeTareas/tareas.json"):
        with open(archivo, "w", encoding="utf-8") as f:
            datos = [
                {
                    "descripcion": t.descripcion,
                    "prioridad": t.prioridad,
                    "estado": t.estado
                } for t in self.tareas
            ]
            json.dump(datos, f, indent=4)

    def cargar_tareas(self, archivo="GestorDeTareas/tareas.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.tareas = [Tarea(d["descripcion"], d["prioridad"]) for d in datos]
                for i, t in enumerate(datos):
                    self.tareas[i].estado = t["estado"]
        except FileNotFoundError:
            print("No hay tareas guardadas.")


# --- Programa principal con menú interactivo ---
gestor = GestorTareas()
gestor.cargar_tareas()

while True:
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como en proceso")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir y guardar")

    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        descripcion = input("Descripción de la tarea: ")
        prioridad = input("Prioridad (alta/media/baja): ")
        gestor.agregar_tarea(descripcion, prioridad)

    elif opcion == "2":
        gestor.listar_tareas()

    elif opcion == "3":
        gestor.listar_tareas()
        indice = int(input("Índice de la tarea a marcar en proceso: "))
        gestor.marcar_en_proceso(indice)

    elif opcion == "4":
        gestor.listar_tareas()
        indice = int(input("Índice de la tarea a marcar como completada: "))
        gestor.marcar_completada(indice)

    elif opcion == "5":
        gestor.listar_tareas()
        indice = int(input("Índice de la tarea a eliminar: "))
        gestor.eliminar_tarea(indice)

    elif opcion == "6":
        gestor.guardar_tareas()
        print("Tareas guardadas. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
