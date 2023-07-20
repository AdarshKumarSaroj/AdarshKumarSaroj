import os
import random
import time
import shutil
import keyboard

# os.startfile('C:/Users/SATYAM/Desktop/School/background_music.mp3')
def typing(text, base_typing_speed, pause_chance, min_pause_duration, max_pause_duration):
    for char in text:
        print(char, end='', flush=True)
        typing_speed = base_typing_speed + random.uniform(-0.02, 0.02)  
        time.sleep(typing_speed)

        if random.random() < pause_chance: 
            pause_duration = random.uniform(min_pause_duration, max_pause_duration)
            time.sleep(pause_duration)

typing_speed = 0.05 
pause_chance = 0.01  
min_pause_duration = 0.0005  
max_pause_duration = 0.005  

def human_typing(text):
    typing(text,typing_speed,pause_chance,min_pause_duration,max_pause_duration)





end_delay = 0  #set delay by your own
time.sleep(end_delay)

def print_right(word):
        columns = shutil.get_terminal_size().columns
        padding = " " * (columns - len(word))
        print(padding + word)
        time.sleep(0.1)
        
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


questions = [
    Question("What is the capital of India?",
             ["Mumbai", "Delhi", "Kolkata", "Chennai"],
             "B"),
    Question("Which river is known as the 'Ganga of the South'?",
             ["Godavari", "Krishna", "Narmada", "Kaveri"],
             "D"),
    Question("Which city is famous for the Golden Temple?",
             ["Amritsar", "Varanasi", "Jaipur", "Agra"],
             "A"),
    Question("Who wrote the Indian national anthem, 'Jana Gana Mana'?",
             ["Subhash Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Rabindranath Tagore"],
             "D"),
    Question("Which method is used to add values in List ?",
             ["Index", "Append", "Update", "sort"],
             "B"),
    Question("'OS' computer abbreviation usually means ?",
             ["Order of Significance", "Open Software", "Operating System", "Optical Sensor"],
             "C"),
    Question("CD-ROM stands for ?",
             ["Compactable Read Only Memory", "Compact Data Read Only Memory", "Compactable Disk Read Only Memory", "Compact Disk Read Only Memory"],
             "D"),
    Question("Who Invented First Computer And when ?",
             ["Reynold Johnson in 1723", "Charles Babbage in 1822", "Herman Hollerith in 1732", "Konrad Zuse in 1798"],
             "b"),
    Question("The Computer or Server on the Interet is Also Known as ?",
             ["PC", "Host", "Browser", "Client"],
             "B"),
    Question("In HTTPS, \'S\' means ?",
             ["Secure", "Software", "Secret", "socket"],
             "A"),
    Question("Secure data transmission means ?",
             ["Data can be accessed by any unauthorized person during transmission.", "Data can not be accessed by any unauthorized person during transmission", "Transmission of data", "None of the above"],
             "B"),
    Question("Which of the following techniques can be used for security of data ?",
             ["Authentication", "Authorisation", "Encryption", "All of the above"],
             "C")
             
]



def display_question(question):
    clear_terminal()
    print_score()
    print()
    print()
    print_centered(question.prompt)
    print()
    print()
    for i, option in enumerate(question.options):
        print(f"{chr(65 + i)}. {option}")
        print()
    print()
    if keyboard.read_key()=="n":
        display_question()
    time.sleep(0.1)






def print_centered(text):
    columns = os.get_terminal_size().columns
    print(text.center(columns))

def print_score():
    print_right(f"Score: {score}/{len(questions)}")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Initialize global variables
score = 0
current_question = 0

def get_answer():
    answer = input("Enter your answer: ").upper()
    handle_answer(answer)


def handle_answer(answer):
    global score, current_question
    if answer == questions[current_question].answer:
        print()
        human_typing("Correct answer!\n")
        time.sleep(1)
        score += 1

    else:
        print()
        human_typing("Wrong answer!\n")
        time.sleep(1)
        print()
        human_typing((f"Correct answer is {questions[current_question].answer}\n"))
        time.sleep(1)




    current_question += 1
    if current_question < len(questions):
        display_question(questions[current_question])
    else:
        finish_quiz()


def finish_quiz():
    time.sleep(1)
    clear_terminal()
    print()
    print()
    print()
    print()
    print_centered("Well done! You have completed the quiz")
    print()
    print()
    print_centered(f"Your score: {score} out of {len(questions)}")
    print()
    print()
    
    g = score
    Score = int(g)
    I = (len(questions) - 5)
    if Score > I:
        print_centered('Excellent')
    else:
        print_centered('Very bad result')
    time.sleep(5)


for question in questions:
    display_question(question)
    get_answer()

if keyboard.read_key()=="n":
    display_question()