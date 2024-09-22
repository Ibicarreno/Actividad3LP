option = ""
expenses = []

def add_expense():
    print("Ingrese descripcion del gasto 💵:")
    description_expense = str(input())
    print("Ingrese la categoria del gasto asi: 1. Alimentacion 🥕 2. Servicios 🔦 3. Vivienda 🏡 4. Transporte 🚙: ")
    category_expense = str(input())
    if category_expense == "1":
        category_expense = "Alimentacion"
    elif category_expense == "2":
        category_expense = "Servicios"
    elif category_expense == "3":
        category_expense = "Vivienda"
    elif category_expense == "4":
        category_expense = "Transporte"
    else:
        print("Categoria no valida")
        return
    print("Ingrese el monto del gasto 🫰:")
    try:
        amount_expense = float(input())
    except:
        print("Ingresaste un monto invalido ❌")
        return
    # Agregamos esta data a la lista
    expenses.append({
        "description_expense": description_expense,
        "category_expense": category_expense,
        "amount_expense": amount_expense
    })
    print("Gasto agregado ✅")



def delete_expense():
    if len(expenses) == 0:
        print("No tienes gastos para eliminar 🤨")
    else:
        view_expense()
        print("Cual de esta lista de gastos deseas eliminar ❌:")
        try:
            index_expense = int(input())
        except ValueError:
            print("El valor ingresado no es valido")
            return
        if index_expense >=1:
            try:
                expenses.pop(index_expense-1)
            except IndexError:
                print("El numero de gasto es invalido ❌")
                return

            print("Tu gasto ha sido eliminado ✅")
        else:
            print("El numero de gasto es invalido ❌")


def view_expense():
    if len(expenses) == 0:
        print("No tienes gastos para ver 🤨")
    else:
        print("Estos son tus gastos 💵:")
        for index, expense in enumerate(expenses):
            print(f"✅ Gasto N°{index+1} | Descripcion: {expense["description_expense"]} | Categoria: {expense["category_expense"]} | Monto: {expense["amount_expense"]}")


def view_expense_category():
    print("Para ver el resumen de gastos por categoria, ingresa la categoria asi: 1. Alimentacion 🥕 2. Servicios 🔦 3. Vivienda 🏡 4. Transporte 🚙: ")
    search_category = str(input())
    if search_category == "1":
        search_category = "Alimentacion"
    elif search_category == "2":
        search_category = "Servicios"
    elif search_category == "3":
        search_category = "Vivienda"
    elif search_category == "4":
        search_category = "Transporte"
    else:
        print("Categoria no valida")
        return
    print(f"La categoria seleccionada es {search_category}")
    for index, expense in enumerate(expenses):
        if expense["category_expense"] == search_category:
            print(f"Gasto N° {index+1} de la categoria {search_category}:  | Descripcion: {expense["description_expense"]} | Monto: {expense["amount_expense"]} ")


def calculate_expenses():
    print("El total de tus gastos son 🥕🔦🏡🚙:")
    total_expenses = 0
    for expense in expenses:
        total_expenses += expense["amount_expense"]
    print(f"total {total_expenses}")


while option != "6":
    print("-------Menu opciones App tus gastos🏛️----------")
    print("1. Agregar gasto")
    print("2. Eliminar gasto")
    print("3. Ver gasto")
    print("4. Ver resumen por categoria de gastos")
    print("5. Calcular total de gastos")
    print("6. Salir")
    print("------------------------------------------------")

    option = str(input())

    if option == "1":
        add_expense()
    elif option == "2":
        delete_expense()
    elif option == "3":
        view_expense()
    elif option == "4":
        view_expense_category()
    elif option =="5":
        calculate_expenses()
    else:
        print("Opcion no valida")