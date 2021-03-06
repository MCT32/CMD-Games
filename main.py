from colorama import *

def playTicTacToe():
    places = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    placesText = [["","",""],
                  ["","",""],
                  ["","",""]]

    def generatePlacesText():
        for x in range(3):
            for y in range(3):
                if places[x][y] == 0:
                    placesText[x][y] = " "
                elif places[x][y] == 1:
                    placesText[x][y] = "X"
                elif places[x][y] == 2:
                    placesText[x][y] = "O"

    def printGrid():
        generatePlacesText()
        print("  ____ _____ ____\n" +
              " /    |     |    \\\n" +
              "|  " + placesText[0][0] + "  |  " + placesText[0][1] + "  |  " + placesText[0][2] + "  |\n" +
              "|_____|_____|_____|\n" +
              "|     |     |     |\n" +
              "|  " + placesText[1][0] + "  |  " + placesText[1][1] + "  |  " + placesText[1][2] + "  |\n" +
              "|_____|_____|_____|\n" +
              "|     |     |     |\n" +
              "|  " + placesText[2][0] + "  |  " + placesText[2][1] + "  |  " + placesText[2][2] + "  |\n" +
              " \\____|_____|____/\n")

    gameWon = False
    printGrid()

init()
print(Style.RESET_ALL + "   _____ __  __ _____          _____\n" +
                        "  / ____|  \\/  |  __ \\        / ____|\n" +
                        " | |    | \\  / | |  | |______| |  __  __ _ _ __ ___   ___  ___\n" +
                        " | |    | |\\/| | |  | |______| | |_ |/ _` | '_ ` _ \\ / _ \\/ __|\n" +
                        " | |____| |  | | |__| |      | |__| | (_| | | | | | |  __/\\__ \\\n" +
                        "  \\_____|_|  |_|_____/        \\_____|\\__,_|_| |_| |_|\\___||___/\n")
print("\n1] Tic-Tac-Toe\n" +
      "2] Chess\n" +
      "3] Blackjack\n")

selection = input("Type the number of the game you want to play: ")

if selection == "1":
    playTicTacToe()
elif selection == "2":
    playChess()
elif selection == "3":
    playBlackjack()
else:
    print("This is an invalid selection.")
