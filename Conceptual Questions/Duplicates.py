# # Longest Substring Without Repeating Characters: Write a function longest_unique_substring(s) that finds the length of the longest substring without repeating characters.

def longest_unique_substring(Str):
    Str = Str.split(" ")
    max = 0
    MaxWord = ''
    for i in Str:
        if len(i)>max:
            max = len(i)
            MaxWord = i
            
    return MaxWord

print(longest_unique_substring("I am alok Tiwari"))
    
''' We Have to find the maximum length of the Word that is not Repleted as well..'''        


def longest_unique_substring_Without_repetation(Str):
    Str = Str.split(" ")
    Word_Count = {}  # Here we are making a Empty Dictionaries and there will we store Number that how many times Repeted in the String.
    for word in Str: 
        if word in Word_Count:  
            Word_Count[word] +=1    # Here we are incermenting the number  on repeating
        else:
            Word_Count[word] = 1 # Here we Intalising the Key  and Value Pair
   
    Uniqe_Word = []  # Here we are Storeing the Unique Words. Those who are not Repeted at all.
    for i in Word_Count: 
        if Word_Count[i] ==1:
            Uniqe_Word.append(i)
    max = 0
    Max_Word = ""    
    for i in Uniqe_Word:
        if len(i)>max:
            max = len(i)
            Max_Word = i
    return Max_Word
        
            
print(longest_unique_substring_Without_repetation("Alok Tiwari and there will be more than Tiwari"))
        
    
            