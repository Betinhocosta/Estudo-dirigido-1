import math

metros_a_pintar = int(input ('qual o tamanho a pintar'))

litros_necessarios = (metros_a_pintar / 6)latas_necessárias = math.ceil (litros_necessarios/18)


#questão A

latas_necessárias = math.ceil (litros_necessarios/18)

print("será necessário:",latas_necessárias)


#questão b)

galoes_necessários= math.ceil (litros_necessarios /3.6)
print("será necessário:", galoes_necessários,"galoes")



#questão c)

latas_necessarias = int(litros_necessarios/18)
faltou = litros_necessarios % 18
galoes_necessarios = math.ceil (faltou / 3.6)

print (" foram necessarios", latas_necessárias,"latas")

