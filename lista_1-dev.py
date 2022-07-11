#!/usr/bin/env python
# coding: utf-8

# 1) Faça uma função que receba um número inteiro e retorne se ele é um número primo ou não.

# In[5]:


### Seu código começa aqui ###
num = int(input('insira um número: '))
cont = 0
for x in range(1, num + 1):
    if num % x == 0:
        cont += 1
    else:
        cont == 0
if cont == 2:
    print(f'{num}, esse número é primo...')
else:
    print(f'{num}, esse número não é primo...')


# 2) Crie uma função que calcule o x da fórmula de Bhaskara.
# 
# A função deverá ter 3 argumentos nomeados como "a", "b" e "c" e retornar o valor do x
# 
# <img src='https://images.educamaisbrasil.com.br/content/banco_de_imagens/guia-de-estudo/D/formula-bhaskara-matematica.jpg' height="100%" width="350" style="margin-left: auto;margin-right: auto">
# 

# In[11]:


### Seu código começa aqui ###
a = int(input('entre com o número correspondente a letra a: '))
b = int(input('entre com o número correspondente a letra b: '))
c = int(input('entre com o número correspondente a letra c: '))

delta = (b**2) - (4 * a * c)
if a == 0:
    print('retornar valor, A não pode ser 0, pois não existiria bhaskara')
elif delta < 0:
    print('não haverá raiz alguma, pois delta < 0')
else:
    x1 = (-b + (delta**0.5)) / 2*a
    x2 = (-b - (delta**0.5)) / 2*a
    
print(f'x1 = {x1} e x2 = {x2} !')


# 3) Novo conceito: **Função Recursiva**
# 
#  Uma função recursiva é aquela que invoca a si mesmo no corpo da função, ou seja, na sequência de códigos que ela
#     executa.
#     
#     Dessa forma, crie uma função recursiva que calcule o fatorial de um número inteiro (n)
#     
#     Dica: fatorial(5) -> 5 * fatorial(4) -> 4 * fatorial (3) ...
# 

# In[19]:


### Seu código começa aqui ###
num = int(input('Entre com qualquer número, iremos descobirir o fatorial dele para você: '))

def fatorial(num):
    if num == 1:
        return num
    else:
        return num * fatorial(num-1)
print(f' o fatorial de {num} é', fatorial(num))


# 4)
# Crie uma lista com as notas da Laís durante o semestre:
# 
# ![image.png](attachment:image.png)
# 
# 

# In[20]:


### Seu código começa aqui ###
notas_lais = [6.7, 4.2, 0, 5, 6.2, 5.4, 5, 10]
print(notas_lais)


# a) Sabendo que a nota final é uma média aritmética entre provas e exercícios, printe se a
# Laís foi aprovada? (média final maior ou igual a 5,0)

# In[27]:


### Seu código começa aqui###
notas_lais = [6.7, 4.2, 0, 5, 6.2, 5.4, 5, 10]
nl = 0

for c in notas_lais:
    nl += c
if nl / (len(notas_lais)) < 5:
    print('reprovada')
else:
    print('aprovada')
print(f'sua média foi de {nl/len(notas_lais)}')


# b) O professor descobriu que a Laís copiou o último exercício de um colega, usando a
# função .pop(), remova o último exercício da lista, recalcule a média e veja se foi
# aprovada?

# In[28]:


### Seu código começa aqui ###
notas_lais = [6.7, 4.2, 0, 5, 6.2, 5.4, 5, 10]
notas_lais.pop(-1)
nl = 0

for c in notas_lais:
    nl += c
if nl / (len(notas_lais)) < 5:
    print('reprovada')
else:
    print('aprovada')
print(f'sua média foi de {nl/len(notas_lais)}')


# c) O professor deu uma chance extra para Laís de fazer um novo exercício, ela tirou 7.5.
# Adicione esse valor na lista de notas e veja se ela foi aprovada.

# In[29]:


### Seu código começa aqui ###
notas_lais = [6.7, 4.2, 0, 5, 6.2, 5.4, 5, 10]
notas_lais.pop(-1)
notas_lais.append(7.5)
nl = 0

for c in notas_lais:
    nl += c
if nl / (len(notas_lais)) < 5:
    print('reprovada')
else:
    print('aprovada')
print(f'sua média foi de {nl/len(notas_lais)}')

