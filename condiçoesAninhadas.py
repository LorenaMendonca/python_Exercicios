#Exe36
'''casa = float(input('valor da casa: '))
sala = float(input('salario do comprador: '))
anos = int(input('quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
cor = {'vermelho':'\033[31m', 'verde':'\033[32m'}
print(f'para pagar uma casa de R${casa} em {anos} anos a prestaçao sera de R${prestacao}')
if prestacao > sala * (30 / 100):
    print(f'emprestimo {cor["vermelho"]} negado!')
else:
    print(f'emprestimo {cor["verde"]} aprovado!')'''

#Exe37

'''def conversao(num, opcao):
    num = int('digite um numero inteiro: ')
    print("""ecolha uma das bases para conversao:
    [ 1 ] converter para BINARIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL""")
    cor = {'red':'\033[31m'}
    opcao = int('sua opcao: ')
    if opcao == 1:
        print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
    elif opcao == 2:
        print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
    elif opcao == 3:
        print(f'{num} convertido em HEXADECIMAL é {hex(num)[2:]}')
    else:
        print(f'{cor["red"]} opcao invalida')
resultado = conversao(15, 2)
print(resultado)''' 

#Exe38
'''num1 = float(input('primeiro numero: '))
num2 = float(input('segundo numero: '))
if num1 > num2:
    print('o PRIMEIRO numero é maior')
elif num1 == num2:
    print('os dois valores sao IGUAIS')
else:
    print('o SEGUNDO numero é maior')'''

#Exe39
'''from datetime import date
ano = int(input('ano de nascimento: '))
genero = int(input("""qual é seu genero? 
[1] mulher
[2] homem
"""))
data = date.today().year
idade = data - ano
faltam = 18 - idade
alistamento = faltam + data 
if idade < 18:
    print(f"""quem nasceu em {ano} tem {idade} anos em {data}.
ainda faltam {faltam} anos para o alistamento
seu alistamento sera em {alistamento}""")
elif genero == 1:
    print('vc nao precisa se alistar')
elif idade == 18:
    print(f"""quem nasceu em {ano} tem {idade} anos em {data}.
vc tem que se alistar IMEDIATAMENTE!""")
else:
    print(f"""quem nasceu em {ano} tem {idade} anos em {data}
vc ja deveria ter se alistado ha {idade - 18} anos.
seu alistamento foi em {alistamento}""")'''

#Exe40
'''num1 = float(input('primeira nota: '))
num2 = float(input('segunda nota: '))
media = (num1 + num2) / 2
if media >= 7:
    print(f"""tirando {num1} e {num2}, a media do aluno é {media:.2f}
o aluno esta APROVADO!""")
elif 7 > media >= 5:
    print(f"""tirando {num1} e {num2}, a media do aluno é {media:.2f} 
o aluno esta de RECUPERAÇAO""")
elif media < 5:
    print(f"""tirando {num1} e {num2}, a media do aluno é {media:.2f}
o aluno esta REPROVADO""")'''

#Exe41
'''from datetime import date
nasc = int(input('ano de nascimento: '))
idade = date.today().year - nasc
print(f'o atleta tem {idade} anos')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')'''

#Exe42
'''a = float(input('primeiro numero: '))
b = float(input('segundo numero: '))
c = float(input('terceiro numero: '))
if a < b + c and b < a + c and c < a + b:
    print('o seguimentos acima podem formar um triangulo ', end='') 
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('os seguimentos acima NAO podem formar um triangulo ')''' 

#Exe43
'''peso = float(input('qual é o seu peso:(Kg) '))
alt = float(input('qual é sua altura:(m) '))
imc = peso / (alt**2)
cor = {'red': '\033[31m', 'green':'\033[32m', 'yello':'\033[33m'}
print(f'o IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print(f'{cor["yello"]}abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'{cor["green"]}peso NORMAL')
elif 30 > imc >= 25:
    print(f'{cor["yello"]}SOBREPESO')
elif 30 <= imc < 40:
    print(f'{cor["yello"]}OBESIDADE GRAU 1')
else:
    print(f'{cor["red"]}OBESIDADE MORBIDA')''' 

#Exe44
'''cor = {'red':'\033[31m'}
print(20*'=', 'LOJA', 20*'=')
preco = float(input('preço das compras:R$ '))
print("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao                  
""")
opc = int(input('qual opcao? ')) 
if opc == 1:
   print(f'sua compra é de R${preco} e vai custar R${preco - (preco * 10 / 100)} no final')
elif opc == 2:
   print(f'sua compra é de R${preco} e vai custar R${preco - (preco * 5 / 100)} no final')
elif opc == 3:
   print(f'sua compra sera parcelada em 2x de R${preco / 2} e vai custar R${preco} no final')
elif opc == 4:
   parcelas = int(input('quantas parcelas? '))
   print(f"""sua compra  sera parcelada em {parcelas}x de R${(preco + (preco * 20 / 100)) / parcelas:.2f} COM JUROS 
sua compra de {preco} vai custar R${preco + (preco * 20 / 100)} no final""")
else:
   print(f'{cor["red"]}OPÇÃO INVALIDA')'''

#Exe45
'''from random import randint
from time import sleep
print("""suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
lista = ('pedra', 'papel', 'tesoura')
jogo = int(input('qual é a sua jogada?' ))
computador = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 20)
print(f'o computador jogou {(lista[computador])} e voce {(lista[jogo])}')
print('-=' * 20)
if jogo == computador:
    print('EMPATE')
elif jogo == 0 and computador == 1 or jogo == 1 and computador == 2 or jogo == 2 and computador == 0:
    print('computador venceu')
else:
    print('voce venceu')''' 