login_and_password={"admin":"admin","jaś":"fasola","stachu":"jons","ania":"cwaniara","tadeusz":"wajche_przełóż","python":"c++"}
login=input("podaj login: ")
password=input("podaj hasło: ")
try:
    if login_and_password[login]==password and login=="admin" and password=="admin":
        print("witamy po ciemniej stronie!!! Tam jest pijalnia piwa i wódki a tam azazel goni lucyfera!!!")
    elif login_and_password[login]==password and login!="admin" and password!="admin":
        print('Witamy po jsanej stronie tu latją aniołki a tam Bozia chodzi ')
except:
    print("to nie działa, nie mam takiego konta")
