texto = """

O rato roeu a roupa do rei de Roma

"""
#qnts vezes aparecem as vogais no texto?
vogal = 0
for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal += 1

print('total de vogais: {}'.format(vogal))

#quanas vezes a consoante R aparece no texto?
erres = 0

for caractere in texto:
    if 'r' in caractere.lower():
        erres += 1

print('total de R: {}'.format(erres))