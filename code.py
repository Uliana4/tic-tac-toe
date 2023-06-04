# Ustawimy pole dla gry w tic-tac-toe. Pole - lista z liczbami od 1 do 9. Aby utworzyć pole, użyjemy funkcji range() 
board = list(range(1,10))   

# Funkcja wyświetla nasze pole w znanym formacie 3x3
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")    #tu robimy właśnie te polę, 3 slupki z ogranicznikami oraz 3 kolumny z ogranicznikami 
        print ("-" * 13)

# Piszemy funkcję, która da użytkownikom możliwość wprowadzania danych do naszej gry.
def take_input(player_token):   # Funkcja take_iinput przyjmuje parametr player_token - kółko lub krzyżyk, w zaleznosci od tego, czyj ruch jest teraz
    valid = False
    while not valid:
        player_answer = input("Dokąd wstawiamy" + player_token + "? ")
        try:             # Używamy konstrukcji try/except oraz if/else, aby upewnić się, że wybrana komórka nie jest zajęta (ze w tym miejscu pozostaje wolna komórka do wpisania naszego znaku)
            player_answer = int(player_answer)
        except:
            print ("Nieprawidłowe wejście. Proszę podać liczbę!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Ta komórka już jest zajęta")
        else:
            print ("Nieprawidłowe wejście. Wpisz liczbę od 1 do 9 aby wykonać ruch.")

# Piszemy funkcję do sprawdzania pola gry i wyników przy których użytkownik otrzymuje zwycięstwo (sukces).
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))    #Stworzyliśmy tuple () ze zwycięskimi współrzędnymi i przeszliśmy przez nią pętlą for. Jeśli znaki we wszystkich trzech podanych komorkach są rowne, zwracamy zwycięski symbol, w przeciwnym przypadku zwracamy wartosć False
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# Pozostałó nam się utworzyć funkcję main, w której połączymy wszystkie opisane funkcje. Oraz warto pamiętać, że zwycięski symbol podczas rzutowania go na typ logiczny zwróci True
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:             # Czekamy aż zmienna "counter" będzie większa niż 4, aby uniknąć niepotrzebnego wywołania funkcji "check_win" (do 5 ruchu nikt nie może wygrać).  
            tmp = check_win(board)     # Zmienna tmp została utworzona, aby ponownie nie wywoływać funkcji "check_in", po prostu "zapamiętujemy" jej wartości i przy nieobchodności używamy w linii 52
            if tmp:
                print (tmp, "Win!")
                win = True
                break
        if counter == 9:
            print ("Draw!")   #gdy nikt nie uzyskał sukcesu
            break
    draw_board(board)

main(board)    # Możemy spokojnie zagrać
