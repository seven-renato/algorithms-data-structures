"""
Type	Immutable?
int	      Yes
float	  Yes
bool	  Yes
complex	  Yes
tuple	  Yes
frozenset Yes
str	      Yes
list	  No
set	      No
dict	  No

"""

"""
23)
a) Sim, são os mesmo endereços dado que apontam ao mesmo valor.
b) Dado que o valor de x foi alterado, tende-se a perceber que y tende a se manter apontando ao mesmo local, entretanto
o endereço de de x será apresentado com o valor alterado. Entendido que int's são valores imutaveis ou seja, alteram-se e apontam-se a cada novos valores!
Lista são mutável e int é imutável.

"""
x = 10
y = 10
print("x = ", x, "\n")
print("1o print - Endereço de x", id(x))
print("2o print - Endereço de y", id(y))
x -= 1
print("x = ", x, "\n")
print(x)
print("3o print - Endereço de x", id(x))
print("3o print - Endereço de y", id(y))
print("---"*30)

"""
24)
Não, dado que a string se trata de um tipo de dado imutavel ou seja a cada troca infere num novo apontamento para outra posição.
"""

str = "Algoritmo e Estrutura de "
print(str)
print("1o print - Endereço de str", id(str))
str += "Dados"
print(str)
print("2o print - Endereço de str", id(str))
print("---"*30)

'''
26)
Não, para resolver utilizaria o conceito de listas ou acrescentaria na própria variável cont.
Qual a melhor forma?
'''
#Por cont
def step(x,value):
    x = x + value
    print("2o print - Endereço de x", id(x))
cont = 0
print("1o print - Endereço de cont", id(cont))
while cont < 10:
    step(cont,1)
    cont += 1
print("3o print - Endereço de cont", id(cont))
print(cont)
#Por listas
def step(x,value):
    x[0] = x[0] + value
    print("2o print - Endereço de x", id(x))
cont = [0]
print("1o print - Endereço de cont", id(cont))
while cont[0] < 10:
    step(cont,1)
print("3o print - Endereço de cont", id(cont))
print(cont)