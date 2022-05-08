import random
import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox


bombcount=30
size=10
count=0
for i in range(0,size+1):
    globals()[f"row{i}c"] = []
    globals()[f"row{i}bomb"] = 0
    for x in range(0,size+2):
        globals()[f"row{i}c"].append(0)

for i in range(1,bombcount):
    pickbombline = random.randint(1,size)
    globals()[f"row{pickbombline}bomb"] +=1

totalbombs = 0
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
                if globals()[f"row{i}c"][columnplacement] !=9:
                    #places bomb and moves on to the surrounding tiles, to update their count
                    globals()[f"row{i}c"][columnplacement] =9
                    placedbomb=True
                    totalbombs +=1
                    surrounding = False
                    while not surrounding:
                        #up left tile +1
                        if globals()[f"row{i-1}c"][columnplacement-1] !=9:
                            globals()[f"row{i-1}c"][columnplacement-1] +=1
                        #up center tile +1
                        if globals()[f"row{i-1}c"][columnplacement] !=9:
                            globals()[f"row{i-1}c"][columnplacement] +=1
                        #up right tile +1
                        if globals()[f"row{i-1}c"][columnplacement+1] !=9:
                            globals()[f"row{i-1}c"][columnplacement+1] +=1
                        #center left tile +1
                        if globals()[f"row{i}c"][columnplacement-1] !=9:
                            globals()[f"row{i}c"][columnplacement-1] +=1
                        #center right tile +1
                        if globals()[f"row{i}c"][columnplacement+1] !=9:
                            globals()[f"row{i}c"][columnplacement+1] +=1
                        #down left tile +1
                        if globals()[f"row{i+1}c"][columnplacement-1] !=9:
                            globals()[f"row{i+1}c"][columnplacement-1] +=1
                        #down center tile +1
                        if globals()[f"row{i+1}c"][columnplacement] !=9:
                            globals()[f"row{i+1}c"][columnplacement] +=1
                        #down right tile +1
                        if globals()[f"row{i+1}c"][columnplacement+1] !=9:
                            globals()[f"row{i+1}c"][columnplacement+1] +=1
                        surrounding = True
print(totalbombs)                    
#initializing board (printable board)
for i in range(0,size):
    globals()[f"row{i}c"].pop()
    globals()[f"row{i}c"].pop(0)
    print(globals()[f"row{i}c"])

def gameend():
    messagebox.showerror(title="Mine Detonated", message="Looks like this game has ended")
    quit()

def gameendwin():
    messagebox.showerror(title="Complete!", message="You've won! Congradulations")
    quit()

master=tkinter.Tk()
master.title("Minesweeper")
geo = 500
height = 400
master.geometry(f"{geo}x{height}")
tilesopened = 0
font="Consolas"
def pressedr0c0():
    globals()[f"buttonpressrow{0}column{0}"]['text'] = f" {row0c[0]} "
    globals()[f"buttonpressrow{0}column{0}"]['font'] = font    
    if row0c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    print(tilesopened)
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr0c0, font=font)
globals()[f"buttonpressrow{0}column{0}"].grid(row=0, column=0)
def pressedr0c1():
    globals()[f"buttonpressrow{0}column{1}"]['text'] = f" {row0c[1]} "
    if row0c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr0c1, font=font)
globals()[f"buttonpressrow{0}column{1}"].grid(row=0, column=1)
def pressedr0c2():
    globals()[f"buttonpressrow{0}column{2}"]['text'] = f" {row0c[2]} "
    if row0c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr0c2, font=font)
globals()[f"buttonpressrow{0}column{2}"].grid(row=0, column=2)
def pressedr0c3():
    globals()[f"buttonpressrow{0}column{3}"]['text'] = f" {row0c[3]} "
    if row0c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr0c3, font=font)
globals()[f"buttonpressrow{0}column{3}"].grid(row=0, column=3)
def pressedr0c4():
    globals()[f"buttonpressrow{0}column{4}"]['text'] = f" {row0c[4]} "
    if row0c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr0c4, font=font)
globals()[f"buttonpressrow{0}column{4}"].grid(row=0, column=4)
def pressedr0c5():
    globals()[f"buttonpressrow{0}column{5}"]['text'] = f" {row0c[5]} "
    if row0c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr0c5, font=font)
