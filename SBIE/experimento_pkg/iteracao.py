from datetime import datetime
import math

def score (user):
    #/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks
    scoreList = list()
    for i in range(0,40):
        scoreList.append("x")
    #for i in scoreList:
    #   print i
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks/"+user+".csv") as fp:
        for line in fp:
            iteracao = line.replace("\n", "")
            campos = iteracao.split(";")
            #19/6/2017-9:31:21;1;Emilyoliveira;1497879079700;click;questionario.html#;Q:35:H:1-2:E;input;404;696
            print (campos)
            try:
                #if len(campos) > 7 and campos[6].split("A") or campos[6].find("B") or campos[6].find("C") or campos[6].find("D") or campos[6].find("E"):
                if len(campos) > 7 and len(campos[6].split(":")) >= 5:
                    option = campos[6].split(":")
                    print (option[1] + " : " + option[4])
                    index = int(option[1]) - 1
                    scoreList[index] = option[4]
            except:
                print ("CATCH" + str(campos))
        Q = 1
        Gabarito = ["C", "D", "C", "E", "A", "E", "E", "C", "D", "A", "E", "C", "E", "A", "A", "B", "B", "B", "B", "B", "E", "E", "E", "B", "D", "A", "C", "B", "D", "C", "A", "D", "C", "A", "D", "C", "D", "C", "B", "C"]
        contCerta = 0
        contErrado = 0
        contPerdido = 0
        for i in range(0,40):
            if (Gabarito[i] == scoreList[i]):
                contCerta = contCerta + 1
            elif (scoreList[i] == "x"):
                contPerdido = contPerdido + 1
            else:
                contErrado = contErrado + 1
            print (str(Q) + ":" + scoreList[i])
            Q = Q + 1

        print ("ContCerta: " + str(contCerta))
        print ("ContErrado: " + str(contErrado))
        print ("contPerdido: " + str(contPerdido))
        nota = 10*(contCerta/(contCerta+contErrado))
        print ("nota : " + str(nota))


def scoreQuestion ():
    #/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks
    scoreQuestion = list()
    contCertoAluno = list()
    contErradoAluno = list()
    for i in range(0,40):
        scoreQuestion.append(0)
        contCertoAluno.append(0)
        contErradoAluno.append(0)

    for user in range(1,28):
        scoreList = list()
        for i in range(0,40):
            scoreList.append("x")
        #for i in scoreList:
        #   print i
        with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks/aluno"+str(user)+".csv") as fp:
            for line in fp:
                iteracao = line.replace("\n", "")
                campos = iteracao.split(";")
                #19/6/2017-9:31:21;1;Emilyoliveira;1497879079700;click;questionario.html#;Q:35:H:1-2:E;input;404;696
                #print (campos)
                try:
                    #if len(campos) > 7 and campos[6].split("A") or campos[6].find("B") or campos[6].find("C") or campos[6].find("D") or campos[6].find("E"):
                    if len(campos) > 7 and len(campos[6].split(":")) >= 5:
                        option = campos[6].split(":")
                        print (option[1] + " : " + option[4])
                        index = int(option[1]) - 1
                        scoreList[index] = option[4]
                except:
                    print ("CATCH" + str(campos))
            Q = 1
            Gabarito = ["C", "D", "C", "E", "A", "E", "E", "C", "D", "A", "E", "C", "E", "A", "A", "B", "B", "B", "B", "B", "E", "E", "E", "B", "D", "A", "C", "B", "D", "C", "A", "D", "C", "A", "D", "C", "D", "C", "B", "C"]
            #contCerta = 0
            #contErrado = 0
            contPerdido = 0
            for i in range(0,40):
                if (Gabarito[i] == scoreList[i]):
                    contCertoAluno[i] = contCertoAluno[i] + 1
                elif (scoreList[i] == "x"):
                    contPerdido = contPerdido + 1
                else:
                    contErradoAluno[i] = contErradoAluno[i] + 1
                print (str(Q) + ":" + scoreList[i])
                Q = Q + 1
            print ("cont certo aluno")
            print (contCertoAluno)

            print ("cont errado aluno")
            print (contErradoAluno)
            #print ("ContCerta: " + str(contCerta))
            #print ("ContErrado: " + str(contErrado))
            #print ("contPerdido: " + str(contPerdido))
            #nota = 10*(contCerta/(contCerta+contErrado))
            #print ("nota : " + str(nota))

    print ("Teste\n\n")
    print (contCertoAluno)
    print (contErradoAluno)
    for i in range(0,40):
        contCerta = contCertoAluno[i]
        contErrada = contErradoAluno[i]
        media = (contCertoAluno[i]/(contCertoAluno[i]+contErradoAluno[i]))
        nota = 100*(contCerta/(float(contErrada) + float(contCerta)))
        print (contCerta)
        print (contErrada)
        print (nota)
        print ("media Q"+str(i+1) + ": " +str(nota) +"\n")


