lista = range(1, 1001)
print(list(lista))


letra = input('Digite uma letra: ')
if letra in 'bcdfghjklmnpqrstvwxyz':
   print('É uma vogal')


while True:
 texto = input("Digite uma string: ")

 if texto.isupper():
  print("Tudo maiusculo")
 elif texto.islower():
  print("Tudo minusculo")
 else:
  print("Misturado")
  break

fruta = input('Digite uma fruta: ')
fruta2 = input('Digite outra fruta: ')
fruta3 = input('Digite outra fruta: ')
fruta4 = input('Digite outra fruta: ')
fruta5 = input('Digite outra fruta: ')
fruta_final = input('Verificar se a fruta foi adicionada: ')
list = [fruta, fruta2, fruta3, fruta4, fruta5]
if fruta in list:
    print(f'A fruta {fruta_final} está na lista')
