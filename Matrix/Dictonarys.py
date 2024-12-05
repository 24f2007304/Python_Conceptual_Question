malg ="It was Monday morning. Swaminathan was reluctant to open his eyes. he considered Monday specially unpleasant in the calendar. After the delicious freedom of Saturday and Sunday, it was difficult to get into the Monday mood of work and discipline. He shuddered at the very thought of school: the dismal yellow building; the fire-eyed Vedanayagam, his class teacher, and headmaster with his"
malg = malg.split() # Here we are  going to be Splite The Paragraph into Wordes
malgudi = list(malg)# Creating a List
s = set(malgudi)# Creating s Sets that is not contaning Dublicates Values
d = {} # Empty Dictonaries   
for x in s:
    d[x] = 0 # Assigning the value to the Dictionare

max =0 # The no times the wordes are repeted
answer_word = "" # Here we assign the max frequency word

for x in malgudi:
    d[x] = d[x] + 1 # Keeps incr the value while the same word on going to malgudi list
    if(d[x]>max): # Keeps changing  the max value
        max = d[x]
        answer_word = x # Keeps changing on max will changing
print(max) 
print(f'The maximum frequency of {answer_word} is {max}')
print(d)
print(len(malgudi))

