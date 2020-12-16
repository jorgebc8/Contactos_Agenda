import csv
def alphabetic_order():
    my_order = []
    my_row = []
    with open('contacts_list.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            name = str(row[0])
            phone = str(row[1])
            email = str(row[2])
            my_row = [name, phone, email]
            my_order.append(my_row)
    alphabetic_order_list = ordenamiento_por_mezcla(my_order)
    return alphabetic_order_list


def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[: medio]
        derecha = lista[medio:]

        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        i = 0
        j = 0

        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = derecha[j]
                j += 1
            else:
                lista[k] = izquierda[i]
                i += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista