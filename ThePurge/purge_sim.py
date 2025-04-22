import random
import os
import time

questions = [
    ("ründa", "A"),
    ("muuda oma asukohta", "A"),
    ("jää siia", "B"),
    ("suurenda gruppi", "B")
]

answers = [
    ["A. ja", "B. ei"],
    ["A. ja", "B. ei"],
    ["A. ja", "B. ei"],
    ["A. ja", "B. ei"]
]

class Player:
    def __init__(self, health, food, energy):
        self.health = health
        self.food = food
        self.energy = energy
        self.time_left = 60
 
    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 10
            print(f"Puhkasid. Uus energia: {self.energy}, toitu jäänud: {self.food}")
        else:
            print("pole piisavalt toitu puhkamiseks")
    
    def status(self):
        print(f"Hetkeseis: Tervis: {self.health}, Toit: {self.food}, Energia: {self.energy}")
    
    def event(self):
        ques_ran = random.randint(0, len(questions) - 1)
        question, correct_answer = questions[ques_ran]
        print(f"\nKüsimus: {question}")
        print(f"Võimalikud vastused: {answers[ques_ran][0]} või {answers[ques_ran][1]}")
        b = input('Sisesta oma vastus (A või B): ')

        if b.strip().upper() != correct_answer:
            self.health -= 1
            print(f"Vale vastus! Elud vähendatud. Uus tervis: {self.health}")
        else:
            x = random.randint(1, 10)
            self.energy += x
            self.food += x
            self.health += x
            print(f"Õige vastus! Saadud boonus: +{x} tervist, +{x} toitu, +{x} energiat")
            self.status()

    def do_turn(self):
        print(f"\nKäik {60 - self.time_left + 1}/60")
        self.status()
        käik = input("\nMida soovid teha?\n1. Puhata (puhkan)\n2. Liikuda (liigun)\n3. Võtta riski (risk)\nSisesta valik: ")
        
        if käik == "puhkan":
            self.rest()
        elif käik == "liigun":
            print("Jätkasid oma teekonda.")
        elif käik == "risk":
            self.event()
        else:
            print("Vale sisend! Proovi uuesti.")

    def play_game(self):
        print("\nTere tulemast mängu!")
        print("Sul on 60 käiku, et ellu jääda.")
        print("Sinu algne seis: 100 tervist, 5 toitu, 60 energiat")
        
        while self.time_left > 0:
            self.do_turn() 
            self.time_left -= 1
            print(f"Aega järgi: {self.time_left} käiku")

        print("\nMäng läbi!")
        self.status()
        print("Tänan mängimast!")

def kontrolli_rest():
    tegelane = Player(health=100, food=5, energy=60)
    tegelane.rest()
    assert tegelane.food == 4, f"VIGA: toit peaks olema 4, aga on {tegelane.food}"
    assert tegelane.energy == 70, f"VIGA: energy peaks olema 70, aga on {tegelane.energy}"
    print("test läbitud")

# Start the game
if __name__ == "__main__":
    player = Player(health=100, food=5, energy=60)
    player.play_game()