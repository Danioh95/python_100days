student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
with open("nato_phonetic_alphabet.csv") as file:
    file1 = file.readlines()
    file2 = [x.replace("\n", "") for x in file1]
    file3 = [x.split(",") for x in file2]
    file4 = {x:value for (x, value) in file3 if x!="letter"}
    print(file4)

    # file3 = {x:value for (x[0], value[1]) in file2}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("insert the word:\n").upper()
[print(file4[0]) for x in word]