globals()[f"buttonpressrow{0}column{5}"].grid(row=0, column=5)
def pressedr0c6():
    globals()[f"buttonpressrow{0}column{6}"]['text'] = f" {row0c[6]} "
    if row0c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr0c6, font=font)
globals()[f"buttonpressrow{0}column{6}"].grid(row=0, column=6)
def pressedr0c7():
    globals()[f"buttonpressrow{0}column{7}"]['text'] = f" {row0c[7]} "
    if row0c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr0c7, font=font)
globals()[f"buttonpressrow{0}column{7}"].grid(row=0, column=7)
def pressedr0c8():
    globals()[f"buttonpressrow{0}column{8}"]['text'] = f" {row0c[8]} "
    if row0c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr0c8, font=font)
globals()[f"buttonpressrow{0}column{8}"].grid(row=0, column=8)
def pressedr0c9():
    globals()[f"buttonpressrow{0}column{9}"]['text'] = f" {row0c[9]} "
    if row0c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{0}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr0c9, font=font)
globals()[f"buttonpressrow{0}column{9}"].grid(row=0, column=9)
def pressedr1c0():
    globals()[f"buttonpressrow{1}column{0}"]['text'] = f" {row1c[0]} "  
    if row1c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr1c0, font=font)
globals()[f"buttonpressrow{1}column{0}"].grid(row=1, column=0)
def pressedr1c1():
    globals()[f"buttonpressrow{1}column{1}"]['text'] = f" {row1c[1]} "
    if row1c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr1c1, font=font)
globals()[f"buttonpressrow{1}column{1}"].grid(row=1, column=1)
def pressedr1c2():
    globals()[f"buttonpressrow{1}column{2}"]['text'] = f" {row1c[2]} "
    if row1c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr1c2, font=font)
globals()[f"buttonpressrow{1}column{2}"].grid(row=1, column=2)
def pressedr1c3():
    globals()[f"buttonpressrow{1}column{3}"]['text'] = f" {row1c[3]} "
    if row1c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr1c3, font=font)
globals()[f"buttonpressrow{1}column{3}"].grid(row=1, column=3)
def pressedr1c4():
    globals()[f"buttonpressrow{1}column{4}"]['text'] = f" {row1c[4]} "
    if row1c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr1c4, font=font)
globals()[f"buttonpressrow{1}column{4}"].grid(row=1, column=4)
def pressedr1c5():
    globals()[f"buttonpressrow{1}column{5}"]['text'] = f" {row1c[5]} "
    if row1c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr1c5, font=font)
globals()[f"buttonpressrow{1}column{5}"].grid(row=1, column=5)
def pressedr1c6():
    globals()[f"buttonpressrow{1}column{6}"]['text'] = f" {row1c[6]} "
    if row1c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr1c6, font=font)
globals()[f"buttonpressrow{1}column{6}"].grid(row=1, column=6)
def pressedr1c7():
    globals()[f"buttonpressrow{1}column{7}"]['text'] = f" {row1c[7]} "
    if row1c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr1c7, font=font)
globals()[f"buttonpressrow{1}column{7}"].grid(row=1, column=7)
def pressedr1c8():
    globals()[f"buttonpressrow{1}column{8}"]['text'] = f" {row1c[8]} "
    if row1c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr1c8, font=font)
globals()[f"buttonpressrow{1}column{8}"].grid(row=1, column=8)
def pressedr1c9():
    globals()[f"buttonpressrow{1}column{9}"]['text'] = f" {row1c[9]} "
    if row1c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{1}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr1c9, font=font)
globals()[f"buttonpressrow{1}column{9}"].grid(row=1, column=9)
def pressedr2c0():
    globals()[f"buttonpressrow{2}column{0}"]['text'] = f" {row2c[0]} "  
    if row2c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr2c0, font=font)
globals()[f"buttonpressrow{2}column{0}"].grid(row=2, column=0)
def pressedr2c1():
    globals()[f"buttonpressrow{2}column{1}"]['text'] = f" {row2c[1]} "
    if row2c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr2c1, font=font)
