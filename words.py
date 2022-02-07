Input = '6\nbarco\ncasa\nbarco\nperro\nlote\nlote\nperro'

Lines = Input.split('\n')

Uniques = []
for x in Lines[1:len(Lines)]:
    if (x not in Uniques):
        Uniques.append(x)

Conteo = []

for x in Uniques:
    Conteo.append( str ( Lines[1:len(Lines)].count(x) ) )

Salida = str(len(Uniques)) + '\n'
for x in Conteo:
    Salida += x + ' '

print(Salida)
