while True:
    # etapa 1
    nome  =  input("Digite seu nome: ")
    if not all(c.isalpha() or c.isspace() for c in nome) or nome.strip() == "":
        print("\n Erro! O nome deve conter apenas letras e não pode estar vazio.\n")
        continue
    
    print(f"Seja bem vindo, {nome}!")
    # etapa 1
    
    idade = input("Digite sua idade: ")
    if not all(c.isdigit() or c.isspace() for c in idade) or idade.strip() == "":
        print("Erro! idade inválida.\n")
        continue
    
    # etapa 2
    print("\nDeseja permitir consentimento do uso de seus dados pessoais para análises estatísticas?")
    print("1 - Sim, prosseguir")
    print("2 - Não")
    resposta = input("Resposta: ")
    
    if resposta == "1":
    #etapa 3
        print("""    
        Tecnologia da Informação (TI) é a área responsável por gerenciar recursos 
        tecnológicos usados para processar, armazenar, proteger e transmitir informações. 
        Envolve o uso de computadores, redes, softwares e sistemas digitais para 
        automatizar tarefas, facilitar a comunicação e apoiar a tomada de decisões em 
        empresas, instituições e na vida cotidiana. Presente em praticamente todos os 
        setores da sociedade, a TI é fundamental para a inovação, a eficiência e o 
        desenvolvimento no mundo moderno.
        """)
        
        print("Deseja prosseguir?")
        print("1 - Sim, prosseguir")
        resposta = input("Resposta: ")
    else:
        continue # retorna a etapa 1
    while resposta == "1":
    
    #etapa 4
        print("Escolha entre essas duas formas de representação de algoritmos: ")
        print("1 - Pseudocódigo")
        print("2 - Fluxograma")
        respostaAlgoritmo = input("Resposta: ")
        
        if respostaAlgoritmo == "1":
            
            print("""
            
            O pseudocódigo é uma forma textual e simplificada de descrever os passos de um
            algoritmo,usando uma linguagem parecida com a programação, mas sem regras 
            rígidas de sintaxe. Ele é útil para planejar a lógica de um programa antes de 
            escrever o código em uma linguagem específica.
            
            Exemplo:
            Início
                Escreva "Digite o primeiro número:"
                Leia num1
                Escreva "Digite o segundo número:"
                Leia num2
                soma ← num1 + num2
                Escreva "A soma é:", soma
            Fim
            """)
            
        elif respostaAlgoritmo == "2":
            print("""
            
            O fluxograma é uma representação gráfica de um algoritmo.
            Ele usa símbolospadronizados para 
            mostrar a sequência de ações e decisões.

            Principais símbolos:
            
            Elipse: início ou fim do algoritmo
            Retângulo: processo (cálculo, atribuição)
            Paralelogramo: entrada ou saída de dados
            Losango: decisão (condição com “sim” ou “não”)
            
            Exemplo:
            
            [Início]
                ↓
           [Leia num1]
                ↓
           [Leia num2]
                ↓
      [soma ← num1 + num2]
                ↓
          [Escreva soma]
                ↓
              [Fim]
            """)
        else:
                print("Opção inválida. Tente novamente.")
                continue
            
        print("1 - Próxima etapa")
        print("2 - Voltar à escolha de algoritmo")
        proxima = input("Resposta: ")

     
        if proxima == "1":
            # Etapa 5
            print("\nDeseja sair do sistema?")
            print("1 - Sim, voltar ao início")
            print("2 - Não, voltar à escolha de algoritmo")
            sair = input("Resposta: ")

            if sair == "1":
                print("\nReiniciando o sistema...\n")
                break  
            
            elif sair == "2":
                continue  # Volta à etapa 4
            else:
                print("Comando inválido. Voltando à escolha de algoritmo.")
                continue

        elif proxima == "2":
            continue  
        else:
            print("Comando inválido. Voltando à escolha.")
            continue
