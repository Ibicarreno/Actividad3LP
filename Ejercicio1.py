option = ""
tasks = []

# Creamos las funciones


def add_task():
    print("Ingrese el titulo de la tarea ✍️")
    title_task = str(input())
    print("Ingrese la descripción de la tarea 👌")
    description_task = str(input())
    tasks.append({
        "title_task": title_task,
        "description_task": description_task,
        "is_completed": False
    })
    print(f"Se ha creado la tarea N° {len(tasks)} ✅")


def remove_task():
    if len(tasks) == 0:
        print("No tienes tareas para eliminar 🤨")
        return
    else:
        view_tasks()
        print("Que numero de tarea deseas eliminar ☢️:")

        try:
            index_task = int(input())
        except ValueError:
            print("Numero de tarea invalida 🤦‍♂️")
            return

        if index_task >= 1:
            try:
                tasks.pop(index_task - 1)
            except IndexError:
                print("El numero seleccionado de tarea no existe 🧐")
                return
            print(f"Se ha eliminado la tarea N° {index_task}")
        else:
            print("Numero de tarea invalida 🤦‍♂️")


def view_tasks():
    if len(tasks) == 0:
        print("No tienes tareas en tu lista 😒")
    else:
        print("Estas son tus tareas ✍️:")
        for index, task in enumerate(tasks):
            print("")
            print(f"------------Tarea N°{index+1}-------------------")
            print(f"Titulo: {task["title_task"]}")
            print(f"Descripción: {task["description_task"]}")
            print(f"Tarea completada?: {task["is_completed"]}")
            print(f"------------------------------------------------")


def mark_as_completed():
    if len(tasks) == 0:
        print("No tienes tareas para actualizar 🤨")
        return
    else:
        view_tasks()
        print("Que numero de tarea deseas marcar como completada 👍🆗:")

    try:
        index_task = int(input())
    except ValueError:
        print("Numero de tarea invalida 🤦‍♂️")
        return

    if index_task >= 1:
        try:
            tasks[index_task-1]["is_completed"] = True
        except IndexError:
            print("El numero seleccionado de tarea no existe 🧐")
            return
        print(f"Se ha completado la tarea N° {index_task}")
    else:
        print("Numero de tarea invalida 🤦‍♂️")


while option != "5":
    print("------------------------------")
    print("Seleccione una opción: ")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver listado de tareas")
    print("4. Marcar tarea como completada")
    print("5. Salir")
    print("------------------------------")

    option = str(input())

    if option == "1":
        add_task()
    elif option == "2":
        remove_task()
    elif option == "3":
        view_tasks()
    elif option == "4":
        mark_as_completed()
    else:
        print("Opcion invalida")
