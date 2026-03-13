#WRP to create a dictionary of Hindi words and their English translations provide user with an option to look up the English translation of a Hindi word and also to add new Hindi-English word pairs to the dictionary. and can add new Hindi-English word pairs to the dictionary. The program should continue to run until the user decides to exit.

words ={"नमस्ते": "Hello", 
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "माफ़ करें": "Sorry",
    "हाँ": "Yes",
    "नहीं": "No",
    "कैसे हो?": "How are you?",
    "मुझे समझ नहीं आया": "I don't understand",
    "आपका नाम क्या है?": "What is your name?",
    "मेरा नाम ... है": "My name is ...",
    "आप कैसे हैं?": "How are you?",
    "मैं ठीक हूँ": "I am fine",
    "आप कहाँ से हैं?": "Where are you from?",
    "मैं ... से हूँ": "I am from ...",
    "आप क्या करते हैं?": "What do you do?",
    "मैं ... हूँ": "I am a ...",
    "आपका दिन कैसा था?": "How was your day?",
    "मेरा दिन अच्छा था": "My day was good",
    "आपको क्या पसंद है?": "What do you like?",
    "मुझे ... पसंद है": "I like ...",
    "आपको क्या चाहिए?": "What do you want?",
    "मुझे ... चाहिए": "I want ...",
    "आपको क्या चाहिए?": "What do you need?"}

word = input("Enter a Hindi word to look up its English translation (or type 'add' to add a new word, 'exit' to quit): ")
if word in words:
    print(words[word])
elif word == "add":
    hindi_word = input("Enter the Hindi word: ")
    english_word = input("Enter the English translation: ")
    words[hindi_word] = english_word
    print("Word added successfully!")
elif word == "exit":
    print("Exiting the program.")
else:
    print("Word not found in dictionary.")