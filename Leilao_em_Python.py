print('digite o lance minimo: ', end="")
lance_minimo = float(input())
print('Vamos começar o leilão com um lance minimo de R$',format(lance_minimo,'.2f'))
nome = ''
maior_participante = ''
maior_oferta = lance_minimo

while(nome != 'n'):
  print('digite seu nome: ', end="")
  nome = str(input())
  print(nome, ", qual o valor do seu lance: ", end="")
  a = float(input())

  if(maior_participante == ''):
    if(a >= maior_oferta):
      maior_oferta = a
      maior_participante = nome
      print('Maior oferta é de',format(maior_oferta,'.2f'),'. Alguem oferece mais? [S/N]')
    else:
      print('alguem oferece mais que o lance minimo? [S/N]')
    
  else:
    if(a > maior_oferta):
      maior_oferta = a
      maior_participante = nome

    print('Maior oferta é de',format(maior_oferta,'.2f'),'. Alguem oferece mais? [S/N]')

  nome = str(input())

print('Dou-lhe uma, dou-lhe duas, dou-lhe tres!')
print('Vendido para ',maior_participante,' por R$',format(maior_oferta,'.2f'))  