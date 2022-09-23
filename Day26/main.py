student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict_from_csv = pandas.read_csv('nato_phonetic_alphabet.csv', header=None, index_col=0, squeeze=True).to_dict()
print(dict_from_csv)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetics():
    user_input = str(input("Enter a word: "))
    try:
        sDict = {x.upper(): dict_from_csv[x.upper()] for x in user_input}
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetics()
    else:
        print(sDict)


generate_phonetics()
