from random import choice
import string

tamanho_da_senha = int(input("Quantos digitos terá a senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(tamanho_da_senha):
   senha_segura += choice(caracteres)
print("A sua senha é:", senha_segura) 