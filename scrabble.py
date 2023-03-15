def myfunc():
    mydict = {}
    mydict["A"] = 1
    mydict["B"] = 3
    mydict["C"] = 3
    mydict["D"] = 2
    mydict["E"] = 1
    mydict["F"] = 4
    mydict["G"] = 2
    mydict["H"] = 4
    mydict["I"] = 1
    mydict["J"] = 8
    mydict["K"] = 5
    mydict["L"] = 1
    mydict["M"] = 3
    mydict["N"] = 1
    mydict["O"] = 1
    mydict["P"] = 3
    mydict["Q"] = 10
    mydict["R"] = 1
    mydict["S"] = 1
    mydict["T"] = 1
    mydict["U"] = 1
    mydict["V"] = 4
    mydict["W"] = 4
    mydict["X"] = 8
    mydict["Y"] = 4
    mydict["Z"] = 10
    player1 = input("Player1 word: ").upper()
    player2 = input("Player2 word: ").upper()
    player1score = 0
    player2score = 0
    resultdict = {}
    for i in player1:
        if i in mydict:
            player1score += mydict[i] 
    resultdict[player1score] = player1 
    for j in player2:
        if j in mydict:
            player2score += mydict[j]
    resultdict[player2score] = player2 
    if resultdict[player1score] > resultdict[player2score]:
        return f'player1wins!' 
    if resultdict[player1score] < resultdict[player2score]:
        return f'player2wins!'
    else:
        return f"it's a tie!"
print(myfunc())
