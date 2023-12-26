import tkinter as tk
WhiteKnight = "WK"
BlackKnight = "BK"
firstTurn = True
whiteTurn = True

def GetValidMoves(row, column, otherPieceLocation):
    validMoves = []
    # Check for the other piece's location
    # Up one and over two 
    if(row - 1 > -1 and column + 2 < 7 and (row - 1, column + 2) != otherPieceLocation):
        validMoves.append((row - 1, column + 2))
    # Up two and over one 
    if(row - 2 > -1 and column + 1 < 7 and (row - 2, column + 1) != otherPieceLocation):
        validMoves.append((row - 2, column + 1))
    # Up two and over negative one 
    if(row - 2 > -1 and column - 1 > -1 and (row - 2, column - 1) != otherPieceLocation):
        validMoves.append((row - 2, column - 1))
    # Up one and over negative two 
    if(row - 1 > -1 and column - 2 > -1 and (row - 1, column -2) != otherPieceLocation):
        validMoves.append((row - 1, column - 2))
        
    # Down one and over negative two 
    if(row + 1 < 7 and column - 2 > -1 and (row + 1, column - 2) != otherPieceLocation):
        validMoves.append((row + 1, column - 2))
    # Down two and over negative one 
    if(row + 2 < 7 and column - 1 > -1 and (row + 2, column - 1) != otherPieceLocation):
        validMoves.append((row + 2, column - 1))
    # Down two and over one 
    if(row + 2 < 7 and column + 1 < 7 and (row + 2, column + 1) != otherPieceLocation):
        validMoves.append((row + 2, column + 1))
    # Down one and over two 
    if(row + 1 < 7 and column + 2 < 7 and (row + 1, column + 2) != otherPieceLocation):
        validMoves.append((row + 1, column + 2))
    return validMoves  

def panel_click(event):
    global WhiteKnight
    global WhiteKnightLocation
    global BlackKnight
    global BlackKnightLocation
    global firstTurn
    global whiteTurn
    global validMoves
    panel_frame = event.widget
    info = panel_frame.grid_info()
    row = info['row']
    column = info['column']
    print(f"Panel clicked at ({row}, {column})")
    if(firstTurn):
        if(whiteTurn):
            new_label = tk.Label(panel_frame, text="White knight", bg=panel_frame.cget("bg"))
            new_label.grid(row=row, column=column, pady=5)
            WhiteKnightLocation = (row, column)
            whiteTurn = False
        else:
            new_label = tk.Label(panel_frame, text="Black knight", bg=panel_frame.cget("bg"))
            new_label.grid(row=row, column=column, pady=5)
            BlackKnightLocation = (row, column)
            whiteTurn = True
            firstTurn = False
    else:
        if '!label2' in panel_frame.children:
            title_label = panel_frame.children['!label2']
            label_text = title_label.cget("text")
            if("white" in label_text.lower() and whiteTurn):
                validMoves = GetValidMoves(row, column, BlackKnightLocation)
            elif ("black" in label_text.lower() and not whiteTurn):
                validMoves = GetValidMoves(row, column, WhiteKnightLocation)
            else:
                print(f"Please select the color whose turn it is. White's turn: {whiteTurn}")
        else:
            color = panel_frame.cget("bg")
            if(color == "lightblue"):
                print("A valid move was selected")
                # Find the panel it is moving from 
                for i in range(len(PanelList)):
                    if '!label2' in panel_frame.children:
                        children = PanelList[i].children['!label2']
                        panel_info = PanelList[i].grid_info()
                        label_text = title_label.cget("text")
                        if(label_text == "White" and whiteTurn):
                            if(panel_info['row'], panel_info['column']):
                                PanelList[i].configure(text="")
                        elif (label_text == "White" and whiteTurn):
                            if(panel_info['row'], panel_info['column']):
                                PanelList[i].configure(text="")
                                            
            else:
                print("The current panel is empty")
            
    if validMoves:   
        for i in range(len(PanelList)):
            panelInfo = PanelList[i].grid_info()
            if((panelInfo['row'], panelInfo['column']) in validMoves):
                PanelList[i].configure(bg="lightblue")
            else:
                PanelList[i].configure(bg="white")   
        validMoves = []        
    else:
        for i in range(len(PanelList)):
            PanelList[i].configure(bg="white")  

def create_panel(parent, title, row, column):
    panel_frame = tk.Frame(parent, bd=1, relief=tk.SOLID)
    panel_frame.grid(row=row, column=column, sticky="nsew")
    panel_frame.configure(bg="white")

    title_label = tk.Label(panel_frame, text=title, font=('Helvetica', 6))
    title_label.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

    # content_label = tk.Label(panel_frame, text="Panel content goes here.")
    #content_label.pack(side=tk.TOP, pady=5, padx=10)
    panel_frame.bind("<Button-1>", panel_click)
    return panel_frame

# Create the main application window
root = tk.Tk()
root.title("Panel Example")


PanelList = []
counter = 1
for i in range(7):
    for j in range(7):
        PanelList.append(create_panel(root, f"({i}, {j})", i, j))
        counter = counter + 1
        
# Configure grid weights to allow resizing

for i in range(7):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()