globals()[f"buttonpressrow{2}column{1}"].grid(row=2, column=1)
def pressedr2c2():
    globals()[f"buttonpressrow{2}column{2}"]['text'] = f" {row2c[2]} "
    if row2c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr2c2, font=font)
globals()[f"buttonpressrow{2}column{2}"].grid(row=2, column=2)
def pressedr2c3():
    globals()[f"buttonpressrow{2}column{3}"]['text'] = f" {row2c[3]} "
    if row2c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr2c3, font=font)
globals()[f"buttonpressrow{2}column{3}"].grid(row=2, column=3)
def pressedr2c4():
    globals()[f"buttonpressrow{2}column{4}"]['text'] = f" {row2c[4]} "
    if row2c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr2c4, font=font)
globals()[f"buttonpressrow{2}column{4}"].grid(row=2, column=4)
def pressedr2c5():
    globals()[f"buttonpressrow{2}column{5}"]['text'] = f" {row2c[5]} "
    if row2c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr2c5, font=font)
globals()[f"buttonpressrow{2}column{5}"].grid(row=2, column=5)
def pressedr2c6():
    globals()[f"buttonpressrow{2}column{6}"]['text'] = f" {row2c[6]} "
    if row2c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr2c6, font=font)
globals()[f"buttonpressrow{2}column{6}"].grid(row=2, column=6)
def pressedr2c7():
    globals()[f"buttonpressrow{2}column{7}"]['text'] = f" {row2c[7]} "
    if row2c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr2c7, font=font)
globals()[f"buttonpressrow{2}column{7}"].grid(row=2, column=7)
def pressedr2c8():
    globals()[f"buttonpressrow{2}column{8}"]['text'] = f" {row2c[8]} "
    if row2c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr2c8, font=font)
globals()[f"buttonpressrow{2}column{8}"].grid(row=2, column=8)
def pressedr2c9():
    globals()[f"buttonpressrow{2}column{9}"]['text'] = f" {row2c[9]} "
    if row2c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{2}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr2c9, font=font)
globals()[f"buttonpressrow{2}column{9}"].grid(row=2, column=9)
def pressedr3c0():
    globals()[f"buttonpressrow{3}column{0}"]['text'] = f" {row3c[0]} "
    if row3c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr3c0, font=font)
globals()[f"buttonpressrow{3}column{0}"].grid(row=3, column=0)
def pressedr3c1():
    globals()[f"buttonpressrow{3}column{1}"]['text'] = f" {row3c[1]} "
    if row3c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr3c1, font=font)
globals()[f"buttonpressrow{3}column{1}"].grid(row=3, column=1)
def pressedr3c2():
    globals()[f"buttonpressrow{3}column{2}"]['text'] = f" {row3c[2]} "
    if row3c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr3c2, font=font)
globals()[f"buttonpressrow{3}column{2}"].grid(row=3, column=2)
def pressedr3c3():
    globals()[f"buttonpressrow{3}column{3}"]['text'] = f" {row3c[3]} "
    if row3c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr3c3, font=font)
globals()[f"buttonpressrow{3}column{3}"].grid(row=3, column=3)
def pressedr3c4():
    globals()[f"buttonpressrow{3}column{4}"]['text'] = f" {row3c[4]} "
    if row3c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr3c4, font=font)
globals()[f"buttonpressrow{3}column{4}"].grid(row=3, column=4)
def pressedr3c5():
    globals()[f"buttonpressrow{3}column{5}"]['text'] = f" {row3c[5]} "
    if row3c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr3c5, font=font)
globals()[f"buttonpressrow{3}column{5}"].grid(row=3, column=5)
def pressedr3c6():
    globals()[f"buttonpressrow{3}column{6}"]['text'] = f" {row3c[6]} "
    if row3c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr3c6, font=font)
globals()[f"buttonpressrow{3}column{6}"].grid(row=3, column=6)
def pressedr3c7():
    globals()[f"buttonpressrow{3}column{7}"]['text'] = f" {row3c[7]} "
    if row3c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr3c7, font=font)
