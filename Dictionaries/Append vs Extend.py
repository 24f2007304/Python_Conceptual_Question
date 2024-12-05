# def Fllaterd_list(lists):
#     Flatterlist = []
#     for i in lists:
#         if isinstance(i , list):
#             Flatterlist.extend(Fllaterd_list(i))
#             # Modifies In-Place: The extend method changes the original list directly and does not create a new list.
#         else:
#             Flatterlist.append(i)
#     return Flatterlist


# print(Fllaterd_list([12,23,[23,34,[34,345,[45,4,57]]]]))
a = [12,52,"Alok"]
b = ["Parth","Anil"]
a.append(b)
print(a)
ac = [12,52,"Alok"]
bc = ["Parth","Anil"]
ac.extend(bc)
print(ac)