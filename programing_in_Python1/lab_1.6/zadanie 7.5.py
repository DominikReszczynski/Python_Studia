'''Utwórz dwie krotki w których zadeklarujesz dwa wyrazy. Sprawdź czy są one anagrami – czy
dwa słowa składają się z tych samych liter. Zaproponuj przykładowe wyrazy, które będą
prawidłowymi rozwiązaniami zadania.'''
tuple1=('jak',)
tuple2=('kajak',)

#def anagram(first_word, second_word):
#    if (sorted(first_word)== sorted(second_word)):
#        print("słowo:",first_word,"oraz słowo:",second_word,"są anagramami")
#    else:
#        print("słowo:",first_word,"oraz słowo:",second_word,"nie są anagramami")
first_word=tuple1[0]
second_word=tuple2[0]
print(first_word)
print(second_word)
print("---------------------------------------------------------------------")
#anagram(first_word,second_word)
def anagram2(first_word,second_word):
    tab_count_number=[]
    if len(second_word)>=len(first_word):
        print('słowo 2 jest większe')
        for i in second_word:
            num=first_word.count(i)
            tab_count_number.append(num)
        if tab_count_number.count(0)==0:
            print("słowa mają takie same litery")
        else:
            print("słowa mają różne litery")
    else:
        print('słowo 1 jest większe')
        for i in first_word:
            num=second_word.count(i)
            tab_count_number.append(num)
        if tab_count_number.count(0)==0:
            print("słowa mają takie same litery")
        else:
            print("słowa mają różne litery")
first_word = tuple1[0]
second_word = tuple2[0]
anagram2(first_word,second_word)