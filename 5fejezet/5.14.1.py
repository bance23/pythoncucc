napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]

n = int(input("Írja be a nap számát:"))

def fuggveny(n):
    return (napok[n])

print("A megadott szám napja:", fuggveny(n))