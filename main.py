import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
# EL -LETTER O .CODE SE REFIERE A LA CSV FILE YA QUE CON PANDAS FUNCIONA COMO SI LAS COLUMNAS FUERAN ATRIBUTOS DE UN OBJETO
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)