def desvio (user):
    #/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks
    Gabarito = list()
    #for i in range(0,40):
    Gabarito.append([1,3,5,3,1])
    Gabarito.append([1,2,3,5,3])
    Gabarito.append([3,2,5,1,1])
    Gabarito.append([1,3,1,1,5])
    Gabarito.append([5,1,4,1,1])
    Gabarito.append([2,1,1,1,5])
    Gabarito.append([1,1,1,1,5])
    Gabarito.append([3,1,5,1,1])
    Gabarito.append([1,2,1,5,2])
    Gabarito.append([5,4,1,1,1])
    Gabarito.append([2,2,1,1,5])
    Gabarito.append([4,2,5,1,1])
    Gabarito.append([1,2,2,1,5])
    Gabarito.append([5,1,1,1,1])
    Gabarito.append([5,1,2,1,1])
    Gabarito.append([1,5,1,1,1])
    Gabarito.append([1,5,1,2,1])
    Gabarito.append([1,5,1,1,1])
    Gabarito.append([2,5,2,1,1])
    Gabarito.append([1,5,1,1,1])
    Gabarito.append([1,1,2,3,5])
    Gabarito.append([1,1,2,4,5])
    Gabarito.append([1,2,1,1,5])
    Gabarito.append([1,5,2,1,1])
    Gabarito.append([1,1,4,5,1])
    Gabarito.append([5,1,1,1,1])
    Gabarito.append([1,1,5,3,1])
    Gabarito.append([1,5,1,2,1])
    Gabarito.append([1,1,4,5,1])
    Gabarito.append([1,1,5,1,1])
    Gabarito.append([5,1,1,1,1])
    Gabarito.append([2,1,1,5,1])
    Gabarito.append([1,1,5,1,1])
    Gabarito.append([5,1,1,1,1])
    Gabarito.append([3,1,1,5,1])
    Gabarito.append([1,2,5,1,1])
    Gabarito.append([3,1,1,5,1])
    Gabarito.append([1,1,5,1,1])
    Gabarito.append([1,5,1,1,1])
    Gabarito.append([1,1,5,1,1])
    print("len scorelist: " + str(len(Gabarito)))

    scoreList = list()
    for i in range(0,40):
        scoreList.append("x")

    #for i in scoreList:
    #   print i
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks/"+user+".csv") as fp:
        for line in fp:
            iteracao = line.replace("\n", "")
            campos = iteracao.split(";")
            #19/6/2017-9:31:21;1;Emilyoliveira;1497879079700;click;questionario.html#;Q:35:H:1-2:E;input;404;696
            print (campos)
            try:
                #if len(campos) > 7 and campos[6].split("A") or campos[6].find("B") or campos[6].find("C") or campos[6].find("D") or campos[6].find("E"):
                if len(campos) > 7 and len(campos[6].split(":")) >= 5:
                    option = campos[6].split(":")
                    print (option[1] + " : " + option[4])
                    index = int(option[1]) - 1
                    scoreList[index] = option[4]
            except:
                print ("CATCH" + str(campos))
        Q = 1

        acumDesvio = 0
        #contErrado = 0
        contPerdido = 0
        for i in range(0,40):
            if (scoreList[i] == "A"):
                acumDesvio = acumDesvio + Gabarito[i][0]
            elif (scoreList[i] == "B"):
                acumDesvio = acumDesvio + Gabarito[i][1]
            elif (scoreList[i] == "C"):
                acumDesvio = acumDesvio + Gabarito[i][2]
            elif (scoreList[i] == "D"):
                acumDesvio = acumDesvio + Gabarito[i][3]
            elif (scoreList[i] == "E"):
                acumDesvio = acumDesvio + Gabarito[i][4]
            else:
                contPerdido = contPerdido + 1
            print (str(Q) + ":" + scoreList[i])
            Q = Q + 1

        print ("acumDesvio: " + str(acumDesvio))
        print ("contPerdido: " + str(contPerdido))
        nota = 10*(acumDesvio/((40-contPerdido)*5))
        print ("nota : " + str(nota))

