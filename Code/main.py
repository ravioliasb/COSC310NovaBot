import Preprocessor
import Processor
import os
import tkinter
from tkinter import *
from nltk.corpus import wordnet
import Wikipedia_Api
import Wolfram_Api
import NASA_Api


def blockPrint():  # Remove all the printing onto console when chatbot is loading
    sys.stdout = open(os.devnull, 'w')


def enablePrint():  # Restores printing
    sys.stdout = sys.__stdout__


questions, responses = Preprocessor.load_corpus()

bye_synonyms = []
for syn in wordnet.synsets("bye"):
    for word in syn.lemmas():
        bye_synonyms.append(word.name())

print("Booting Up... (this may take a while!)")
blockPrint()
question_list = Processor.vectorizer(questions)
enablePrint()
print("The Chat Bot has loaded.")

window = tkinter.Tk()
# height is false so that we do not lose the fixed bar at the bottom
window.resizable(width=True, height=False)
window.title("Nova, the chatbot")
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
Nova = StringVar()
You = StringVar()
messages = Text(window, width=120, height=20, yscrollcommand=scrollbar.set, wrap=WORD)
messages.config(background="#e6e9f0")
scrollbar.config(command=messages.yview())
messages.pack(anchor='nw', expand=1, fill=BOTH)


def event_enter(key):
    Enter_pressed()


def Enter_pressed():
    input_get = You.get()
    if input_get.lower() in bye_synonyms:
        quit()
    elif input_get.lower() == 'picture of the day':
        messages.insert(END, "You: " + '%s\n' % input_get)
        nasa_response = NASA_Api.apod()
        messages.insert(INSERT, "Nova: " + '%s\n' % nasa_response)
        You.set('')
        messages.see(END)
        return "break"
    elif input_get.lower().split()[0] == 'wikipedia:':
        messages.insert(END, "You: " + '%s\n' % input_get)
        wiki_response = Wikipedia_Api.wikiSearch(input_get)
        messages.insert(INSERT, "Nova: " + '%s\n' % wiki_response)
        You.set('')
        messages.see(END)
        return "break"
    elif input_get.lower().split()[0] == 'wolfram:':
        messages.insert(END, "You: " + '%s\n' % input_get)
        # this gets the response from the Processor.py file and then prints them out
        wolfram_response = Wolfram_Api.wolframSearch(input_get)
        messages.insert(INSERT, "Nova: " + '%s\n' % wolfram_response)
        You.set('')
        messages.see(END)
        return "break"
    else:
        messages.insert(END, "You: " + '%s\n' % input_get)
        # this gets the response from the Processor.py file and then prints them out
        get_response = Processor.process(input_get, question_list, responses)
        messages.insert(INSERT, "Nova: " + '%s\n' % get_response)
        You.set('')
        messages.see(END)
        return "break"


Label(window, text=" user : ").pack(side=LEFT)
Entry(window, textvariable=You, width=10, background="white").pack(side=LEFT, anchor='nw', expand=1, fill=BOTH)
frame = Frame(window)
Button(window, width=10, text="Send", foreground="Black", command=Enter_pressed, relief="flat").pack(side=LEFT)
messages.insert(END,
                "Nova: " + '%s\n' % "Hello. My name is Nova, the astronomy and geography Chat Bot. Pleased to meet you.")
window.bind("<Return>", event_enter)
frame.pack(anchor='nw', expand=1, fill=BOTH)
window.mainloop()
