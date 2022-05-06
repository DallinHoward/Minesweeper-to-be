import random
import tkinter


size=16
bombcount=size*2

for i in range(0,size+1):
    globals()[f"row{i}"] = []
    globals()[f"row{i}bomb"] = 0
    for x in range(0,size+2):
        globals()[f"row{i}"].append(0)

for i in range(1,bombcount):
    pickbombline = random.randint(1,size)
    globals()[f"row{pickbombline}bomb"] +=1
    
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
                    
#initializing board (printable board)
for i in range(0,size):
    globals()[f"row{i}"].pop()
    globals()[f"row{i}"].pop(0)
    print(globals()[f"row{i}"])
        

master=tkinter.Tk()
master.title("Minesweeper")
geo = size*26
master.geometry(f"{geo}x{geo}")


def buttonpushed(row,column):
    print(globals()[f"row{row}"][column])

for i in range(0,size):   
    for x in range(0,size):
        globals()[f"buttonrow{i}column{x}"] = tkinter.Button(master, text= "     ", command=buttonpushed(i,x))
        globals()[f"buttonrow{i}column{x}"].grid(row=i, column=x)


    
master.mainloop()