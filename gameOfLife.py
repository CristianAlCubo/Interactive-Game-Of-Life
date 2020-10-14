import tkinter
import random
import numpy as np

cellsData = np.zeros((21,21))
cellsList = []
debugMode = False

def disposition():

  cellsData[13][18] = 1
  cellsData[13][19] = 1
  cellsData[13][20] = 1

def checkLife():
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

  mainWindow.after(100,checkLife)
    
def comeAlive():
  disposition()
  for x in cellsList:
    col = x.grid_info()['column']
    row = x.grid_info()['row']
    
    if debugMode:
      x['text'] = int(cellsData[row][col])
    if int(cellsData[row][col]) == 1:
      x['bg'] = 'green'
    

mainWindow = tkinter.Tk()
mainWindow.title("Juego de la vida")

for row in range(0,21):
  rowItems = []
  for col in range(0,21):
    label = tkinter.Label(bg="black",fg="red",width=2,height=1)
    label.grid(row=row,column=col)
    rowItems.append(0)
    cellsList.append(label)
  cellsData = np.insert(cellsData,row,rowItems,axis=0)

button = tkinter.Button(text="Iniciar",width=56,command=checkLife)
button.grid(row=21,column=0,columnspan=21)

comeAlive()
mainWindow.mainloop()


"""
UN MONTON DE BASURA!!!!!!!!!!!!!!!!!!!!!!!!!!
"""