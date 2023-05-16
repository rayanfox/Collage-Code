#10-9

#In Case Study 5.5, when the patient addresses the therapist personally, the therapist’s reply does not change persons appropriately. To see an example of this problem, test the program with “you are not a helpful therapist.” Fix this problem by repairing the dictionary of replacements.


replacements = {
    "i'm": "you are",
    "i": "you",
    "me": "you",
    "my": "your",
    "you're": "I am",
    "you": "I",
    "yourself": "myself",
    "am": "are",
    "are": "am",
    "was": "were",
    "were": "was",
    "your": "my",
    "myself": "yourself",
    "i'd": "you would",
    "i've": "you have",
    "you've": "I have",
    "you'd": "I would",
    "you'll": "I will",
    "i'll": "you will",
    "yours": "mine",
    "mine": "yours",
    "you are not": "I am not",
    "you were not": "I was not",
    "you can't": "I can't",
    "you cannot": "I cannot",
    "you are": "I am",
    "you were": "I was",
    "you can": "I can",
    "you will": "I will"
}

def replace_pronouns(message):
    words = message.lower().split()
    for i, word in enumerate(words):
        if word in replacements:
            words[i] = replacements[word]
    return ' '.join(words).capitalize()

def therapist():
    print("Hello, I'm a psychotherapist. What's on your mind?")
    while True:
        message = input("> ")
        if message.lower() == "quit":
            print("Goodbye.")
            break
        else:
            print(replace_pronouns(message))
