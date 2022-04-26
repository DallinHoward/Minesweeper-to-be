import random

size=16
bombcount=size*2

for i in range(0,size+1):
    globals()[f"row{i}"] = []
    for x in range(0,size+2):
        globals()[f"row{i}"].append(0)
    print(globals()[f"row{i}"])


row9bomb,row10bomb,row11bomb,row12bomb,row13bomb,row14bomb,row15bomb,row16bomb,row1bomb,row2bomb,row3bomb,row4bomb,row5bomb,row6bomb,row7bomb,row8bomb, row0bomb,row17bomb =0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


for i in range(1,bombcount):
    pickbombline = random.randint(1,size)
    globals()[f"row{pickbombline}bomb"] +=1
    print(pickbombline,globals()[f"row{pickbombline}bomb"])




#For each row that was made (i)
for i in range(1,size):
    #If a bomb is supposed to spawn in the row (i) excecute the following
    if globals()[f"row{i}bomb"] > 0:
        #Repeat for each bomb to be placed
        for x in range(1,globals()[f"row{i}bomb"]):
            #This is to make sure the code doesn't place a bomb on the same tile
            placedbomb = False
            while not placedbomb:
                #picks a potential tile
                columnplacement = random.randint(1,size)
                #If the tile already has a bomb, pick a new one
                if globals()[f"row{i}"][columnplacement] !=9:
                    #places bomb and moves on to the surrounding tiles, to update their count
                    globals()[f"row{i}"][columnplacement] =9
                    placedbomb=True
                    surrounding = False
                    while not surrounding:
                        #up left tile +1
                        if globals()[f"row{i-1}"][columnplacement-1] !=9:
                            globals()[f"row{i-1}"][columnplacement-1] +=1
                        #up center tile +1
                        if globals()[f"row{i-1}"][columnplacement] !=9:
                            globals()[f"row{i-1}"][columnplacement] +=1
                        #up right tile +1
                        if globals()[f"row{i-1}"][columnplacement+1] !=9:
                            globals()[f"row{i-1}"][columnplacement+1] +=1
                        #center left tile +1
                        if globals()[f"row{i}"][columnplacement-1] !=9:
                            globals()[f"row{i}"][columnplacement-1] +=1
                        #center right tile +1
                        if globals()[f"row{i}"][columnplacement+1] !=9:
                            globals()[f"row{i}"][columnplacement+1] +=1
                        #down left tile +1
                        if globals()[f"row{i+1}"][columnplacement-1] !=9:
                            globals()[f"row{i+1}"][columnplacement-1] +=1
                        #down center tile +1
                        if globals()[f"row{i+1}"][columnplacement] !=9:
                            globals()[f"row{i+1}"][columnplacement] +=1
                        #down right tile +1
                        if globals()[f"row{i+1}"][columnplacement+1] !=9:
                            globals()[f"row{i+1}"][columnplacement+1] +=1
                        surrounding = True

                    

for i in range(0,size):
    globals()[f"row{i}"].pop()
    globals()[f"row{i}"].pop(0)
        
    

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)
print(row7)
print(row8)
print(row9)
print(row10)
print(row11)
print(row12)
print(row13)
print(row14)
print(row15)
print(row16)
