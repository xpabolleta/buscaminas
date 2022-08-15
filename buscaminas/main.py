from random import randint
from numpy import zeros

TABLA = 0
ILARA = 1
ZUTABEA = 2
MINA_SOBERAN = 3
BANDERA_SOBERAN = 4
BUKAERA = 5

GERUZA_TAPA = 0
GERUZA_MINA = 1
GERUZA_BANDERA = 2
GERUZA_BALIOA = 3

KAR_ITZALITA = '*'
KAR_MINA = 'X'
KAR_BANDERA = '@'

BUKAERA_TXARRA = 1
BUKAERA_ONA = 2

def hasi():
    print('============================================')
    print('        ->  MINA BILATZAILEA  <-')
    print('============================================')
    print('Ongi etorri, jokalari\n')
    print('\nAukeratu zailtasuna:\n')
    print('Erraza: 8 x 8 eta 10 mina      (1)')
    print('Tartekoa: 16 x 16 eta 40 mina  (2)')
    print('Zaila: 16 x 30 eta 99 mina     (3)')
    zailtasuna = int(input('\nSartu zailtasuna: '))
    while (zailtasuna < 1) or (zailtasuna > 4):
        print('\nAukeratutako zailtasuna ez dago hautagai')
        zailtasuna = int(input('Mesedez, aukeratu zailtasuna: '))
    if zailtasuna == 1:
        ilara_kop = 8
        zutabe_kop = 8
        mina_kop = 10
    elif zailtasuna == 2:
        ilara_kop = 16
        zutabe_kop = 16
        mina_kop = 40
    elif zailtasuna == 3:
        ilara_kop = 16
        zutabe_kop = 30
        mina_kop = 99
    tabla = hasi_tabla(ilara_kop,zutabe_kop,mina_kop)
    bandera_kop = mina_kop
    bukaera = 0

    jokua = [tabla,ilara_kop,zutabe_kop,mina_kop,bandera_kop,bukaera]

    return(jokua)

def hasi_tabla (ilara_kop,zutabe_kop,mina_kop):
    tabla = zeros((4,ilara_kop,zutabe_kop), dtype = int)
    for i in range(mina_kop):
        x_rand = randint(0,ilara_kop-1)
        y_rand = randint(0,zutabe_kop-1)
        while tabla[GERUZA_MINA][x_rand][y_rand] == 1:
            x_rand = randint(0,ilara_kop-1)
            y_rand = randint(0,zutabe_kop-1)
        tabla[GERUZA_MINA][x_rand][y_rand] = 1
        for j in range(3):
            for k in range(3):
                if (x_rand-1+j >= 0 and x_rand-1+j < ilara_kop) and (y_rand-1+k >= 0 and y_rand-1+k < zutabe_kop) and not(j==k==1):
                    tabla[GERUZA_BALIOA][x_rand-1+j][y_rand-1+k] += 1
    return(tabla)

def imprimatu_tabla (jokua):
    print('\n--------------------------------------------')
    print('{} bandera dituzu oraindik kokatzeko' .format(jokua[BANDERA_SOBERAN]))
    print(' ',end = '')
    for i in range(jokua[ZUTABEA]):
        print('_', end = ' ')
    print()
    for k in range(jokua[ILARA]):
        print('|', end = '')
        for l in range(jokua[ZUTABEA]):
            if (jokua[BUKAERA] == BUKAERA_TXARRA) and (jokua[TABLA][GERUZA_MINA][k][l] == 1):
                print(KAR_MINA, end = ' ')
            elif(jokua[TABLA][GERUZA_BANDERA][k][l] == 1):
                print(KAR_BANDERA,end = ' ')
            elif(jokua[TABLA][GERUZA_TAPA][k][l] == 0):
                print(KAR_ITZALITA,end = ' ')
            else:
                print(jokua[TABLA][GERUZA_BALIOA][k][l],end = ' ')
        print()
    return(jokua)

