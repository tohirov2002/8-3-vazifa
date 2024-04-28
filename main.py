from LinkedList import LinkedList

week = LinkedList()
week.append(1)
week.append(2.5)
week.append("Monday")
week.append(True)
week.append([3, 4, 5])


week.print_list()
print(week.counts())
str1 = "Salom"
str2 = week.string_sanash(str1)
print(str2)
new_list = [6, 7, "Wednesday", False]
week.append_list(new_list)
new_list = [6, 7, "Wednesday", False]
week.append_list(new_list)
week.print_list()
delete = week.remove()
print(delete)