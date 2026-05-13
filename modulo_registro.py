def registrar_ticket(tickets, descripcion, prioridad):
    print("hola mundo")
    # Valida que descripcion no esté vacía
    if descripcion == "" or prioridad == "":
        print("Error: Descripción y prioridad son obligatorias.")
        return
    # Genera ID: "T-001", "T-002"...
    numero = len(tickets) + 1
    id_ticket = "T-" + str(numero).zfill(3)

    ticket = {
        "id": id_ticket,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Abierto"
    }
    # Escribe en el diccionario
    tickets.append(ticket)

    print(f"Ticket {id_ticket} registrado con éxito.")