def konprobatu_mugimendua(jokua):
    print('Zer egin behar duzu orain?:\n')
    print(' -Bandera bat kokatu   (1)')
    print(' -Kutxatila bat argitu (2)')
    aukera = int(input('\nZure aukera: '))
    while aukera < 1 or aukera > 2:
        print('\nHautatutako aukera ez dago hautagai')
        aukera = int(input('Mesedez, sartu zure aukera: '))
    x_posizioa = int(input('\nSartu ilara zenbakia: '))
    while x_posizioa < 0 or x_posizioa > jokua[ILARA]-1:
        print('\nHautatutako aukera ez dago hautagai')
        x_posizioa = int(input('Mesedez sartu ilara zenbakia: '))
    y_posizioa = int(input('Sartu zutabe zenbakia: '))
    while y_posizioa < 0 or y_posizioa > jokua[ZUTABEA]-1:
        print('\nHautatutako aukera ez dago hautagai')
        y_posizioa = int(input('Mesedez sartu zutabe zenbakia: '))
    if aukera == 1:
        jokua = kokatu_bandera(jokua,x_posizioa,y_posizioa)
        if jokua[MINA_SOBERAN] == 0:
            jokua[BUKAERA] = BUKAERA_ONA
    if aukera == 2:
        jokua = argitu_kutxatila(jokua,x_posizioa,y_posizioa)
        if jokua[TABLA][GERUZA_MINA][x_posizioa][y_posizioa] == 1:
            jokua[BUKAERA] = BUKAERA_TXARRA
    return(jokua)

def kokatu_bandera(jokua,x_posizioa,y_posizioa):
    if jokua[TABLA][GERUZA_BANDERA][x_posizioa][y_posizioa] == 1:
        jokua[TABLA][GERUZA_BANDERA][x_posizioa][y_posizioa] = 0
        if jokua[TABLA][GERUZA_MINA][x_posizioa][y_posizioa] == 1:
            jokua[BANDERA_SOBERAN] += 1
            jokua[MINA_SOBERAN] += 1
        else:
            jokua[BANDERA_SOBERAN] += 1
    else:
        if jokua[BANDERA_SOBERAN] != 0:
            jokua[TABLA][GERUZA_BANDERA][x_posizioa][y_posizioa] = 1
            if jokua[TABLA][GERUZA_MINA][x_posizioa][y_posizioa] == 1:
                jokua[BANDERA_SOBERAN] -= 1
                jokua[MINA_SOBERAN] -= 1
            else:
                jokua[BANDERA_SOBERAN] -= 1
        else:
            print('\nBarkatu, ezin dituzu bandera gehiagorik kokatu')
    return(jokua)

def argitu_kutxatila(jokua,x_posizioa,y_posizioa):
    jokua[TABLA][GERUZA_TAPA][x_posizioa][y_posizioa] = 1
    if jokua[TABLA][GERUZA_MINA][x_posizioa][y_posizioa] == 0 and jokua[TABLA][GERUZA_BANDERA][x_posizioa][y_posizioa] == 0:
        if jokua[TABLA][GERUZA_BALIOA][x_posizioa][y_posizioa] == 0:
            for i in range(3):
                for j in range(3):
                    if (x_posizioa-1+i >= 0 and x_posizioa-1+i < jokua[ILARA]) and (y_posizioa-1+j >= 0 and y_posizioa-1+j < jokua[ZUTABEA]) and not(i==j==1):
                        if jokua[TABLA][GERUZA_TAPA][x_posizioa-1+i][y_posizioa-1+j] == 0:
                            jokua = argitu_kutxatila(jokua,x_posizioa-1+i,y_posizioa-1+j)
    return(jokua)

def main():
    joku_berria = hasi()
    imprimatu_tabla(joku_berria)
    amaitu = 0
    while amaitu == 0:
        joku_berria = imprimatu_tabla(konprobatu_mugimendua(joku_berria))
        amaitu = joku_berria[BUKAERA]
    if amaitu == BUKAERA_ONA:
        print('\n--------------------------------------------')
        print('Partida bukatu da')
        print('Zorionak, irabazi egin duzu :)\n')
    elif amaitu == BUKAERA_TXARRA:
        print('\n--------------------------------------------')
        print('Partida bukatu da')
        print('Galdu egin duzu :(\n')

main()