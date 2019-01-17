import time
from datetime import datetime

def window (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-clicks/aluno"+str(user)+".csv") as fp:
        questionIni = list()
        questionFim = list()
        #questionIni.append(1)
        for line in fp:
            obj = line.replace("\n", "").split(";")
            print (obj)
            if questionIni == []:
                if len(obj) > 7:
                    question = obj[6]
                    question = question.split(":")
                    if len(question) > 2:
                        idQuestion = question[1]
                        print (idQuestion)
                        questionIni.append(idQuestion)
                        questionIni.append(obj[3])
            elif len(obj) > 7:
                question = obj[6]
                question = question.split(":")
                if len(question) > 2:
                    if questionIni[0] != question[1]:
                        print (question[1] + " Aqui")
                        createClassificationByQuestion(user,questionIni[0],questionIni[1], obj[3])
                        questionIni = []
                        questionIni.append(question[1])
                        questionIni.append(obj[3])
            else:
                print (False)
        print (questionIni)

def createClassificationByQuestion(user, q, ini, fim):
    auxini = int(ini[0:10])
    auxfim = int(fim[0:10]) - 1
    timeini = time.strftime("%H:%M:%S", time.localtime(auxini))
    timefim = time.strftime("%H:%M:%S", time.localtime(auxfim))

    if time.localtime(auxini) > time.localtime(auxfim):
        timefim = time.strftime("%H:%M:%S", time.localtime(auxfim+1))
        auxfim = int(fim[0:10])
    print (timeini)
    print (timefim)
    print ("questao " + q)
    print ("questao comecou " + str(timeini))
    print ("questao terminou " + str(timefim))
    dt_ini = datetime.strptime(timeini, '%H:%M:%S')
    dt_fim = datetime.strptime(timefim, '%H:%M:%S')
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/logs/aluno"+str(user)+".csv") as fp:
        #log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/user-questao/aluno"+str(user)+".csv", "a+")
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/questao-user/q"+str(q)+".csv", "a+")
        for line in fp:
            obj = line.replace("\n", "").split(",")
            #print obj
            dt_atual = datetime.strptime(obj[0], '%H:%M:%S')
            #timeQ = int(obj[0])
            if dt_ini == dt_atual or dt_fim == dt_atual or (dt_atual > dt_ini and dt_atual < dt_fim):
                print("Ini")
                print (dt_ini)
                print (dt_fim)
                print (dt_atual)
                print ("Fim")
                question = "Q"+str(q)
                log.write(str(user)+","+ question+","+line)
        log.close()


#>>> import time
#>>> time.ctime(1497874188)
#'Mon Jun 19 08:09:48 2017'
#>>> time.strftime("%D %H:%M:%S", time.localtime(1497874188))
#'06/19/17 08:09:48'
#>>> time.strftime("%H:%M:%S", time.localtime(1497874188))
#'08:09:48'
#>>> time.strftime("%H:%M:%S", time.localtime(1497874208))
#'08:10:08'
#>>> 