globals()[f"buttonpressrow{3}column{7}"].grid(row=3, column=7)
def pressedr3c8():
    globals()[f"buttonpressrow{3}column{8}"]['text'] = f" {row3c[8]} "
    if row3c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr3c8, font=font)
globals()[f"buttonpressrow{3}column{8}"].grid(row=3, column=8)
def pressedr3c9():
    globals()[f"buttonpressrow{3}column{9}"]['text'] = f" {row3c[9]} "
    if row3c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{3}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr3c9, font=font)
globals()[f"buttonpressrow{3}column{9}"].grid(row=3, column=9)
def pressedr4c0():
    globals()[f"buttonpressrow{4}column{0}"]['text'] = f" {row4c[0]} "
    if row4c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr4c0, font=font)
globals()[f"buttonpressrow{4}column{0}"].grid(row=4, column=0)
def pressedr4c1():
    globals()[f"buttonpressrow{4}column{1}"]['text'] = f" {row4c[1]} "
    if row4c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr4c1, font=font)
globals()[f"buttonpressrow{4}column{1}"].grid(row=4, column=1)
def pressedr4c2():
    globals()[f"buttonpressrow{4}column{2}"]['text'] = f" {row4c[2]} "
    if row4c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr4c2, font=font)
globals()[f"buttonpressrow{4}column{2}"].grid(row=4, column=2)
def pressedr4c3():
    globals()[f"buttonpressrow{4}column{3}"]['text'] = f" {row4c[3]} "
    if row4c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr4c3, font=font)
globals()[f"buttonpressrow{4}column{3}"].grid(row=4, column=3)
def pressedr4c4():
    globals()[f"buttonpressrow{4}column{4}"]['text'] = f" {row4c[4]} "
    if row4c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr4c4, font=font)
globals()[f"buttonpressrow{4}column{4}"].grid(row=4, column=4)
def pressedr4c5():
    globals()[f"buttonpressrow{4}column{5}"]['text'] = f" {row4c[5]} "
    if row4c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr4c5, font=font)
globals()[f"buttonpressrow{4}column{5}"].grid(row=4, column=5)
def pressedr4c6():
    globals()[f"buttonpressrow{4}column{6}"]['text'] = f" {row4c[6]} "
    if row4c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr4c6, font=font)
globals()[f"buttonpressrow{4}column{6}"].grid(row=4, column=6)
def pressedr4c7():
    globals()[f"buttonpressrow{4}column{7}"]['text'] = f" {row4c[7]} "
    if row4c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr4c7, font=font)
globals()[f"buttonpressrow{4}column{7}"].grid(row=4, column=7)
def pressedr4c8():
    globals()[f"buttonpressrow{4}column{8}"]['text'] = f" {row4c[8]} "
    if row4c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr4c8, font=font)
globals()[f"buttonpressrow{4}column{8}"].grid(row=4, column=8)
def pressedr4c9():
    globals()[f"buttonpressrow{4}column{9}"]['text'] = f" {row4c[9]} "
    if row4c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{4}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr4c9, font=font)
globals()[f"buttonpressrow{4}column{9}"].grid(row=4, column=9)
def pressedr5c0():
    globals()[f"buttonpressrow{5}column{0}"]['text'] = f" {row5c[0]} "
    if row5c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr5c0, font=font)
globals()[f"buttonpressrow{5}column{0}"].grid(row=5, column=0)
def pressedr5c1():
    globals()[f"buttonpressrow{5}column{1}"]['text'] = f" {row5c[1]} "
    if row5c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr5c1, font=font)
globals()[f"buttonpressrow{5}column{1}"].grid(row=5, column=1)
def pressedr5c2():
    globals()[f"buttonpressrow{5}column{2}"]['text'] = f" {row5c[2]} "
    if row5c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr5c2, font=font)
globals()[f"buttonpressrow{5}column{2}"].grid(row=5, column=2)
def pressedr5c3():
    globals()[f"buttonpressrow{5}column{3}"]['text'] = f" {row5c[3]} "
    if row5c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr5c3, font=font)
globals()[f"buttonpressrow{5}column{3}"].grid(row=5, column=3)
def pressedr5c4():
    globals()[f"buttonpressrow{5}column{4}"]['text'] = f" {row5c[4]} "
    if row5c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr5c4, font=font)
