def intToRoman(number):
    try:
        intTab=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
        romaTab=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        romaNum=""
        tabControl=0
        while number>0:
            for loop in range(number//intTab[tabControl]):
                romaNum+=romaTab[tabControl]
                number-=intTab[tabControl]
            tabControl+=1
        return romaNum
    except:
        return "nie mogę tego zamienić"
def romaToInt(number):
    try:
        romaLibry={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        tabControl=0
        totalNumber=0
        while tabControl<len(number):
            str_1=romaLibry[number[tabControl]]
            if (tabControl+1<len(number)):
                str_2=romaLibry[number[tabControl]]
                if (str_1>=str_2):
                    totalNumber+=str_1
                    tabControl+=1
                else:
                    totalNumber-=str_1
                    tabControl+=1
            else:
                totalNumber+=str_1
                tabControl+=1
            return totalNumber
    except:
        return "nie mogę tego zamienić"
numberFirst=int(input("podaj pierwszą liczbę dziesiętną by zamienić na roma: "))
print(intToRoman(numberFirst))
numberSecond=input("podaj liczbę w: I:1,V:5,X:10,L:50,C:100,D:500,M:1000 żeby zamienić ją na intiger: ")
numberSecond=numberSecond.upper()
print(romaToInt(numberSecond))
