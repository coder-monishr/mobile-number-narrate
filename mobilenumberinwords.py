'''
input == 9887552221
output == nine double eight seven double five triple two one 
'''

number = {'1' : 'One', '2': 'Two' , '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six' , '7': 'Seven', '8': 'Eight', '9':'Nine', '0': 'Zero'}
repea = {2: 'double', 3: 'Triple', 4: 'Double double', 5: 'triple double', 6 : 'Triple triple'}

count = 0
a = []
numberinput = input("Enter the number: ")
for i in numberinput:
    a.append(i)
#print(numberinput)
print(a)

# for i in a:
#     if i in number.keys():
#         print(number.get(i), end = " ")
#         count += 1
#     if count in repea.keys():
#             print(repea.get(count), end = " ")

result = []
i = 0
n = len(a)
while i < n:
    count = 1
    while i + 1 < n and a[i] == a[i + 1]:
        count += 1
        i += 1
    if count == 1:
        result.append(number[a[i]].lower())
    elif count == 2:
        result.append("double " + number[a[i]].lower())
    elif count == 3:
        result.append("triple " + number[a[i]].lower())
    elif count == 4:
        result.append("double"+ number[a[i]].lower() + "double "+ number[a[i]].lower())
    elif count == 5:
        result.append("Triple " + number[a[i]].lower() + " double " + number[a[i]].lower())
    elif count == 6:
        result.append("Triple " + number[a[i]].lower() + " triple " + number[a[i]].lower())
    else:
        result.extend([number[a[i]].lower()] * count)
    i += 1
print(' '.join(result))
