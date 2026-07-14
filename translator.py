# Simple Translator

translator = {
    "hello": "سلام",
    "good": "اچھا",
    "book": "کتاب",
    "school": "اسکول",
    "cat": "بلی"
}

word = input("Enter an English word: ").lower()

if word in translator:
    print("Urdu Meaning:", translator[word])
else:
    print("Sorry, word not found.")