def timeTo(user):
    fp = open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks/"+user+".csv")
    lines = fp.readlines()
    ini = lines[0].split(";")
    fim = lines[-2].split(";")
    timeini = ini[0]
    timefim = fim[0]
    print ("timeini: " + str(timeini))
    print ("timefim: " + str(timefim))
    timestampini = timeini.split("-")
    timestampfim = timefim.split("-")

    dataini = timestampini[0]
    datafim = timestampfim[0]
    print ("dataini: " + str(dataini))
    print ("datafim: " + str(datafim))


    horaini = timestampini[1]
    horafim = timestampfim[1]
    print ("horaini: " + str(horaini))
    print ("horaafim: " + str(horafim))

    splitDataIni = dataini.split("/")
    splitHoraIni = horaini.split(":")
    splitHoraFim = horafim.split(":")

    inicio = datetime(int(splitDataIni[2]), int(splitDataIni[1]), int(splitDataIni[0]), int(splitHoraIni[0]), int(splitHoraIni[1]), int(splitHoraIni[2]))
    fim = datetime(int(splitDataIni[2]), int(splitDataIni[1]), int(splitDataIni[0]), int(splitHoraFim[0]), int(splitHoraFim[1]), int(splitHoraFim[2]))

    diff = fim - inicio
    print ("diff: "+  str(diff))

def timeDiff(ini, fim):
    timeini = "19/6/2017-"+ini
    timefim = "19/6/2017-"+fim
    print ("timeini: " + str(timeini))
    print ("timefim: " + str(timefim))
    timestampini = timeini.split("-")
    timestampfim = timefim.split("-")

    dataini = timestampini[0]
    datafim = timestampfim[0]
    print ("dataini: " + str(dataini))
    print ("datafim: " + str(datafim))


    horaini = timestampini[1]
    horafim = timestampfim[1]
    print ("horaini: " + str(horaini))
    print ("horaafim: " + str(horafim))

    splitDataIni = dataini.split("/")
    splitHoraIni = horaini.split(":")
    splitHoraFim = horafim.split(":")

    inicio = datetime(int(splitDataIni[2]), int(splitDataIni[1]), int(splitDataIni[0]), int(splitHoraIni[0]), int(splitHoraIni[1]), int(splitHoraIni[2]))
    fim = datetime(int(splitDataIni[2]), int(splitDataIni[1]), int(splitDataIni[0]), int(splitHoraFim[0]), int(splitHoraFim[1]), int(splitHoraFim[2]))

    diff = fim - inicio
    print ("diff: "+  str(diff))

def entropy():
    entr = list()
    for question in range (1,41):
        entr.append(entropyByQuestion(question))
    for i in entr:
        print (str(i))

def entropyByQuestion(questao):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/entropy/q"+str(questao)+".csv") as fp:
        contNeutral = 0
        contSadness = 0
        contContempt = 0
        contDisgust = 0
        contAnger = 0
        contSurprise = 0
        contFear = 0
        contHappiness = 0

        for line in fp:
            obj = line.replace("\n", "").split(",")
            if obj[11] == "neutral":
                contNeutral = contNeutral + 1
            elif obj[11] == "sadness":
                contSadness = contSadness + 1
            elif obj[11] == "contempt":
                contContempt = contContempt + 1
            elif obj[11] == "disgust":
                contDisgust = contDisgust + 1
            elif obj[11] == "anger":
                contAnger = contAnger + 1
            elif obj[11] == "surprise":
                contSurprise = contSurprise + 1
            elif obj[11] == "fear":
                contFear = contFear + 1
            elif obj[11] == "happiness":
                contHappiness = contHappiness + 1

        print ("Questao " + str(questao) + " :")
        print ("sadness " + str(contSadness))
        print ("neutral " + str(contNeutral))
        print ("contempt " + str(contContempt))
        print ("disgust " + str(contDisgust))
        print ("anger " + str(contAnger))
        print ("surprise " + str(contSurprise))
        print ("fear " + str(contFear))
        print ("happiness " + str(contHappiness))
        total = contSadness + contNeutral + contContempt + contDisgust + contAnger + contSurprise + contFear + contHappiness
        print ("total " + str(total))
        print ("\n\n")

        entrop = 0.0

        if contSadness > 0:
            entrop = -(contSadness/float(total))*math.log((contSadness/float(total)),2)
        if contNeutral > 0:
            entrop = -(contNeutral/float(total))*math.log((contNeutral/float(total)),2) + entrop
        if contContempt > 0:
            entrop = -(contContempt/float(total))*math.log((contContempt/float(total)),2) + entrop
        if contDisgust > 0:
            entrop = -(contDisgust/float(total))*math.log((contDisgust/float(total)),2) + entrop
        if contAnger > 0:
            entrop = -(contAnger/float(total))*math.log((contAnger/float(total)),2) + entrop
        if contSurprise > 0:
            entrop = -(contSurprise/float(total))*math.log((contSurprise/float(total)),2) + entrop
        if contFear > 0:
            entrop = -(contFear/float(total))*math.log((contFear/float(total)),2) + entrop
        if contHappiness > 0:
            entrop = -(contHappiness/float(total))*math.log((contHappiness/float(total)),2) + entrop

        print ("ENTROPIA " + str(entrop))
        return entrop
