from human import Worker, Normalperson
from mall import Mall, Gencemall,Genclikmall,Denizmall,Aygunmall,Iyirmisekkizmall
from movie import Hours,Movie
from movie import Ghajini,Ayla,Suzume,Spidarman,VeerZaara,DDLJ,Fanaa,Peekay,Threeidiots,Devdas
from money import Money

print('''
Write your personel information!

1)Worker or any emploee? 
2)Normal person? 
''')

try:
   personselection=int(input("Selection: "))
except:
    "Enter valid value"
if personselection==1:
    print(Worker.who())
elif personselection==2:
    print(Normalperson.who())



print('''
Selection mall:

1)Genclik mall? 
2)Gence mall? 
3)Deniz mall? 
4)Iyirmi sekkiz mall? 
5)Aygun mall? 
''')
try:
   mallselection=int(input("Selection: "))
except:
    "Enter valid value"


if mallselection==1:
    genclik=Genclikmall("Genclik",4,5)
    genclik.working_time()
    print(genclik.person_age(int(input("How old are you?\n(Can't enter under 14 years old): "))))
    print(genclik.vaksinasiya(input("You have been vaccinated?\nYes or No\n")))
    genclik.information()
elif mallselection==2:
    gence = Gencemall("Gence", 5, 7)
    gence.working_time()
    print(gence.person_age(int(input("How old are you?\nCan't enter under 14 years old: "))))
    print(gence.vaksinasiya(input("You have been vaccinated?\nYes or No\n")))
    gence.information()
elif mallselection==3:
    deniz=Denizmall("Sahil", 3, 7)
    deniz.working_time()
    print(deniz.person_age(int(input("How old are you?\nCan't enter under 14 years old: "))))
    print(deniz.vaksinasiya(input("You have been vaccinated?\nYes or No\n")))
    deniz.information()
elif mallselection==4:
    iyirmisekkiz= Iyirmisekkizmall("Iyirmisekkiz", 4, 8)
    iyirmisekkiz.working_time()
    print(iyirmisekkiz.person_age(int(input("How old are you?\nCan't enter under 14 years old: "))))
    print(iyirmisekkiz.vaksinasiya(input("You have been vaccinated?\nYes or No\n")))
    iyirmisekkiz.information()
elif mallselection==5:
    aygun=Aygunmall("Bakixanov", 5, 9)
    aygun.working_time()
    print(aygun.person_age(int(input("How old are you?\nCan't enter under 14 years old: "))))
    print(aygun.vaksinasiya(input("You have been vaccinated?\nYes or No\n")))
    aygun.information()

print('''
Selection film:

1) Ghajini? 
2) Ayla? 
3) Suzume no tajimaru? 
4) Spiderman? 
5) Veer-Zaara? 
6) DDLJ? 
7) Fanaa? 
8) Peekay? 
9) 3 idiots? 
10) Devdas? 
''')
try:
    filmselection=int(input("Selection: "))
    print("-------------------")
except:
    "Enter valid value"

seans1=Hours("10:00","12:00")
seans2=Hours("12:00","14:00")
seans3=Hours("14:00","16:00")
seans4=Hours("16:00","18:00")
seans5=Hours("18:00","20:00")
seans6=Hours("20:00","22:00")

