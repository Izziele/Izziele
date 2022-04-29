#Izzie Le

#This project's goal is to using data list to suggest the user a list of matched school base on their GPA and SAT, if they doesn't
#interested in the list but have another school in their mind, I will suggest what they need to improve and by how much to get
#them into that school. An admission chance graph will be given with their current standing.

#all the code in this project is mine


import csv
import turtle
import random

def makeDataList(dataName):
    dataList = []
    with open('finalprojectdata.csv', encoding="ISO-8859-1") as dataFile:
        csvReader = csv.reader(dataFile)
        titles = next(csvReader)
        colNum = 0
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum = colNum + 1
        if colNum >= len(titles):
            print(dataName,"is not found")
        else:
            for lines in csvReader:
                dataList.append(lines[colNum])
        return dataList
schoolList = makeDataList("SCHOOL NAME")
satList = makeDataList("25th")
gpaList = makeDataList("GPA")
accList = makeDataList("acc rate")
avesatList = makeDataList("Average")
abovsatList = makeDataList("75th")

lst = []
for i in range(len(satList)):
    lst.append(gpaList[i])
    lst.append(satList[i])
    lst.append(avesatList[i])
    lst.append(abovsatList[i])
    lst.append(accList[i])

n = 5
scoreList = [lst[k:k+n] for k in range(0, len(lst), n)]

myDict = {}
for i in range(len(schoolList)):
    myDict[schoolList[i]]=scoreList[i]

usergpa = input("Enter your GPA: ")
usersat = input("Enter your SAT: ")
userScore = [usersat,usergpa]

def findSchool(userScore):
    suggestList = []
    for keys in myDict:
        scoreVal = myDict[keys]
        if userScore[0] > scoreVal[1] and userScore[1] > scoreVal[0]:
            suggestList.append(keys)
    return suggestList
print(findSchool(userScore))

quest = input("Have you satisfy with this school list? ")
if quest == "yes":
    print("Sound good! Good luck!!!")
    quit()
elif quest == "no":
    print("It's ok, let's try another thing!")
else:
    print("Please enter yes/no answer")

myDreamSchool = input("Enter the college's name: ")
def dreamSchool(userScore):
    if myDreamSchool in schoolList:
        scoreVal = myDict[myDreamSchool]
        if usersat < scoreVal[1]:
            satImprove = float(scoreVal[1])-float(userScore[0])
            print("You need to improve your SAT at least by",satImprove)
        else: 
            print("Your SAT is at good standing")
        
        if usergpa < scoreVal[0]:
            gpaImprove = float(scoreVal[0])-float(userScore[1])
            print("You need to improve your GPA at least by",gpaImprove)
        else:
            print("Your GPA is good standing")
    else:
        print("Sorry, your college is not found!")
dreamSchool(userScore) 

wn = turtle.Screen()
wn.tracer(0,0)
wn.bgcolor("light cyan")
chartT = turtle.Turtle()
wn.setworldcoordinates(-1,-1,801,6) 
chartT.hideturtle() 

chartT.up() 
chartT.goto(0,0) 
chartT.down()
chartT.goto(800,0) 
chartT.up()
chartT.goto(0,0)
chartT.down()
chartT.goto(0,5)
chartT.up()

chartT.goto(-50,0)
chartT.write("0",font=("Helvetica",16,"bold")) 
chartT.goto(-50,4.8)
chartT.write("5",font=("Helvetica",16,"bold"))

chartT.goto(0,-0.6)
chartT.write("800",font=("Helvetica",16,"bold")) 
chartT.goto(780,-0.6)
chartT.write("1600",font=("Helvetica",16,"bold"))

chartT.goto(0,0)
chartT.goto(int(usersat)-800,float(usergpa))
chartT.down()
chartT.color("blue")
chartT.dot()
wn.update()
chartT.up()

#     gpa = scoreVal[0]
#     belowsat = scoreVal[1]
#     aversat = scoreVal[2]
#     abovesat = scoreVal[3]
#     acceptance = scoreVal[4]

def drawing(num):
    ScoreVal = myDict[myDreamSchool]
    abovesat = int(ScoreVal[3])-800
    avesat = int(ScoreVal[2])-800
    acceptNum = (num/100)*float(ScoreVal[4])
    _75percentacc = ((acceptNum/100)*75)//1
    _25percentrej = acceptNum - _75percentacc
    _50percentacc = ((acceptNum/100)*50)//1
    _50percentrej = acceptNum - _50percentacc
    _25percentacc = ((acceptNum/100)*25)//1
    _75percentrej = acceptNum - _25percentacc
    _100percentrej =  (_75percentrej + _25percentacc)//1
    for i in range(int(_75percentacc)):
        x1 = random.randint(int(ScoreVal[3])-800,800)
        y1 = random.uniform(float(ScoreVal[0]),5)
        chartT.goto(x1,y1)
        chartT.color("green")
        chartT.dot()
    for i in range(int(_25percentrej)):
        x1 = random.randint(int(ScoreVal[3])-800,800)
        y1 = random.uniform(float(ScoreVal[0]),5)
        chartT.goto(x1,y1)
        chartT.color("red")
        chartT.dot()
    for i in range(int(_50percentacc)):
        x1 = random.randint(int(ScoreVal[2])-800,abovesat)
        y1 = random.uniform(2,float(ScoreVal[0]))
        chartT.goto(x1,y1)
        chartT.color("green")
        chartT.dot()
    for i in range(int(_50percentrej)):
        x1 = random.randint(int(ScoreVal[2])-800,abovesat)
        y1 = random.uniform(2,float(ScoreVal[0]))
        chartT.goto(x1,y1)
        chartT.color("red")
        chartT.dot()
    for i in range(int(_25percentacc)):
        x1 = random.randint(int(ScoreVal[1])-800,avesat)
        y1 = random.uniform(0,float(ScoreVal[0]))
        chartT.goto(x1,y1)
        chartT.color("green")
        chartT.dot()
    for i in range(int(_75percentrej)):
        x1 = random.randint(int(ScoreVal[1])-800,avesat)
        y1 = random.uniform(0,float(ScoreVal[0]))
        chartT.goto(x1,y1)
        chartT.color("red")
        chartT.dot()
    for i in range(int(_100percentrej)):
        x1 = random.randint(0,int(ScoreVal[1])-800)
        y1 = random.uniform(0,float(ScoreVal[0])-1.5)
        chartT.goto(x1,y1)
        chartT.color("red")
        chartT.dot()
    wn.update()
drawing(300)
    