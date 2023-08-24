#zadanie 6.Oblicz średnią prędkość jazdy samochodu, który dystans 30km
#pokonał w 15 minut. Wynik podaj w km/h.  O ile wynik się zmieni jeśli
#kolejne 30 km przejechał 12 minut? Z jaką średnią prędkością przejechał
#samochód cały dystans?
dystans=[30,30,60] #km
czas=[15,12,27] #minuty
wynik=[]
for i in range(len(czas)):
    h=czas[i]/60
    km_h=dystans[i]/h
    km_h=round(km_h,0)
    print("dystans",dystans[i],"km,",czas[i],"min, prędkość to:",km_h)