ghajini=Ghajini("Ghajini","A.R. Murugadoss",2008,"Dram",183,7.3,[seans1,seans2],20)
ayla=Ayla("Ayla","Can Ulkay",2017,"Dram",124,8.3,[seans3,seans6],12)
suzume=Suzume("Ali ve Nino","Asif Kapadia",2016,"Romance",122,7.8,[seans3,seans5],9)
spidarman=Spidarman("Spidar-Man","Sam Raimi",2002,"Aksiyon",121,7.4,[seans1,seans6],30)
veerzaara= VeerZaara("Veer-Zaara","Yash Chopra",2004,"Romantic drama",192,7.8,[seans4,seans5],20)
ddlj=DDLJ("Dilwale Dulhania Le Jayenge","Aditya Chopra",1995,"Romance",189,8,[seans2,seans4],25)
fanaa=Fanaa("Fanaa","Kunak Kohli",2006,"Romance Dram",168,7.1,[seans2,seans3],15)
peekay=Peekay("Peekay","Rajkumar Hirani",2014,"Comedy-dram",153,8.1,[seans3,seans5],21)
threeidiots=Threeidiots("3 Idiots","Rajkumar Hirani",2009,"Comedy-dram",171,8.4,[seans1,seans5],25)
devdas=Devdas("Devdas","Sanjay Leela Bhansali",2002,"Romance-dram",185,7.5,[seans4,seans5],12)
if filmselection==1:
    print("Ghajini Film infomation:")
    print("   ")
    ghajini.duration_info()
    ghajini.year_info()
    ghajini.rating_info()
    print("------------------")
    print(ghajini.show_info())
    print("--------------")
    print("Choices:")
    for i in range(len(ghajini.hours)):
        print(str(i+1) +")" , str(ghajini.hours[i].starttime) + "-"+ str(ghajini.hours[i].endtime))
    seansselection=int(input("Select: "))
    if seansselection==1:
        print(f"{ghajini.name}: {ghajini.hours[i-1].starttime}-{ghajini.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{ghajini.name}: {ghajini.hours[i].starttime}-{ghajini.hours[i].endtime}")
    print("-------------")
    print(f"The price of the ticket:{ghajini.price}")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("--------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(ghajini))

elif filmselection==2:
    print("Ayla Film Infotmation:")
    print(" ")
    ayla.year_info()
    ayla.duration_info()
    ayla.rating_info()
    print("------------------")
    print(ayla.show_info())
    print("------------------")
    print("Choices:")
    for i in range(len(ayla.hours)):
        print(str(i+1) +")" , str(ayla.hours[i].starttime) + "-"+ str(ayla.hours[i].endtime))
    seansselection=int(input("Select: "))
    if seansselection==1:
        print(f"{ayla.name}: {ayla.hours[i-1].starttime}-{ayla.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{ayla.name}: {ayla.hours[i].starttime}-{ayla.hours[i].endtime}")
    print("----------------")
    print(f"The price of the ticket:{ayla.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("---------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(ayla))

elif filmselection==3:
    print("Suzume Film Information:")
    print(" ")
    suzume.year_info()
    suzume.duration_info()
    suzume.rating_info()
    print("------------------")
    print(suzume.show_info())
    print("------------------")
    print("Choices:")
    for i in range(len(suzume.hours)):
        print(str(i+1) +")" , str(suzume.hours[i].starttime) + "-"+ str(suzume.hours[i].endtime))
    seansselection=int(input("Select: "))
    if seansselection==1:
        print(f"{suzume.name}: {suzume.hours[i-1].starttime}-{suzume.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{suzume.name}: {suzume.hours[i].starttime}-{suzume.hours[i].endtime}")
    print("---------------------")
    print(f"The price of the ticket:{suzume.price}")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("---------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(suzume))

elif filmselection==4:
    print("Spidar-Man Film Infomation:")
    print(" ")
    spidarman.year_info()
    spidarman.duration_info()
    spidarman.rating_info()
    print(spidarman.show_info())
    print("--------------")
    print("Choices:")
    for i in range(len(spidarman.hours)):
        print(str(i+1) +")" , str(spidarman.hours[i].starttime) + "-"+ str(spidarman.hours[i].endtime))
    seansselection=int(input("Select: "))
    if seansselection==1:
        print(f"{spidarman.name}: {spidarman.hours[i-1].starttime}-{spidarman.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{spidarman.name}: {spidarman.hours[i].starttime}-{spidarman.hours[i].endtime}")
    print("---------------------")
    print(f"The price of the ticket:{spidarman.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("---------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(spidarman))

elif filmselection==5:
    print("Veer-Zaara Film Informatin:")
    print(" ")
    veerzaara.year_info()
    veerzaara.duration_info()
    veerzaara.rating_info()
    print("------------------")
    print(veerzaara.show_info())
    print("---------------")
    print("Choices:")
    for i in range( len(veerzaara.hours)):
        print(str(i+1) +")" , str(veerzaara.hours[i].starttime) + "-"+ str(veerzaara.hours[i].endtime))
    seansselection=int(input("select: "))
    if seansselection==1:
        print(f"{veerzaara.name}: {veerzaara.hours[i-1].starttime}-{veerzaara.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{veerzaara.name}: {veerzaara.hours[i].starttime}-{veerzaara.hours[i].endtime}")
    print("---------------------")
    print(f"The price of the ticket:{veerzaara.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(veerzaara))

elif filmselection==6:
    print("DDLJ Film Informtaion:")
    print( )
    ddlj.year_info()
    ddlj.duration_info()
    ddlj.rating_info()
    print("------------------")
    print(ddlj.show_info())
    print("------------------")
    print("Choices:")
    for i in range(len(ddlj.hours)):
        print(str(i+1) +")" , str(ddlj.hours[i].starttime) + "-"+ str(ddlj.hours[i].endtime))
    seansselection=int(input("select: " ))
    if seansselection==1:
        print(f"{ddlj.name}: {ddlj.hours[i-1].starttime}-{ddlj.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{ddlj.name}: {ddlj.hours[i].starttime}-{ddlj.hours[i].endtime}")
    print("---------------------")
    print(f"The price of the ticket:{ddlj.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("---------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(ddlj))

elif filmselection==7:
    print("Fanaa Film informtaion:")
    print( )
    fanaa.year_info()
    fanaa.duration_info()
    fanaa.rating_info()
    print("------------------")
    print(fanaa.show_info())
    print("-----------------")
    print("Choices:")
    for i in range(len(fanaa.hours)):
        print(str(i+1) +")" , str(fanaa.hours[i].starttime) + "-"+ str(fanaa.hours[i].endtime))
    seansselection=int(input("select: "))
    if seansselection==1:
        print(f"{fanaa.name}: {fanaa.hours[i-1].starttime}-{fanaa.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{fanaa.name}: {fanaa.hours[i].starttime}-{fanaa.hours[i].endtime}")
    print("------------------")
    print(f"The price of the ticket:{fanaa.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(fanaa))

elif filmselection==8:
    print("Peekay Film Information:")
    peekay.year_info()
    peekay.duration_info()
    peekay.rating_info()
    print("------------------")
    print(peekay.show_info())
    print("------------------")
    print("Choices:")
    for i in range(len(peekay.hours)):
        print(str(i+1) +")" , str(peekay.hours[i].starttime) + "-"+ str(peekay.hours[i].endtime))
    seansselection=int(input("select: "))
    if seansselection==1:
        print(f"{peekay.name}: {peekay.hours[i-1].starttime}-{peekay.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{peekay.name}: {peekay.hours[i].starttime}-{peekay.hours[i].endtime}")
    print("------------------")
    print(f"The price of the ticket:{peekay.price} ")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(peekay))

elif filmselection==9:
    print("Three idiots Film Information:")
    print()
    threeidiots.year_info()
    threeidiots.duration_info()
    threeidiots.rating_info()
    print("------------------")
    print(threeidiots.show_info())
    print("-------------------")
    print("Choices:")
    for i in range(len(threeidiots.hours)):
        print(str(i+1) +")" , str(threeidiots.hours[i].starttime) + "-"+ str(threeidiots.hours[i].endtime))
    seansselection=int(input("select: " ))
    if seansselection==1:
        print(f"{threeidiots.name}: {threeidiots.hours[i-1].starttime}-{threeidiots.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{threeidiots.name}: {threeidiots.hours[i].starttime}-{threeidiots.hours[i].endtime}")
    print("------------------")
    print(f"The price of the ticket:{threeidiots.price}")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(threeidiots))

elif filmselection==10:
    print("Devdas Film Information:")
    print()
    devdas.year_info()
    devdas.duration_info()
    devdas.rating_info()
    print("------------------")
    print(devdas.show_info())
    print("------------------")
    print("Choices:")
    for i in range(len(devdas.hours)):
        print(str(i+1) +")" , str(devdas.hours[i].starttime) + "-"+ str(devdas.hours[i].endtime))
    seansselection=int(input("select: " ))
    if seansselection==1:
        print(f"{devdas.name}: {devdas.hours[i-1].starttime}-{devdas.hours[i-1].endtime}")
    elif seansselection==2:
        print(f"{devdas.name}: {devdas.hours[i].starttime}-{devdas.hours[i].endtime}") 
    print("------------------")   
    print(f"The price of the ticket:{devdas.price}")
    ticket=input("Do you want to buy a ticket?\nYes or No\n")
    if ticket=="Yes":
        print("------------------")
        buyticket=int(input("How much is your money? "))
        print(Money(buyticket).get_money())
        print(Money(buyticket).set_money(devdas))







    










