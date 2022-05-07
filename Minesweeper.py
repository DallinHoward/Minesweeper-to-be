import random

#Lenght and width of the project
size=16
#temporary placeholder for difficulty more bombs = harder
bombcount=size*2

#Initializes my rows/columns in lists named row1, row2, row3, ect...
#Important to note it makes two extra columns and rows giving a border around the whole project.
#This is extremely imporant for later
for i in range(0,size+1):
    globals()[f"row{i}"] = []
    #adds total items in the list equal to total amount of lists, so it's a square
    for x in range(0,size+2):
        globals()[f"row{i}"].append(0)
    print(globals()[f"row{i}"])

#Temporary initializing of bomb counts, will make this a loop later.
row9bomb,row10bomb,row11bomb,row12bomb,row13bomb,row14bomb,row15bomb,row16bomb,row1bomb,row2bomb,row3bomb,row4bomb,row5bomb,row6bomb,row7bomb,row8bomb, row0bomb,row17bomb =0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


#assigns bombs to a row, no placements yet though.
for i in range(1,bombcount):
    pickbombline = random.randint(1,size)
    globals()[f"row{pickbombline}bomb"] +=1

    #temporary check to make sure each line has x amount of bombs for comparison
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

                    
#Removes the border that was initialized earlier. The border was there to catch the potential faults of a bomb in column0 increasing the count on the right most columns count, and vice versa.
for i in range(0,size):
    globals()[f"row{i}"].pop()
    globals()[f"row{i}"].pop(0)
        
    
#Temporary display. This will be changed to a GUI if I can figure that out.
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
