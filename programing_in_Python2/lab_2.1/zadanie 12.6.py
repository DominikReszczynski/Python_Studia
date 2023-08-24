
def decToBin(number):
    return bin(number).replace("0b", "")

def decToHex(number):
    return hex(number).replace("0x", "")

try:
    number=int(input("podaj liczbę dziesiętną: "))
except:
    print("nie podałeś liczby")

print("liczba binarna z ",number, "to",decToBin(number))
print("liczba szesnastkowa z ",number, "to",decToHex(number))
########################################################################################################################
def binToHex (bin):
    try:
        bin_=int(bin,2) #zamiana str na int
        hex_=hex(bin_) #zamiana int bin na int hex
        return hex_.replace("0x","")
        #nie rozumiem tylko dla czego jak podasz od razu int do def to nie wyjdzie np. 1111 to 0xf jak wprowadzisz od razu int to wyjdzie 0x457
    except:
        return "nie podałeś bin"
def hexToBin (hex):
    try:
        hex_=int(hex,16)
        bin_=bin(hex_)
        return bin_.replace("0b","")
    except:
        return "nie podałeś hex"

binNumber=input("podaj liczbę w bin")
print(binToHex(binNumber))

hexNumber=input("podaj liczbę w hex")
print(hexToBin(hexNumber))

########################################################################################################################

def binToOct (bin):
    try:
        bin_=int(bin,2)
        oct_=oct(bin_)
        return oct_.replace("0o","")
    except:
        return "nie podałeś hex"

print(binToOct(binNumber))

