'''In the first line if the Input accept a sequence of space - seperatede words. In the Second line of input acccept a single word. If this single word no present in the Sequence , then print YES and in next line of the Output, Print the number of times the word appears in the Sequence.'''

Seq = input().split()
Word = input()
count = 0

for i in Seq:
    if i == Word:
        count +=1
if count !=0:
    print(f"Yes\n{count}")  # TO use only one print Statement we can print in two line By Useing these.
   