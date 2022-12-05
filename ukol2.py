def ukol2(klíč, hodnota, slovník):
    try:
        if hodnota == slovník[klíč]:
            return True
        else:
            return False
    except KeyError:   
        print("Klíč neexistuje")
        return False


slovník = {"ahoj":"hello" }

print(ukol2("ahoj","hello", slovník))
print(ukol2("ahoj","hola", slovník))
print(ukol2("hola","hello", slovník))