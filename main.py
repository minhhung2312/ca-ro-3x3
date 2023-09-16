import random

#Vẽ bàn cờ:
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

#Cho phép người chơi chọn X hoặc O:
def inputPlayerLetter():
    #Cho phép người dùng nhập ký tự:
    #Trả vế tập hợp với ký tự của người chơi là phần tử đầu tiên và ký tự của máy tính là phần tử thứ 2
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")
        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']
    
#Quyết định xem ai là người đi trước:
def whoGoesFirst():
    #Chọn bất kỳ ngẫu nhiên cho phép người chơi đi trước hay không:
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
#Vẽ ký tự lên bàn cờ:
def makeMove(board, letter, move):
    board[move] = letter

#Kiểm tra người chơi thắng hay chưa:
def isWinner(bo, le):
    #Trả về True nếu người chơi thắng:
    #Sử dụng bo thay vì thay đầy đủ là board và le là viết tắt của letter;
    return ((bo[7] == le and bo[8] == le and bo[9] == le)or #Một hàng trên cùng
            (bo[4] == le and bo[5] == le and bo[6] == le)or #Một hàng ở giữa
            (bo[1] == le and bo[2] == le and bo[3] == le)or #Một hàng ở cuối
            (bo[7] == le and bo[4] == le and bo[1] == le)or #Cột bên trái
            (bo[8] == le and bo[5] == le and bo[2] == le)or #Cột ở giữa
            (bo[9] == le and bo[6] == le and bo[3] == le)or #Cột bên phải
            (bo[7] == le and bo[5] == le and bo[3] == le)or #Đường chéo
            (bo[9] == le and bo[5] == le and bo[1] == le)) #Đường chéo

#Sao chép dữ liệu của Board:
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

#Kiểm tra xem ô trên bàn cờ còn hay không:
def isSpaceFree(board, move):
    #Trả về True nếu nước đi vẫn còn trên bàn cờ:
    return board[move] == ' '

#Cho phép người chơi nhập một bước đi:
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

#Chọn một bước đi từ tập hợp các bước đi:
def chooseRandomMoveFromList(board, movesList):
    #Trả về nước đi hợp lệ từ tập hợp được truyền vào:
    #Trả về None nếu không còn nước đi hợp lệ
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
#Tạo đoạn mã AI cho máy tính:
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'
    #Kiểm tra xem máy tính có thể thắng trong một bước đi hay không
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    
    #Kiểm tra xem người chơi có thắng trong một bước nào đó hay không
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i ):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
            
    #Kiểm tra các ô ở các góc, ở giữa trung tâm và các bên xem còn trống rỗng hay không
    move  = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    #Nếu ở góc không còn trống hãy kiểm tra ở giữa: số 5
    if isSpaceFree(board, 5):
        return 5
    
    #Chọn một trong các nước đi ở các cạnh bên của bàn cờ
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

#Kiểm tra bàn cờ đã đầy hay chưa:
def isBoardFull(board):
    #Trả về True nếu không còn nước đi trên bàn cờ, nếu không trả về False
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic Tac Toe!")

while True:
    theBoard = [' ']*10
    #Vòng lặp trò chơi:
    playerLetter, computerLetter = inputPlayerLetter()

    #Hàm whoGoesFirst quyết định ai đi trước:
    turn = whoGoesFirst()
    print("The " + turn + "will go first.")
    gameIsPlaying = True

    #Thực hiện lượt của người chơi:
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            #Kiểm tra người chơi có thắng hay không
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            
            #Nếu người chơi không thắng, có thể bàn cờ bị lấp đầy, kiểm tra bàn cờ:
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        #Thực hiện lượt chơi của máy:
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The  computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    #Kiểm tra họ muốn chơi nữa không:
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break



