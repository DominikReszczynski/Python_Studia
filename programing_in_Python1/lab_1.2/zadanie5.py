"""Zadanie5.Napisz program „symulator badania alkomatem”,
który po podaniu odpowiednich wartości w wydychanym powietrzu
(zgodnie z przepisami prawa) wskaże stan nietrzeźwości i stan  po użyciu
alkoholu zgodniez przepisami prawa."""
promil=(float(input("podaj ile promili posiada kierowca w wydychanym powietrzu: ")))
if promil>=0.2 and promil<=0.5:
    print("Stan po spożyciu alkoholu")
elif promil>0.5:
    print("stan nietrzeźwości")
else:
    print("chyba trzeźwy ale uważaj")
