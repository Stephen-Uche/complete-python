
file = open('csv_data.txt', 'r') #Open the file with 'r' read mode to -

lines = file.readlines() #Read all the lines in the file including the \n

file.close() #Close the file.

#To read the lines and ignoring the first line "lines[1:]"
#To remove the white space and \n "line.strip()"
#Iterate over line in list of lines excluding the first line to strip them.
lines = [line.strip() for line in lines[1:]] 

#Iterate over the strip line
for line in lines:
    #To get the datas on each line which is separated by comas, we split the line with coma
    person_data = line.split(',')

    #Give the datas variables and use built in code to make them uppercase and capitalized
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age} years old, studying {degree} at {university}.')


