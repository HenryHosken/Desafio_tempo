import random
senha1= random.random()
print(senha1)
senha = input('Digite a senha acima para confirma: ')
if len(senha) < 6:
    print('Senha muito curta')  # Senha muito curta

autenticando_senha = input('Repita a senha: ')
if senha == autenticando_senha:
    print('Senha válida')  # Senha válida  
else:
    print('Senha inválida')
