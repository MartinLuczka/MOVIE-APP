# Movie App

# importy proměnných jiných python files

import os

import math

from seznam_uzivatelu import uzivatele

from seznam_filmu import vsechny_filmy

from filmove_maratony import vsechny_maratony

oddelovac = "=" * 83 # grafický prvek v menu

odsazeni = "\n" * 30

sluzby = ("dostupné filmy", "detaily filmu", "doporuč film", "filmový maraton", "ohodnoť filmy") # dostupné služby

uzivatelske_jmeno = ""

# prvotní prostředí po zapnutí programu

print('''   
█▀▄▀█ █▀█ █░█ █ █▀▀   ▄▀█ █▀█ █▀█
█░▀░█ █▄█ ▀▄▀ █ ██▄   █▀█ █▀▀ █▀▀
      ''')

print("=" * 33)

uzivatel = input("Zadejte zde své uživatelské jméno:\n") # přihlášení, pokud je uživatel již v seznamu uživatelů

if not uzivatel in uzivatele:
    print(odsazeni)
    print("Nejste zde zaregistrován.")
    volba_registrace = input("Chcete se zaregistrovat? (ANO/NE)\n").lower() # Možnost registrace nového uživatele

    if volba_registrace == "ne":
        print(odsazeni)
        print("Dobře, mějte se pěkně. Program se ukončuje...")
        quit()

    elif volba_registrace == "ano":
        print(odsazeni)
        print("Dobře, jsme rádi, že máte zájem o naši aplikaci!\n")
        while bool(uzivatelske_jmeno) == False:  # uživatel nebude moct zadat prázdný string, bude muset mít aspoň nějaké uživatelské jméno
            uzivatelske_jmeno = input("Zadejte zde své nové uživatelské jméno:\n")
        uzivatele[uzivatelske_jmeno] = {
            "OBLIBENE_FILMY": [],
            "OBLIBENE_ZANRY": []
            }
        print(odsazeni)
        print("Ještě než se dostanete k funkcím naší aplikace, chtěli bychom Vás poznat lépe, aby pro Vás některé funkce byly funkčnější.\n")

        # Uživatel si bude moct personalizovat profil

        volba_zanru = input("Máte v tuto chvíli zájem o personalizování Vašeho účtu? (ANO/NE) (Pokud tuto akci neprovedete v tuto chvíli, program se Vás zeptá při zájmu použít určité funkce)\n").lower()

        if volba_zanru == "ne":
            print(odsazeni)
            print("Dobře, ostatní funkce naší aplikace můžete používat bez omezení.")

        elif volba_zanru == "ano": # Zvolit žánr si bude uživatel moct jen tady, takový EASTER EGG, pokud si tady své oblíbené filmy napíše, vypíší se mu v závěrečné zprávě
            print(odsazeni)
            print("Jaké jsou Vaše oblíbené filmy? Zadávejte filmy nejlépe celým jménem v angličtině.\n")
            print("Až budete chtít ze zadáváním skočnit, napište dvakrát za sebou 'stop' (bez mezery). Nejlépe zadejte alespoň jeden film.\n")
            while True:
                film = input("Zde zadejte svůj oblíbený film:\n")
                if film == "stopstop":
                    break
                uzivatele[uzivatelske_jmeno]["OBLIBENE_FILMY"].append(film)
            print(odsazeni)
            print("Abychom Vám mohli vhodně doporučovat filmy, tak by nás zajímalo, jaký typ filmů máte rádi.\n") # Uživatel si bude moct zvolit oblíbené žánry, podle kterých se mu poté doporučí filmy
            print("""
Při zadávání filmových žánrů vybírejte z těchto možností:
[komedie, muzikal, pohadka, drama, krimi, detektivka, western, akcni film, 
dobrodruzny film, thriller, horor, sci-fi, fantasy, historicky film, valecny film, 
zivotopisny film, romanticky film, mysteriozni, animak, rodinny film] (Pište bez diakritiky.)\n""")
            print("Výběr opět zastavíte zadáním 'stop' dvakrát po sobě (bez mezery). Zadejte alespoň jeden žánr.\n")
            while True:
                zanr = input("Zde zadejte svůj oblíbený žánr:\n").lower()
                if zanr == "stopstop":
                    break
                uzivatele[uzivatelske_jmeno]["OBLIBENE_ZANRY"].append(zanr)

        else:
            print(odsazeni)
            print("Někde nastala chyba...")
            print("Zkuste se přihlásit ještě jednou. Program se ukončuje...")
            quit()

    else:
        print(odsazeni)
        print("Někde nastala chyba...")
        print("Zkuste se přihlásit ještě jednou. Program se ukončuje...")
        quit()

elif uzivatel in uzivatele:
    print(odsazeni)
    print(f"Vítejte zpátky, {uzivatel}!")

# Menu hlavní nabídky

print("\n")
print(oddelovac, sep="\n")
print("Vítejte v naší filmové aplikaci!".upper().center(82), oddelovac,sep="\n")
print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")

vyber = input("Vyberte si jednu z našich služeb: (napište ji s diakritikou)\n") # službu musí uživatel napsat správně s diakritikou

