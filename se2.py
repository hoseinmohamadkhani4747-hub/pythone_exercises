#Exercise 2:
# Defining and printing variables
#part 1 to 11


numbers = [ 1 , 2 , 3 , 4, 5 ]
for mm in numbers:
    print(mm)



mylist = [ "bmw" , "toyota" , "lambo" , "douge"]
print(mylist[0])
print(mylist[-1])



mylist = [ "bmw" , "toyota" , "lambo" , "douge"]
print(len(mylist))


number = [ 1 , 2 , 3 ]
number.append(10)
print(number)


mylist = [ "bmw" , "toyota" , "lambo" , "douge"]
del mylist[2]
print(mylist)

t = [ 10 , 7 , 21 ]
print(t[0] + t[1])

names = ["ali" , "hosein" , "mamad" , "hasan"]
name = "reza"
if name not in names:
    print("not ok")



d = [ ]
d.append(10)
d.append(7)
d.append(21)
print(d)


u = [ 10 , 7 , 21 ]
t = 0
for n in u:
    t += n

    
print(f"answer: {t}")




k = [ 5 , 15 , 8 , 20 , 3 ]
for w in k:
    if w > 10:
        print(w)
 