napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]

indul = int(input("Adja meg annak a napnak a számát amikor indult:"))

ido = int(input("Hány napig voltál oda?:"))

a = ido % 7

if (indul + a) < 7:
    print("Ezen a napon érsz haza:", napok[indul + a])
else:
    print("Ezen a napon érsz haza:", napok[(indul + a) - 7])