#Napisz program wyświetlający trójkąt prostokątny z gwiazdek (*, **, *** itp.). W „podstawie” ma być 5 gwiazdek nie 8
number_base=5
line = ''
for i in range(number_base):
    for j in range(i+1):
        line += "*"
    print(line)
    line=""