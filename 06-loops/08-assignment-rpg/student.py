def rpg2(n_sides,goal): #2 dobbelstenen van 4 en doel 4
    wincount=0
    totalit=0
    for dob1 in range(1,n_sides+1):
        for dob2 in range(1,n_sides+1):
            sum=dob1+dob2
            totalit+=1
            if sum>=goal:
                wincount+=1
    return (wincount / totalit)*100

#print(rpg2(4,8))

def rpg3(n_sides,goal): #3 dobbelstenen van 4 en doel 4
    wincount=0
    totalit=0
    for dob1 in range(1,n_sides+1):
        for dob2 in range(1,n_sides+1):
            for dob3 in range(1,n_sides+1):
                sum=dob1+dob2+dob3
                totalit+=1
                if sum>=goal:
                    wincount+=1
    return (wincount / totalit)*100

#print(rpg3(4, 4))