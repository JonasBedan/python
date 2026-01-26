import random

subjects = [
    "Programátor",
    "Student",
    "AI startup founder",
    "Noční hacker",
    "Unavený génius"
]

states = [
    "je totálně vyhořelý",
    "debuguje už 5 hodin",
    "přemýšlí o smyslu života",
    "pije 4. kafe",
    "se snaží pochopit Python"
]

outcomes = [
    "a stejně to rozbije.",
    "a pak to náhodou funguje.",
    "a googlí řešení.",
    "a vzdává to.",
    "a stane se legendou."
]

def load(type):
    if(type == 'sub'):
        try:
            with open("custom_subjects.txt", "r") as f:
                for line in f:
                    subjects.append(line.strip())
        except:
            pass
    elif(type == 'sta'):
        try:
            with open("custom_states.txt", "r") as f:
                for line in f:
                    states.append(line.strip())
        except:
            pass
    elif(type == 'out'):
        try:
            with open("custom_outcomes.txt", "r") as f:
                for line in f:
                    outcomes.append(line.strip())
        except:
            pass


def save(text, type):
    if(type == 'sub'): 
        with open("custom_subjects.txt", "a") as f:
            f.write(text + "\n")
    elif(type == 'sta'): 
        with open("custom_states.txt", "a") as f:
            f.write(text + "\n")
    elif(type == 'out'): 
        with open("custom_outcomes.txt", "a") as f:
            f.write(text + "\n")


load('sub')
load('sta')
load('out')

def generate():
    s = random.choice(subjects)
    st = random.choice(states)
    o = random.choice(outcomes)


    print('here you go:')
    print(s,st,o)
    print(':)')

while True:
    print('vítej v generaci')
    print('1-generuj')
    print('2-přidej vlastní texty')
    print('3-ukonči program')

    c = input('volíš:')

    if c == '1':
        generate()

    elif c == '2':
        while True:
            print('přidej nove texty pro hlasky')
            print('1-subjekta')
            print('2-state')
            print('3-outocme')
            print('Pokud zvolíš cokoliv jiného přidání se ukončí.')

            cc = input('volíš:')

            if cc == '1':
                x = input('kdo bude náš nový subjekt:')
                subjects.append(x)
                save(x, 'sub')
            elif cc == '2':
                x = input('Co bude náš nový state:')
                states.append(x)
                save(x, 'sta')
            elif cc == '3':
                x = input('Co bude náš nový outcome:')
                outcomes.append(x)
                save(x, 'out')
            else:
                break
    elif c == '3':
        break
    else:
        print('nelze provést jakoukoliv akci zkus to znovu')
