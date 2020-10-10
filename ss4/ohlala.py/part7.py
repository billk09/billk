#1
Highscore= [45,67,56,78]
print('Highscore:',Highscore)
#2
for i in range(len(Highscore)):
    print(i+1, "." , Highscore[i])
#3
x=int(input("New score:"))
Highscore.append(x)
print('High score:')
for i in range(len(Highscore)):
    print(i+1, Highscore[i])

