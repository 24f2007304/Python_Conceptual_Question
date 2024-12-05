    # Given an odd-length string, 
    # swap the parts before and after the middle three characters,
    # while keeping the middle three characters in place.

    # Assume the string has at least 5 characters.

    # Examples:
    #     "firstabclast1" -> "last1abcfirst"
    #     "abcdefghi" -> "ghidefabc"
    
''' Here in the Slicing form[1:3]then in the postion from 1 to 2 ("3 is exclusive") from in the Slicing'''

''' And also Counting Starts from 1 not form 0 in the String.'''
    
string = str(input())
Len = len(string)
NewLen = (len(string)-3)//2
part3 = string[:NewLen]

part1 = string[NewLen+3:]
part2 = string[NewLen:NewLen+3]
print(part1+part2+part3)
