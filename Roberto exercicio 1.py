# velocidade = int(input("Qual a velocidade:"))
# if velocidade>125


#     print("Você foi multado em: R$ ",(velocidade-110)*5)
# else:
#     print("Você não foi multado")

def multa_excesso_velocidade(velocidade):
    if velocidade <= 110:
        return 0
    if velocidade > 110:
        return ((velocidade - 110) * 5)





print(multa_excesso_velocidade(109))
print(multa_excesso_velocidade(110))
print(multa_excesso_velocidade(150))