def color_menu():
    print("\n--- Menú de Colores ---")
    print("1. Rojo")
    print("2. Amarillo")
    print("3. Verde")
    print("0. Salir")

    choice = input("Seleccione un boletín: ")

    if choice == '1':
        print("Estoy to Rojo")
    elif choice == '2':
        print("Amarillo, amarillo, amarillo lo platano...")
    elif choice == '3':
        print("Verde, que te voy a poner verde")
    elif choice == '0':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")
