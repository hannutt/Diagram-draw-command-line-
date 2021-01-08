import matplotlib.pyplot as plt

#luodaan funktio, jolla toteutetaan piirakkakaavion piirtäminen.
#values taulukkoon tallennetaan käyttäjän syöttämät lukuarvot
#valuelabels taulukkoon lukuarvojen teksti/otsikko ja colors
#taulukkoon käyttäjän syöttämät piirakkasektoreiden värit.
#while truella luodaan toistosilmukka, joka kysyy käyttäjältä
#arvoja, kun halutut arvot on syötetty, toisto keskeytetään
#antamalla myvalue muuttujalle arvoksi 00 ja kahdelle muulle muuttujalle
#tyhjä merkkijono. matplotlib kirjasto saa syötetyt arvot parametreina
#ja piirtää niiden pohjalta diagrammin.
def pieChart():
    
    values = []
    valuelabels = []
    Colors = []
    while True:
        
        myvalue = int(input('Enter a value: '))
        values.append(myvalue)
        mylabel = input('Enter a value title: ')
        valuelabels.append(mylabel)
        mycolor = input('Enter value color: ')
        Colors.append(mycolor)
        if myvalue == 00 and mylabel == '' and mycolor == '':
            Colors.pop()
            break

    plt.pie(values,labels=valuelabels,colors=Colors)
    plt.show()

#luodaan funktio viivakaavion piirtämiseen. funktio kysyy viivan värin,
#y ja x-akseleiden tekstit sekä y ja x-akseleiden alku ja loppupisteet.
def lineDraw():

    xpoint = []
    ypoint = []
    Color = input('Enter linecolor: ')
    ytitle = input('Enter y-axis title: ')
    xtitle = input('Enter x-axis title: ')
    Color = Color.lower()
    xvalue = int(input('Enter x-axis starting point: '))
    xpoint.append(xvalue)
    xvalue = int(input('Enter x-axis ending point: '))
    xpoint.append(xvalue)
    yvalue = int(input('Enter y-axis starting point: '))
    ypoint.append(yvalue)
    yvalue = int(input('Enter y-axis ending point: '))
    ypoint.append(yvalue)

    plt.plot(xpoint,ypoint,color=Color)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.show()    

#luodaan funktio, jolla toteutetaan pylväskaavion piirtäminen.
def bars():
    barName = []
    barValue = []

    while True:
        bartitle = input('Enter bar title: ')
        barName.append(bartitle)
        barval = int(input('Enter bar value: '))
        barValue.append(barval)
        if bartitle == '' and barval == 00:
            break
    plt.bar(barName,barValue)
    plt.show()

#tulostetaan ohjeteksti ohjelman käyttäjälle. select muuttujaan tallennetaan
#käyttäjän syöttämä komento ja ehtolauseiden avulla kutsutaan oikeaa funktiota.
#lower metodi muuttaa käyttäjän syöttämät kirjaimet pieniksi kirjaimiksi, jolloin
#syötetyn komennon kirjainkoolla ei ole merkitystä.

print('Enter pie to draw piechart, line to draw line diagram or bar to draw Bar chart')
select = input('Select function: ')
select = select.lower()
if select == 'pie':
    pieChart()
    
elif select == 'line':
    lineDraw()

elif select == 'bar':
    bars()



                 
 
