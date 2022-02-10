porcentagem = 0
resposta = 0

while True:
    ceu = input('O céu está escuro? (1 - sim // 2 - não)')
    if ceu == "1":
      porcentagem = porcentagem + 10

    if ceu == "2":
      porcentagem = porcentagem

    if ceu != "1" and ceu != "2":
     print("opção inválida!")
     continue

    aspecto = input('O céu apresenta ráios e/ou trovões? (1 - sim // 2 - não)')
    if aspecto == "1":
      porcentagem = porcentagem +30

    if aspecto == "2":
      porcentagem = porcentagem

    if aspecto != "1" and aspecto != "2":
     print("opção inválida!")
     continue

    cheiro = input('O ar cheira a chuva? (1 - sim // 2 - não) ')
    if cheiro == "1":
      porcentagem = porcentagem +20

    if cheiro == "2":
      porcentagem = porcentagem

    if cheiro != "1" and cheiro != "2":
     print("opção inválida!")
     continue

    res = input('deseja saber a previsão? s/n')
    if res == 's':
        print("há",porcentagem,"%","de chances de chover hoje!")
        porcentagem = 0

    if res == "n":
        print("Fechando o programa!")
        break