def descobrir_interruptores():
    print("1. Ligue o interruptor 1.")
    input("Aperte Enter quando estiver pronto para continuar...")

    print("2. Desligue o interruptor 1 e ligue o interruptor 2.")
    input("Aperte Enter quando estiver pronto para continuar...")

    estado_lampada = input("Entre na sala das lâmpadas. A lâmpada está acesa? (s/n): ")

    if estado_lampada.lower() == 's':
        print("O interruptor 2 controla a lâmpada.")
    else:
        temperatura = input("A lâmpada está fria ao toque? (s/n): ")
        if temperatura.lower() == 's':
            print("O interruptor 1 controla a lâmpada.")
        else:
            print("O interruptor 3 controla a lâmpada.")

descobrir_interruptores()
