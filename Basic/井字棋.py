# coding:utf-8
import re
firstLetter   ='X'
secondLetter  ="O"
currentLetter ='X'
boardContent  =[["7","8","9"],["4","5","6"],["1","2","3"]]
def drawBoard():
	def drawBoardTop():
		print "		-------------------",
	def drawBoardRow(row):
		borad= """
		|     |     |     |
		|  %s  |  %s  |  %s  |
		|     |     |     |
		-------------------"""
		print borad%(boardContent[row][0],boardContent[row][1],boardContent[row][2]),
	drawBoardTop()
	drawBoardRow(0)
	drawBoardRow(1)
	drawBoardRow(2)
	print ""
def judge():

	board = boardContent[0]+boardContent[1]+boardContent[2]
	
	def judgeRow(n):
		return boardContent[n][0] == boardContent[n][1] == boardContent[n][2]
	def judgeCol(n):
		return boardContent[0][n] == boardContent[1][n] == boardContent[2][n]
	def judgeAngle45():
		return boardContent[0][0] == boardContent[1][1] == boardContent[2][2]
	def judgeAngle135():
		return boardContent[0][2] == boardContent[1][1] == boardContent[2][0]

	for i in range(0,3):

		if judgeRow(i):
			return boardContent[i][0]
		elif judgeCol(i):
			return boardContent[0][i]
	else:
		if judgeAngle45():
			return boardContent[0][0]
		elif judgeAngle135():
			return boardContent[1][1]
		else:
			if board.count(firstLetter) + board.count(secondLetter) < 9:
				return None
			else:
				return "P"

def first():
	x=raw_input("Please select %s or %s(%s first)"%(firstLetter,secondLetter,firstLetter))
	while  x!="X" and x!="O":
		x=raw_input("Please select %s or %s(%s first)"%(firstLetter,secondLetter,firstLetter))
	else:
		currentLetter=x

def used(x):
	letter = boardContent[(9 - int(x))/3][2 - (9 - int(x))%3]
	return letter == firstLetter or letter == secondLetter


def run():
	drawBoard()
	first()
	global currentLetter
	while (not judge()):
		x=raw_input(" %s run (1-9)"%(currentLetter))
		while ( not re.match(r"^[1-9]{1}$",x) or used(x)):
			x=raw_input(" %s run (1-9)"%(currentLetter))
		
		boardContent[(9 - int(x))/3][2 - (9 - int(x))%3] =currentLetter

		if currentLetter == firstLetter:
			currentLetter = secondLetter
		else:
			currentLetter = firstLetter

		drawBoard()
	else:
		 result = judge()
		 if result =="P":
		 	print "平手,你们太牛了!"
		 else:
		 	print result+" 胜!"



if __name__=="__main__"	:
	run()