globals()[f"buttonpressrow{5}column{4}"].grid(row=5, column=4)
def pressedr5c5():
    globals()[f"buttonpressrow{5}column{5}"]['text'] = f" {row5c[5]} "
    if row5c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr5c5, font=font)
globals()[f"buttonpressrow{5}column{5}"].grid(row=5, column=5)
def pressedr5c6():
    globals()[f"buttonpressrow{5}column{6}"]['text'] = f" {row5c[6]} "
    if row5c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr5c6, font=font)
globals()[f"buttonpressrow{5}column{6}"].grid(row=5, column=6)
def pressedr5c7():
    globals()[f"buttonpressrow{5}column{7}"]['text'] = f" {row5c[7]} "
    if row5c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr5c7, font=font)
globals()[f"buttonpressrow{5}column{7}"].grid(row=5, column=7)
def pressedr5c8():
    globals()[f"buttonpressrow{5}column{8}"]['text'] = f" {row5c[8]} "
    if row5c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr5c8, font=font)
globals()[f"buttonpressrow{5}column{8}"].grid(row=5, column=8)
def pressedr5c9():
    globals()[f"buttonpressrow{5}column{9}"]['text'] = f" {row5c[9]} "
    if row5c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{5}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr5c9, font=font)
globals()[f"buttonpressrow{5}column{9}"].grid(row=5, column=9)
def pressedr6c0():
    globals()[f"buttonpressrow{6}column{0}"]['text'] = f" {row6c[0]} "
    if row6c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr6c0, font=font)
globals()[f"buttonpressrow{6}column{0}"].grid(row=6, column=0)
def pressedr6c1():
    globals()[f"buttonpressrow{6}column{1}"]['text'] = f" {row6c[1]} "
    if row6c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr6c1, font=font)
globals()[f"buttonpressrow{6}column{1}"].grid(row=6, column=1)
def pressedr6c2():
    globals()[f"buttonpressrow{6}column{2}"]['text'] = f" {row6c[2]} "
    if row6c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr6c2, font=font)
globals()[f"buttonpressrow{6}column{2}"].grid(row=6, column=2)
def pressedr6c3():
    globals()[f"buttonpressrow{6}column{3}"]['text'] = f" {row6c[3]} "
    if row6c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr6c3, font=font)
globals()[f"buttonpressrow{6}column{3}"].grid(row=6, column=3)
def pressedr6c4():
    globals()[f"buttonpressrow{6}column{4}"]['text'] = f" {row6c[4]} "
    if row6c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr6c4, font=font)
globals()[f"buttonpressrow{6}column{4}"].grid(row=6, column=4)
def pressedr6c5():
    globals()[f"buttonpressrow{6}column{5}"]['text'] = f" {row6c[5]} "
    if row6c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr6c5, font=font)
globals()[f"buttonpressrow{6}column{5}"].grid(row=6, column=5)
def pressedr6c6():
    globals()[f"buttonpressrow{6}column{6}"]['text'] = f" {row6c[6]} "
    if row6c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr6c6, font=font)
globals()[f"buttonpressrow{6}column{6}"].grid(row=6, column=6)
def pressedr6c7():
    globals()[f"buttonpressrow{6}column{7}"]['text'] = f" {row6c[7]} "
    if row6c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr6c7, font=font)
globals()[f"buttonpressrow{6}column{7}"].grid(row=6, column=7)
def pressedr6c8():
    globals()[f"buttonpressrow{6}column{8}"]['text'] = f" {row6c[8]} "
    if row6c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr6c8, font=font)
globals()[f"buttonpressrow{6}column{8}"].grid(row=6, column=8)
def pressedr6c9():
    globals()[f"buttonpressrow{6}column{9}"]['text'] = f" {row6c[9]} "
    if row6c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{6}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr6c9, font=font)
globals()[f"buttonpressrow{6}column{9}"].grid(row=6, column=9)
def pressedr7c0():
    globals()[f"buttonpressrow{7}column{0}"]['text'] = f" {row7c[0]} "
    if row7c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr7c0, font=font)
