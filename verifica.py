dizionario: 
{'Giuseppe Gullo': [('campestre', (40, 21, 0), 'Allievi'), ('100mt', (0, 12, 0), 'Juniores mas'), ('200mt', (0, 29, 19), 'Juniores mas'), ('400mt', (0, 40, 34), 'Allievi')], 'Antonia Barbera': [('campestre', (0, 39, 11), 'Juniores fem'), ('100mt', (0, 18, 0), 'Juniores fem'), ('200mt', (0, 0, 0), 'Juniores fem'), ('400mt', (0, 39, 10), 'Allievi')], 'Nicola Esposito': [('campestre', (0, 43, 22), 'Allievi'), ('100mt', (0, 14, 0), 'Juniores mas'), ('200mt', (0, 36, 19), 'Juniores mas'), ('400mt', (0, 40, 10), 'Allievi')], 'Tommaso Fagnani': [('campestre', (30, 11, 0), 'Allievi'), ('100mt', (0, 14, 0), 'Juniores mas'), ('200mt', (0, 31, 19), 'Juniores mas'), ('400mt', (0, 40, 26), 'Allievi')]}

Dati Giuseppe Gullo campestre: 
('campestre', (40, 21, 0), 'Allievi')

Dati Nicola Esposito 200mt: 
Discipilina:  200mt
Tempi:  min:  0 sec:  36 cent:  19
Categoria:  Juniores mas

Tempi Nicola Esposito 100mt: 
Tempi:  min:  0 sec:  18 cent:  0

--tempo minimo 100mt della categoria Juniores mas--
tempo minimo:  12

--tempo minimo 200mt della categoria Juniores mas--
19
tempo minimo: Sec: 29 Cent:  19

--media dei tempi nella corsa campestre della categoria allievi--
CONTATORI
3
4
2
TOTALI
70
75
22
MEDIE
23.333333333333332
17.5
11.0
Media: min:  23.333333333333332 sec:  17.5 cent:  11.0
#10 facoltativo
def leggiChiave():
  nome=input("Inserisci nome :")
  cognome=input("Inserisci cognome :")
  return nome+""+cognome
def leggiDati():
  disciplina=input("Inserisci disciplina :")
  m=int(input("Inserire il  minuti: "))
  s=int(input("Inserire il  secondi: "))
  c=int(input("Inserire il  millesimi: "))
  tempi=(m,s,c)
  categoria=input("Inserisci  categoria: ")
  return[disciplina,tempi,categoria]
def leggiNumeroDiChiavi():
  nChiavi=0
  while (nChiavi)==0:
    nChiavi=int(input("Inserisci il numero di atleti : "))
    if nChiavi==0:
      print("!-devi inserire il numero di -!")
  return nChiavi


def popola():
  nChiavi=leggiNumeroDiChiavi()
  for i in range(nChiavi):
    chiave=leggiChiave()
    if chiave in diz:
      print("contatto già presente!")
      while(chiave in diz):
        chiave=leggiChiave()
        dati=leggiDati()
        diz[chiave]=dati
    else:
      dati=leggiDati()
      diz[chiave]=dati

def tutti():
    print(diz)
    
risp=1
while (risp!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Visualizza tutti')
  risp=int(input('Scegli :'))
  if(risp==1):
    popola()
  elif(risp==2):
    tutti()
  elif(risp==0):
    break  
