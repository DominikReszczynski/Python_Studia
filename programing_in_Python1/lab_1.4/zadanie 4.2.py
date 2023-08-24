"""Napisz program przy użyciu pętli while wyświetlający na ekranie liczby od 254 do 320, ale
niepodzielne przez 2 ale podzielne przez 5. Jak zmieni się program jeśli będziemy chcieli
wyświetlać tylko liczby ujemne z zakresu -320 do -254 ?"""
i=254
while i<320:
    if i%2!=0 and i%5==0:
        print(i)
    i+=1
print("------------------------------")
#-----------------------------------
j=-320
while j<-254:
    if j%2!=0 and j%5==0:
        print(j)
    j+=1