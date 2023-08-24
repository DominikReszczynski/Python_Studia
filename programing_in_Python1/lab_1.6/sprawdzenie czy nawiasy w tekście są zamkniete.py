slowo="abcdefg([]}{}"
tab=["a"]
okrongly=0
dziubek=0
kwadrat=0
"""if "(" in slowo:
    a=slowo.find("(")
    b=slowo.find(")")
    if a<b:
        print("jest tutaj () zamyka się")
        okrongly+=1
    else:
        print("nie zamyka się")
if "{" in slowo:
    a=slowo.find("{")
    b=slowo.find("}")
    if a<b:
        print("jest tutaj {} zamyka się")
        dziubek+=1
    else:
        print("nie zamyka się")
if "[" in slowo:
    a=slowo.find("[")
    b=slowo.find("]")
    if a<b:
        print("jest tutaj [] zamyka się")
        kwadrat+=1
    else:
        print("nie zamyka się")"""
'''for i in slowo:
    tab.append(i)
print(tab)
for i in range (1,len(tab)):
    if tab[i]==")" or tab[i]=="}" or tab[i]=="]":
        if tab[i-1]=="(" or tab[i-1]=="[" or tab[i-1]=="{":
            print('tak')
        else:
            print("nie")
            break
    else:
        print('idę dalej')'''

class sklad:
    def __init__(self):
        self.items = []

    def jest_pusty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

def sprawdzenie(wyraz):
    s = sklad()
#####################################
    for i in wyraz:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.jest_pusty():
                return False
            else:
                s.pop()
#####################################
    for i in wyraz:
        if i == '{':
            s.push(i)
        elif i == '}':
            if s.jest_pusty():
                return False
            else:
                s.pop()
####################################
    for i in wyraz:
        if i == '[':
            s.push(i)
        elif i == ']':
            if s.jest_pusty():
                return False
            else:
                s.pop()
    return s.jest_pusty()
####################################

