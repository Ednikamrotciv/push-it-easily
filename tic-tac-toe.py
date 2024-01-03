def drawfield(field):
    for row in range(5):# 01234
        if row%2==0: # if range is divisible by 2 then it gives 0 then row
            #print vertical line
            practicalrow= int(row/2)#012
            for column in range(5):
                if column%2==0:
                    practicalcolumn= int(column/2)
                    if column!=4:# if column is not 4 print|
                        print(field[practicalcolumn][practicalrow],end='')
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print('|', end='')
        else:
            print('-----')
player=1
currentfield=[[' ', ' ',' '],[' ', ' ', ' '],[' ', ' ', ' ']]#columns
drawfield(currentfield)#linking drawfield to currentfield
while(True):
    print('players turn: ',player)
    moverow=int(input('please input row\n'))
    movecolumn=int(input('please input column\n'))
    if player==1:
        #make move for player1
        if currentfield[moverow][movecolumn]==' ':
            currentfield[moverow][movecolumn]='x' #player1
            player=2
    else:
        #make move for player2
        if currentfield[moverow][movecolumn]==' ':
            currentfield[moverow][movecolumn]='o' #player2
            player=1
    drawfield(currentfield) #linking