globals()[f"buttonpressrow{7}column{0}"].grid(row=7, column=0)
def pressedr7c1():
    globals()[f"buttonpressrow{7}column{1}"]['text'] = f" {row7c[1]} "
    if row7c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr7c1, font=font)
globals()[f"buttonpressrow{7}column{1}"].grid(row=7, column=1)
def pressedr7c2():
    globals()[f"buttonpressrow{7}column{2}"]['text'] = f" {row7c[2]} "
    if row7c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr7c2, font=font)
globals()[f"buttonpressrow{7}column{2}"].grid(row=7, column=2)
def pressedr7c3():
    globals()[f"buttonpressrow{7}column{3}"]['text'] = f" {row7c[3]} "
    if row7c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr7c3, font=font)
globals()[f"buttonpressrow{7}column{3}"].grid(row=7, column=3)
def pressedr7c4():
    globals()[f"buttonpressrow{7}column{4}"]['text'] = f" {row7c[4]} "
    if row7c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr7c4, font=font)
globals()[f"buttonpressrow{7}column{4}"].grid(row=7, column=4)
def pressedr7c5():
    globals()[f"buttonpressrow{7}column{5}"]['text'] = f" {row7c[5]} "
    if row7c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr7c5, font=font)
globals()[f"buttonpressrow{7}column{5}"].grid(row=7, column=5)
def pressedr7c6():
    globals()[f"buttonpressrow{7}column{6}"]['text'] = f" {row7c[6]} "
    if row7c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr7c6, font=font)
globals()[f"buttonpressrow{7}column{6}"].grid(row=7, column=6)
def pressedr7c7():
    globals()[f"buttonpressrow{7}column{7}"]['text'] = f" {row7c[7]} "
    if row7c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr7c7, font=font)
globals()[f"buttonpressrow{7}column{7}"].grid(row=7, column=7)
def pressedr7c8():
    globals()[f"buttonpressrow{7}column{8}"]['text'] = f" {row7c[8]} "
    if row7c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr7c8, font=font)
globals()[f"buttonpressrow{7}column{8}"].grid(row=7, column=8)
def pressedr7c9():
    globals()[f"buttonpressrow{7}column{9}"]['text'] = f" {row7c[9]} "
    if row7c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{7}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr7c9, font=font)
globals()[f"buttonpressrow{7}column{9}"].grid(row=7, column=9)
def pressedr8c0():
    globals()[f"buttonpressrow{8}column{0}"]['text'] = f" {row8c[0]} "
    if row8c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr8c0, font=font)
globals()[f"buttonpressrow{8}column{0}"].grid(row=8, column=0)
def pressedr8c1():
    globals()[f"buttonpressrow{8}column{1}"]['text'] = f" {row8c[1]} "
    if row8c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr8c1, font=font)
globals()[f"buttonpressrow{8}column{1}"].grid(row=8, column=1)
def pressedr8c2():
    globals()[f"buttonpressrow{8}column{2}"]['text'] = f" {row8c[2]} "
    if row8c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr8c2, font=font)
globals()[f"buttonpressrow{8}column{2}"].grid(row=8, column=2)
def pressedr8c3():
    globals()[f"buttonpressrow{8}column{3}"]['text'] = f" {row8c[3]} "
    if row8c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr8c3, font=font)
globals()[f"buttonpressrow{8}column{3}"].grid(row=8, column=3)
def pressedr8c4():
    globals()[f"buttonpressrow{8}column{4}"]['text'] = f" {row8c[4]} "
    if row8c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr8c4, font=font)
globals()[f"buttonpressrow{8}column{4}"].grid(row=8, column=4)
def pressedr8c5():
    globals()[f"buttonpressrow{8}column{5}"]['text'] = f" {row8c[5]} "
    if row8c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr8c5, font=font)
globals()[f"buttonpressrow{8}column{5}"].grid(row=8, column=5)
def pressedr8c6():
    globals()[f"buttonpressrow{8}column{6}"]['text'] = f" {row8c[6]} "
    if row8c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr8c6, font=font)
globals()[f"buttonpressrow{8}column{6}"].grid(row=8, column=6)
def pressedr8c7():
    globals()[f"buttonpressrow{8}column{7}"]['text'] = f" {row8c[7]} "
    if row8c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr8c7, font=font)
