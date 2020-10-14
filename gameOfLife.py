import tkinter
import random
import numpy as np

#------------------------------------------------------
# App Logic
#------------------------------------------------------

cellsData = np.zeros((21,21))
cellsList = []
debugMode = False
programRunning = 0
stopSignal = False

def runControl():

  global programRunning
  global stopSignal

  if programRunning == 0:
    start['state'] = "disabled"
    stop['state'] = "normal"
    defaultDisposition1['state'] = 'disabled'
    defaultDisposition2['state'] = 'disabled'
    defaultDisposition3['state'] = 'disabled'
    programRunning = 1
    checkLife()
  elif programRunning == 1:
    start['state'] = "normal"
    stop['state'] = "disabled"
    defaultDisposition1['state'] = 'normal'
    defaultDisposition2['state'] = 'normal'
    defaultDisposition3['state'] = 'normal'
    programRunning = 0
    stopSignal = True

def disposition(disposition):

  # Restart the board

  for row in range(0,21):
    for col in range(0,21):
      cellsData[row][col] = 0
  comeAlive()

  if disposition == 1:

    cellsData[9][10] = 1
    cellsData[10][10] = 1
    cellsData[11][10] = 1
    comeAlive()

  elif disposition == 2:

    cellsData[9][9] = 1
    cellsData[9][10] = 1
    cellsData[10][10] = 1
    cellsData[10][11] = 1
    cellsData[11][10] = 1
    comeAlive()

  elif disposition == 3:
    
    cellsData[8][10] = 1
    cellsData[9][10] = 1
    cellsData[10][10] = 1
    cellsData[11][11] = 1
    cellsData[12][10] = 1
    comeAlive()

def checkLife():

  global stopSignal

  for x in cellsList:
    cellsAlive = 0
    col = x.grid_info()['column']
    row = x.grid_info()['row']

    try:
      if int(cellsData[row-1][col-1]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row-1][col]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row-1][col+1]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row][col-1]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row][col+1]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row+1][col-1]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row+1][col]) == 1:
        cellsAlive += 1
    except:
      pass

    try:
      if int(cellsData[row+1][col+1]) == 1:
        cellsAlive += 1
    except:
      pass
    
    if x['bg'] == "black":
      if cellsAlive == 3:
        x['bg'] = "green"
    else:
      if cellsAlive == 2 or cellsAlive == 3:
        x['bg'] = 'green'    
      else:
        x['bg'] = 'black'
    
  for x in cellsList:
    col = x.grid_info()['column']
    row = x.grid_info()['row']
    if x['bg'] == 'black':
      cellsData[row][col] = 0
      if debugMode:
        x['text'] = '0'
    elif x['bg'] == 'green':
      cellsData[row][col] = 1
      if debugMode:
        x['text'] = '1'

  ID = mainWindow.after(100,checkLife)
  if stopSignal == True:
    mainWindow.after_cancel(ID)
    stopSignal = False

def comeAlive():
  for x in cellsList:
    col = x.grid_info()['column']
    row = x.grid_info()['row']
    
    if debugMode:
      x['text'] = int(cellsData[row][col])
    if int(cellsData[row][col]) == 1:
      x['bg'] = 'green'
    else:
      x['bg'] = 'black'


#------------------------------------------------------
# Window Construction
#------------------------------------------------------

mainWindow = tkinter.Tk()
mainWindow.title("Juego de la vida")

frameGame = tkinter.LabelFrame(mainWindow)
frameGame.grid(row=0,column=0)

frameMenu = tkinter.LabelFrame(mainWindow)
frameMenu.grid(row=0,column=1)

for row in range(0,21):
  rowItems = []
  for col in range(0,21):
    label = tkinter.Label(frameGame,bg="black",fg="red",width=2,height=1)
    label.grid(row=row,column=col)
    rowItems.append(0)
    cellsList.append(label)
  cellsData = np.insert(cellsData,row,rowItems,axis=0)

# START/STOP BUTTONS

start = tkinter.Button(frameMenu,text="Start",width=20,height=5,command=lambda:runControl())
start.grid(row=0,column=0,columnspan=3,pady=(0,20))

stop = tkinter.Button(frameMenu,text="Stop",width=20,height=5,state='disabled',command=lambda:runControl())
stop.grid(row=1,column=0,columnspan=3,pady=(0,40))

# DISPOSITIONS MENU

label = tkinter.Label(frameMenu,text="Disposition:")
label.grid(row=2,column=1,columnspan=1,pady=(0,20))

defaultDisposition1 = tkinter.Button(frameMenu,text="1",width=8,height=4,command=lambda:disposition(1))
defaultDisposition1.grid(row=3,column=0)

defaultDisposition2 = tkinter.Button(frameMenu,text="2",width=8,height=4,command=lambda:disposition(2))
defaultDisposition2.grid(row=3,column=1)

defaultDisposition3 = tkinter.Button(frameMenu,text="3",width=8,height=4,command=lambda:disposition(3))
defaultDisposition3.grid(row=3,column=2)

mainWindow.mainloop()
