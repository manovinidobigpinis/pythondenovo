def CacularMedia():
    soma=0
    for nota in notas:
        soma += nota #soma= soma+nota
    return soma/len(notas)
notas = [ 8, 9, 6]
media = CacularMedia(notas)

if (media >= 7):
    print("aprovado")
elif (media >=5):
    print("Recuperação")
else:
    print("reprovado")