globals()[f"buttonpressrow{8}column{7}"].grid(row=8, column=7)
def pressedr8c8():
    globals()[f"buttonpressrow{8}column{8}"]['text'] = f" {row8c[8]} "
    if row8c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr8c8, font=font)
globals()[f"buttonpressrow{8}column{8}"].grid(row=8, column=8)
def pressedr8c9():
    globals()[f"buttonpressrow{8}column{9}"]['text'] = f" {row8c[9]} "
    if row8c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{8}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr8c9, font=font)
globals()[f"buttonpressrow{8}column{9}"].grid(row=8, column=9)
def pressedr9c0():
    globals()[f"buttonpressrow{9}column{0}"]['text'] = f" {row9c[0]} "
    if row9c[0] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{0}"] = tkinter.Button(master, text= "   ", command=pressedr9c0, font=font)
globals()[f"buttonpressrow{9}column{0}"].grid(row=9, column=0)
def pressedr9c1():
    globals()[f"buttonpressrow{9}column{1}"]['text'] = f" {row9c[1]} "
    if row9c[1] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{1}"] = tkinter.Button(master, text= "   ", command=pressedr9c1, font=font)
globals()[f"buttonpressrow{9}column{1}"].grid(row=9, column=1)
def pressedr9c2():
    globals()[f"buttonpressrow{9}column{2}"]['text'] = f" {row9c[2]} "
    if row9c[2] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{2}"] = tkinter.Button(master, text= "   ", command=pressedr9c2, font=font)
globals()[f"buttonpressrow{9}column{2}"].grid(row=9, column=2)
def pressedr9c3():
    globals()[f"buttonpressrow{9}column{3}"]['text'] = f" {row9c[3]} "
    if row9c[3] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{3}"] = tkinter.Button(master, text= "   ", command=pressedr9c3, font=font)
globals()[f"buttonpressrow{9}column{3}"].grid(row=9, column=3)
def pressedr9c4():
    globals()[f"buttonpressrow{9}column{4}"]['text'] = f" {row9c[4]} "
    if row9c[4] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{4}"] = tkinter.Button(master, text= "   ", command=pressedr9c4, font=font)
globals()[f"buttonpressrow{9}column{4}"].grid(row=9, column=4)
def pressedr9c5():
    globals()[f"buttonpressrow{9}column{5}"]['text'] = f" {row9c[5]} "
    if row9c[5] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{5}"] = tkinter.Button(master, text= "   ", command=pressedr9c5, font=font)
globals()[f"buttonpressrow{9}column{5}"].grid(row=9, column=5)
def pressedr9c6():
    globals()[f"buttonpressrow{9}column{6}"]['text'] = f" {row9c[6]} "
    if row9c[6] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{6}"] = tkinter.Button(master, text= "   ", command=pressedr9c6, font=font)
globals()[f"buttonpressrow{9}column{6}"].grid(row=9, column=6)
def pressedr9c7():
    globals()[f"buttonpressrow{9}column{7}"]['text'] = f" {row9c[7]} "
    if row9c[7] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{7}"] = tkinter.Button(master, text= "   ", command=pressedr9c7, font=font)
globals()[f"buttonpressrow{9}column{7}"].grid(row=9, column=7)
def pressedr9c8():
    globals()[f"buttonpressrow{9}column{8}"]['text'] = f" {row9c[8]} "
    if row9c[8] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{8}"] = tkinter.Button(master, text= "   ", command=pressedr9c8, font=font)
globals()[f"buttonpressrow{9}column{8}"].grid(row=9, column=8)
def pressedr9c9():
    globals()[f"buttonpressrow{9}column{9}"]['text'] = f" {row9c[9]} "
    if row9c[9] == 9:
        gameend()
    global tilesopened
    tilesopened += 1
    if tilesopened  == 102 - totalbombs:
        gameendwin()
globals()[f"buttonpressrow{9}column{9}"] = tkinter.Button(master, text= "   ", command=pressedr9c9, font=font)
globals()[f"buttonpressrow{9}column{9}"].grid(row=9, column=9)


master.mainloop()