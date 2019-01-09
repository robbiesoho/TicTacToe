#! python

""" This my Tic Tac Toe game with python.

2018-12-10
"""
import random

board = [1,2,3,4,5,6,7,8,9]
board_copy = [1,2,3,4,5,6,7,8,9]
open_boxes = 9
human_letter = ''
opp_letter = ''

def choose_letter():  
    global human_letter
    global opp_letter
    human_letter = input('Please choose "x" or "o": ').lower()
    if human_letter == 'x':
        opp_letter = 'o'
    elif human_letter == 'o':
        opp_letter = 'x'
    else:
        print('Please choose again.')
        choose_letter()
        
def show_board():
    print (board[0], '|', board[1], '|', board[2])
    print ("----------")
    print (board[3], '|', board[4], '|', board[5])
    print ("----------")
    print (board[6], '|', board[7], '|', board[8])
    print (" ")

def checkLine(char, first, second, third):
    if board[first] == char and board[second] == char and board[third] == char:
        return True

def checkAll(char):
    #Check for winning condtions
    if checkLine(char,0,1,2):
        return True
    if checkLine(char,3,4,5):
        return True
    if checkLine(char,6,7,8):
        return True
    if checkLine(char,0,3,6):
        return True
    if checkLine(char,1,4,7):
        return True
    if checkLine(char,2,5,8):
        return True
    if checkLine(char,0,4,8):
        return True
    if checkLine(char,2,4,6):
        return True


    

def computer_move():
        global open_boxes
        if open_boxes > 0:
            opp_move = random.randint(0,8)
            if board[opp_move] != 'o' and board[opp_move] != 'x':
                open_boxes -= 1
                board[opp_move] = opp_letter
                print('Computer\'s turn')
                print('Computer is thinking...')
                print('\n')
                show_board()            
            else:
                computer_move()
        else:
            print('--DRAW--')
            

def human_first():
    global open_boxes
    if open_boxes > 0:
        while True:
            move = input('Please pick a number from 1 - 9: ')
            move = int(move) - 1   
            winner = False
                
            if board[move] != 'x' and board[move] != 'o':
                board[move] = human_letter
                open_boxes -= 1
                show_board()
                
            else:
                print('\n')
                print('Sorry that space is taken. Try again')
                print('\n')
                show_board()
                human_first()
            
            if checkAll(human_letter) == True:
                winner = True
                print ("--HUMAN WINS--")
                print ('\n')
                play_again()
                break;
                      
            computer_move()
                   
            if checkAll(opp_letter) == True:
                winner = True
                print ("--COMPUTER WINS--")
                print ('\n')
                play_again()
                break;
    else:
        print('--DRAW--')
        play_again()

def computer_first():
    global open_boxes
    if open_boxes > 0:
        computer_move()
        while True:
            move = input('Please pick a number from 1 - 9: ')
            move = int(move) - 1   
            winner = False
                
            if board[move] != 'x' and board[move] != 'o':
                board[move] = human_letter
                open_boxes -= 1
                show_board()
                
            if checkAll(human_letter) == True:
                winner = True
                print ("--HUMAN WINS--")
                print ('\n')
                play_again()
                break;
                      
            computer_move()
                   
            if checkAll(opp_letter) == True:
                winner = True
                print ("--COMPUTER WINS--")
                print ('\n')
                play_again()
                break;
    else:
        print('--DRAW--')
        play_again()
        
def who_goes_first():
    print ('\n')
    print('The first player will be chosen at random.')
    print('...')
    first = random.randint(0,1)
    if first == 1:
        print('Human goes first')
        human_first()
    else:
        print('Computer goes first')
        computer_first()

def play_again():
    global board
    global board_copy
    print('Do you want to play again?: ')
    answer = input().lower()
    if answer in ('y','ye','yes'):
        board = board_copy
        who_goes_first()
    else:
        print('Hope you enjoyed the game!')
        
print ('Welcome to Tic Tac Toe!This is your game board: ')
print ('\n')
show_board()
choose_letter()
who_goes_first()