if vyber in sluzby and vyber == "dostupné filmy": # Zde se vypíší všechny filmy ze souboru seznam_filmu
    print(odsazeni)
    print("VŠECHNY DOSTUPNÉ FILMY:\n")
    print("=" * 30)
    for film in vsechny_filmy.keys():
        print(film)
    print("=" * 30)

elif vyber in sluzby and vyber == "detaily filmu": # informace ze slovníku v souboru seznam_filmu se zde vypíší do poměrně pěkného textového výpisku platného pro každý film
    print(odsazeni)
    print("VŠECHNY DOSTUPNÉ FILMY:\n")
    print("=" * 30)
    for film in vsechny_filmy.keys():
        print(film)
    print("=" * 30)
    vyber_filmu = input("O jakém filmu se chcete něco dozvědět?\n")
    print(odsazeni)
    print(f"""
Vybraný film: {vyber_filmu}\n
Tento film pochází z roku {vsechny_filmy[vyber_filmu]["ROK"]}.
Režisérem filmu je {vsechny_filmy[vyber_filmu]["REZISER"]}.
Žánry, do kterých se film může řadit: {", ".join(vsechny_filmy[vyber_filmu]["ZANR"])}
Film vás bude bavit po dobu {vsechny_filmy[vyber_filmu]["STOPAZ"]} minut, což je/jsou {math.floor((vsechny_filmy[vyber_filmu]["STOPAZ"])/60)} hodina/hodiny a {((vsechny_filmy[vyber_filmu]["STOPAZ"])%60)} minut.
Ve filmu se můžete těšit na tyto herce: {", ".join(vsechny_filmy[vyber_filmu]["HRAJI"])}
Zde se můžete podívat na hodnocení publika na nejpopulárnějších recenzních webech:
ČSFD: {vsechny_filmy[vyber_filmu]["HODNOCENI"]["ČSFD"]}
IMDb: {vsechny_filmy[vyber_filmu]["HODNOCENI"]["IMDb"]}
Kinobox: {vsechny_filmy[vyber_filmu]["HODNOCENI"]["Kinobox"]}
Rotten Tomatoes: {vsechny_filmy[vyber_filmu]["HODNOCENI"]["Rotten_Tomatoes"]}
""")
    
elif vyber in sluzby and vyber == "doporuč film": # Doporučí všechny filmy, které splňují zadané žánry. Pokud si uživatel nepersonalizoval profil již na začátku, aplikace ho o to požádá teď
    if uzivatelske_jmeno != "":
        if bool(uzivatele[uzivatelske_jmeno]["OBLIBENE_ZANRY"]) == False:
            print(odsazeni)
            print("Abychom Vám mohli vhodně doporučovat filmy, tak by nás zajímalo, jaký typ filmů máte rádi.\n")
            print("""
Při zadávání filmových žánrů vybírejte z těchto možností: 
[komedie, muzikal, pohadka, drama, krimi, detektivka, western, akcni film, 
dobrodruzny film, thriller, horor, sci-fi, fantasy, historicky film, valecny film, 
zivotopisny film, romanticky film, mysteriozni, animak, rodinny film] (Pište bez diakritiky.)\n""")
            print("Výběr opět zastavíte zadáním 'stop' dvakrát po sobě (bez mezery). Zadejte alespoň jeden žánr.\n")
            while True:
                zanr = input("Zde zadejte svůj oblíbený žánr:\n").lower()
                if zanr == "stopstop":
                    break
                uzivatele[uzivatelske_jmeno]["OBLIBENE_ZANRY"].append(zanr)

        print(odsazeni)
        print("Podle Vašeho výběru žánrů by Vás mohli zajímat tyto filmy:\n")
        if bool(uzivatele[uzivatelske_jmeno]["OBLIBENE_ZANRY"]) == False: # Pokud uživatel nic nezadá, aplikace se ukonční
            print(odsazeni)
            print("Omouváme se, ale bez zadání aspoň jednoho žánru Vám vhodně nemůžeme doporučit žádný film, zkuste to ještě jednou. Program se ukončuje...")
            quit()
        print("=" * 30) # Grafické zpracování vypsání filmů
    
        # Kód, který zajistí nalezení filmu podle oblíbeného žánru uživatele

        for key in vsechny_filmy.keys():
            for film in vsechny_filmy[key]["ZANR"]:
                for oblibeny_zanr in uzivatele[uzivatelske_jmeno]["OBLIBENE_ZANRY"]:
                    if film == oblibeny_zanr:
                        print(key)
        print("=" * 30)

    elif uzivatelske_jmeno == "": # tento kód pracuje s oblíbenými žánry zadanými ručně již do souboru seznam_uzivatelu
        print(odsazeni)
        print("Podle Vašeho výběru žánrů by Vás mohli zajímat tyto filmy:\n")
        print("=" * 30)
        for key in vsechny_filmy.keys():
            for film in vsechny_filmy[key]["ZANR"]:
                for oblibeny_zanr in uzivatele[uzivatel]["OBLIBENE_ZANRY"]:
                    if film == oblibeny_zanr:
                        print(key)
        print("=" * 30)

