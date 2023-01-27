import random # Random for å lage random sannsynligheter
import time # importerer time for å bruke sleep funksjon senere i koden

# Lager klasse monster
class Monster:
    def __init__(self):
        self.navn = str
        self.helse = int
        self.styrke = int
    # Her definerer jeg alle monsterne som kommer i spillet, med verdier i styrke og helse. 
    def monstre(self):
        monster_typer = {
            'Boros': [100000, 456760],
            'Dragen Eragon': [3000, 786],
            'Rotte': [60, 8],
            'Goblin': [250, 35],
        }
        # gir random monster
        self.navn = random.choice(list(monster_typer))
        stats = monster_typer.get(self.navn)
        self.helse = stats[0]
        self.styrke = stats[1]

# Klasse for spiller, bruker bare en spiller i dette spillet
class Spiller:
    def __init__(self):
        self.navn = str
        self.helse = 1000000
        self.styrke = 1000000000 

# Intor scenen, med valgmulighter
def introScene():
  directions = ["venstre","høyre","fram"]
  print("Hvilken vei tar du?")
  userInput = ""
  while userInput not in directions:
    print("Muligheter: venstre/høyre/fram")
    userInput = input()
    if userInput == "venstre":
      skikkelse() 
    elif userInput == "høyre":
      vill_mann()
    elif userInput == "fram":
      vill_mann()
    else: 
      print("Vennligst velg en av mulighetene.")

# En annen scene som sier du gikk feil vei og sender deg tilbake til intro scenen
def vill_mann():
  print("Oisann, det viser seg at du gikk deg vill og endte opp på samme sted")
  time.sleep(1.5)
  introScene()

# En til scene som gir deg andre valgmuligheter
def skikkelse(): #Venstret valget ditt
    directions = ["fram","tilbake"]
    print("Du ser en skummel skikkelse i mørket foran deg. Du blir redd. Hvilken vei går du?")
    userInput = ""
    while userInput not in directions:
        print("Options: fram/tilbake")
        userInput = input()
        if userInput == "fram":
            kamp() #
        elif userInput == "tilbake":
            introScene()
        else:
            print("Ikke et alternativ.")

# Når du møter monsteret, en form får en scene
def kamp():

    monster = Monster()
    monster.monstre()
    # Utifra random monster vi fikk hvis det er Rotte eller Goblin skjer det her
    if monster.navn == ('Rotte', 'Goblin'):
        print(f'En {monster.navn} har dukket opp!')
    else:
        print(f'En {monster.navn} har dukket opp!')
    time.sleep(1)
    print(f' {monster.navn} har {monster.helse} HP, '
          f'og {monster.styrke} styrke')
    print('Monstre blir sinna og gjør seg klar for å slå tilbake!')

    # Sjekker helse til monsteret og fortsetter i tur basert spill til en av dere har null helse

    while True:
        if monster.helse <= 0:
            print('Du har nedkjempet monsteret!')
            time.sleep(1)
            print("Du har vunnet One-Punch-Man simulator, Gratulerer!")
            del monster
            break
        print('Hva vil du gjøre?')
        print('Muligheter: Punch monster [punch]')
        user_input = input()
        if user_input == 'punch':
            # Sannsynlighet for å få en sykdom 10% sjanse
            sykdom = random.randint(1, 10)
            # Får kreft og dør i spillet
            if sykdom == 1:
              print("Før du fikk Punchet så stivnet armen din, pustingen ble tung... du døde du av hjerteinfarkt")
              print("Game Over")
              break
            else:
              pass
            print('ONE PUNCH!!')
            monster.helse -= spiller.styrke
            spiller.helse -= monster.styrke
            if monster.helse <= 0:
                pass
            else:
              print(f'Monsteret har {monster.helse} HP igjen')
              print(f'Du har {spiller.helse} HP igjen')
        else:
          print("Ikke en mulighet")


# Her koden faktisk starter i konsollen og tar i bruk alle funkjsonene
#Sleep blir brukt for å gi litt delay i print outputsa
print("Hei velkommen til One Punch Man simulator!")
time.sleep(1.5) 
print("Etter å ha vært svak hele livet ditt velger du å trene, og etter at du har løpt 10km tatt 100 squats og 100 push ups så har du blitt sterk")
time.sleep(2)
print("Men plutselig befinner du deg fortapt i en skog")
time.sleep(2)
print("Du kan velge å gå i flere retninger for å komme deg ut")
time.sleep(2)
print("La oss starte med hva du heter: ")
navn = input()
spiller = Spiller()
spiller.navn = navn
print("Lykke til, " +navn+ ".")
introScene()