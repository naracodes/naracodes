//Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

//Escreva um código que imprima todos os números exceto o número 13. Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

//Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

//Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

for i in range(20,0, -1):
  if(i == 13):
    continue
  print(i)

contador = 21

while(contador > 1):
  contador -= 1
  if(contador == 13):
    continue
  print(contador)
  
  