elif vyber in sluzby and vyber == "filmový maraton": # Podle dostupného času uživatele se vybere, co nejvhodnější filmová série, aby uživatelovi zbylo co nejméně času "nicnedělání", tento zbývající čas se vypíše
    print(odsazeni)
    print("V této funkci se Vám budeme snažit doporučit, co nejvhodnější maraton filmů do Vašeho časového limitu. Nejmenší možná doba jsou 4 hodiny a 24 minut.\n")
    cas_uzivatele_hodiny = int(input("Kolik máte hodin na sledování filmů? (zatím zadejte pouze celočíselně hodiny číslem)\n"))
    cas_uzivatele_minuty = int(input("Máte k těm hodinám ještě nějaký počet minut, kolik? (zadejte čísleně)\n"))
    cas_uzivatele = (cas_uzivatele_hodiny*60) + cas_uzivatele_minuty

    # algoritmus výběru filmu

    novy_cas = 1000000 # přehnaně vysoké číslo pro splnění počáteční podmínky
    finalni_maraton = ""

    for maraton in vsechny_maratony.keys():
        zbyly_cas = cas_uzivatele - vsechny_maratony[maraton]["STOPAZ"]
        if zbyly_cas >= 0 and zbyly_cas < novy_cas:
            novy_cas = zbyly_cas
            finalni_maraton = maraton

    if bool(finalni_maraton) == True:

        print(odsazeni)
        print(f"""
S Vámi dostupných časem krásně stihnete zhlédnout tuto sérii filmů: 
{"=" * 30}        
{finalni_maraton}
{"=" * 30}
Pro tento maraton zhlédnete tyto filmy:
        """)
        filmy = vsechny_maratony[finalni_maraton]["FILMY"]
        for film in filmy:
            print(film)
        print("=" * 30)
        print(f"Zbyde Vám ještě krásný počet minut: {novy_cas}\n")

    else: # Pokud uživatel zadá moc krátký čas pro jakoukoliv sérii
        print(odsazeni)
        print("S Vámi zadaných časem žádný pořádný maraton nestihnete.")

elif vyber in sluzby and vyber == "ohodnoť filmy": # Uživatel si bude moct vybrat, které filmy ohodnotí a které neohodnotí, jeho odpovědi se mu graficky zpracují do textového dokumentu
    print(odsazeni)
    print("V této funkci budete moct ohodnit všechny dostupné filmy v této aplikaci.\n")
    print("Projdete všechny filmy a napíšete číslo x v předpisu x/100. Pokud jste film neviděli nebo ho nebudete chtít hodnotit, napište cokoliv kromě číslic.\n")
    for film in vsechny_filmy.keys():
        hodnoceni = input(f"Ohodnoťte tento film: {film}\n").lower()
        vsechny_filmy[film]["HODNOCENI_UZIVATELE"] = ""
        if hodnoceni.isdigit() == True:
            hodnoceni = int(hodnoceni)
            vsechny_filmy[film]["HODNOCENI_UZIVATELE"] = f"{hodnoceni}/100"

    # vyhodnocení hodnocení do textového dokumentu
    
    print(odsazeni)
    print("Vaše hodnocení bude přepsáno do textového dokumentu.")
    
    with open ("hodnoceni_uzivatele.txt", "w") as file:
        file.write("MOVIE APP\n")
        file.write("=" * 33 + "\n")
        if bool(uzivatelske_jmeno) == True:
            file.write(f"Hodnocení uživatele: {uzivatelske_jmeno}\n")
        else:
            file.write(f"Hodnocení filmů uživatele: {uzivatel}\n")
        file.write("=" * 30 + "\n")
        for film in vsechny_filmy.keys():
            if bool(vsechny_filmy[film]["HODNOCENI_UZIVATELE"]) == True:
                file.write(f"{film}: {vsechny_filmy[film]['HODNOCENI_UZIVATELE']}\n")
        if bool(uzivatelske_jmeno) == False:
            if bool(uzivatele[uzivatel]["OBLIBENE_FILMY"]) == True:
                file.write("=" * 30 + "\n")
                file.write("Oblíbené filmy uživatele:\n")
                file.write("=" * 30 + "\n")
                for film in uzivatele[uzivatel]["OBLIBENE_FILMY"]:
                    file.write(f"{film}\n")
        else:
            if bool(uzivatele[uzivatelske_jmeno]["OBLIBENE_FILMY"]) == True:
                file.write("=" * 30 + "\n")
                file.write("Oblíbené filmy uživatele:\n")
                file.write("=" * 30 + "\n")
                for film in uzivatele[uzivatelske_jmeno]["OBLIBENE_FILMY"]:
                    file.write(f"{film}\n")

else: # Uživatel špatně vybere (asi většinou napíše) název služby
    print(odsazeni)
    print("Něco se pokazilo...Taková služba není na výběr (zkontrolujte si diakritiku). Program se ukončuje...")
    quit()

print("Děkujeme za použití naší aplikace!")
print("Pro použití jiné funkce se znovu přihlašte. Program se ukončuje...")
quit()