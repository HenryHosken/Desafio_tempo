chance_de_chuva = 0 
print('Utilize de "1" para sim e "2" para não: ')
while True:
    dia1 = input ('No domingo choveu ? ')
    if dia1 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia1 == "2":
        chance_de_chuva= chance_de_chuva + 0
    elif dia1 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')
   
    dia2 =input('Na segunda choveu ? ')
    if dia2 == "2":
        chance_de_chuva= chance_de_chuva + 16.6
    elif dia2 == "1":
        chance_de_chuva= chance_de_chuva + 0   
    elif dia2 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')
    
    dia3 = input ('Na terça choveu ? ')
    if dia3 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia3 == "2":
        chance_de_chuva= chance_de_chuva + 0
    elif dia3 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')
    
    dia4 = input ('Na quarta choveu ? ')
    if dia4 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia4 == "2":
        chance_de_chuva= chance_de_chuva + 0
    elif dia4 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')
    
    dia5 = input ('Na quinta choveu ? ')
    if dia5 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia5 == "2":
        chance_de_chuva= chance_de_chuva + 0
    elif dia5 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')
  
    dia6 = input ('Na sexta choveu ? ')
    if dia6 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia6 == "2":
        chance_de_chuva + 0
    elif dia6 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')

    dia7 = input ('O tempo está nublado ? ')
    if dia7 == "1":
        chance_de_chuva= chance_de_chuva + 16.66
    elif dia7 == "2":
        chance_de_chuva + 0
    elif dia7 != "1" and dia1 != "2":
        print('Tente 1 ou 2 por favor')    
    
    print(f'A probabilidade de chover sábado é de {chance_de_chuva}% ')    
    break  