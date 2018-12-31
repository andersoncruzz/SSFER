import json

def exportToAllEmotionsProbabilitiesCSV():
    for i in range(1,28):
        exportToEmotionsProbabilitiesCSV ("aluno"+str(i))

def exportToAloneFileEmotionsProbabilitiesCSV():

    log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/CSV-emotionsProbabilities/merge-emotionsProbabilities.csv", "a+")
    colun = "photo,sadness,neutral,contempt,disgust,anger,surprise,fear,happiness,student"
    log.write(colun+"\n")
    log.close()
    for i in range(1,28):
        exportToFileEmotionsProbabilitiesCSV ("aluno"+str(i))

def exportToAloneFileEmotionsCSV():

    log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/CSV-emotionsProbabilities/merge-emotions.csv", "a+")
    colun = "photo,sadness,neutral,contempt,disgust,anger,surprise,fear,happiness,student,emotion"
    log.write(colun+"\n")
    log.close()
    #users = plus()
    for i in range(1,28):
        exportToFileEmotionsCSV ("aluno"+str(i))

def exportToFileEmotionsCSV (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/CSV-emotionsProbabilities/merge-emotions.csv", "a+")
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            #print obj
            if objV[1].find("scores") != -1:
                photo = objV[0]
                objson = json.loads(str(objV[1]))
                #t = objson[0]["scores"]["sadness"]
                #print (t)
                sadness = objson[0]["scores"]["sadness"]
                neutral = objson[0]["scores"]["neutral"]
                contempt = objson[0]["scores"]["contempt"]
                disgust = objson[0]["scores"]["disgust"]
                anger = objson[0]["scores"]["anger"]
                surprise = objson[0]["scores"]["surprise"]
                fear = objson[0]["scores"]["fear"]
                happiness = objson[0]["scores"]["happiness"]
                emotions = [sadness, neutral, contempt, disgust, anger, surprise, fear, happiness]
                classification = ""
                if max(emotions) == sadness:
                    classification = "sadness"
                elif max(emotions) == neutral:
                    classification = "neutral"
                elif max(emotions) == contempt:
                    classification = "contempt"
                elif max(emotions) == disgust:
                    classification = "disgust"
                elif max(emotions) == anger:
                    classification = "anger"
                elif max(emotions) == surprise:
                    classification = "surprise"
                elif max(emotions) == fear:
                    classification = "fear"
                elif max(emotions) == happiness:
                    classification = "happiness"

                instance = photo + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"]) + "," + user + "," + classification
                log.write(instance + "\n")
        log.close()



def exportToFileEmotionsProbabilitiesCSV (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/CSV-emotionsProbabilities/merge-emotionsProbabilities.csv", "a+")
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            #print obj
            if objV[1].find("scores") != -1:
                photo = objV[0]
                objson = json.loads(str(objV[1]))
                #t = objson[0]["scores"]["sadness"]
                #print (t)
                instance = photo + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"]) + "," + user
                log.write(instance + "\n")
        log.close()



def exportToEmotionsProbabilitiesCSV (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/CSV-emotionsProbabilities/"+user+"-emotionsProbabilities.csv", "a+")
        colun = "photo,sadness,neutral,contempt,disgust,anger,surprise,fear,happiness,aluno"
        log.write(colun+"\n")
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            print (obj)
            if objV[1].find("scores") != -1:
                photo = objV[0]
                objson = json.loads(str(objV[1]))
                #t = objson[0]["scores"]["sadness"]
                #print (t)
                instance = photo + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"]) + "," + user
                log.write(instance + "\n")
        log.close()

def exportToArff (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/ARFF/"+user+".arff", "a+")
        header = """% 1. Title: Emotion Recognition EETI
% 
% 2. Sources:
%      (a) Creator: Anderson Araujo da Cruz 
%      (b) Date: June, 2017
% 
@RELATION emotionRecognition

@ATTRIBUTE photo  STRING
@ATTRIBUTE sadness  NUMERIC
@ATTRIBUTE neutral   NUMERIC
@ATTRIBUTE contempt  NUMERIC
@ATTRIBUTE disgust   NUMERIC
@ATTRIBUTE anger   NUMERIC
@ATTRIBUTE surprise   NUMERIC
@ATTRIBUTE fear   NUMERIC
@ATTRIBUTE happiness   NUMERIC

@DATA   
"""
        log.write(header)
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            if objV[1].find("scores") != -1:
                name = objV[0]
                objson = json.loads(str(objV[1]))
                #t = objson[0]["scores"]["sadness"]
                #print (t)
                instance = name + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"])
                log.write(instance + "\n")
        log.close()

def exportAllToArff():
    log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/ARFF/merge-data.arff", "a+")
    header = """% 1. Title: Emotion Recognition EETI
% 
% 2. Sources:
%      (a) Creator: Anderson Araujo da Cruz 
%      (b) Date: June, 2017
% 
@RELATION emotionRecognition

@ATTRIBUTE photo  STRING
@ATTRIBUTE sadness  NUMERIC
@ATTRIBUTE neutral   NUMERIC
@ATTRIBUTE contempt  NUMERIC
@ATTRIBUTE disgust   NUMERIC
@ATTRIBUTE anger   NUMERIC
@ATTRIBUTE surprise   NUMERIC
@ATTRIBUTE fear   NUMERIC
@ATTRIBUTE happiness   NUMERIC
@ATTRIBUTE qtdRespostasCertas NUMERIC 
@ATTRIBUTE qtdRespostasErradas NUMERIC 
@ATTRIBUTE qtdRespostasPerdidas NUMERIC 
@ATTRIBUTE notaScore NUMERIC 
@ATTRIBUTE desvio NUMERIC
@ATTRIBUTE desvioNormalizado NUMERIC
@ATTRIBUTE tempoGasto NUMERIC
@ATTRIBUTE diaNoMomento {Pessimo,Ruim,Regular,Bom,Otimo}
@ATTRIBUTE sentimentoNoMomento {indisposto,Normal,disposto}
@ATTRIBUTE horaSonoUltNoite NUMERIC
@ATTRIBUTE expectativaVestibular {Pessima,Ruim,Regular,Boa,Otima}
@ATTRIBUTE desempenhoEscola {Pessimo,Ruim,Regular,Bom,Otimo}
@ATTRIBUTE preparacaoVestibular {Pessima,Ruim,Regular,Boa,Otima}
@ATTRIBUTE cursinho {yes,no}
@ATTRIBUTE maisAfinidadeArea {Exatas,Naturezas,Humanas,Linguagens}
@ATTRIBUTE menosAfinidadeArea {Exatas,Naturezas,Humanas,Linguagens}
@ATTRIBUTE sexo {M,F}
@ATTRIBUTE aprovado {yes,no}
@ATTRIBUTE student {aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10,aluno11,aluno12,aluno13,aluno14,aluno15,aluno16,aluno17,aluno18,aluno19,aluno20,aluno21,aluno22,aluno23,aluno24,aluno25,aluno26,aluno27}
@ATTRIBUTE emotion {sadness,neutral,contempt,disgust,anger,surprise,fear,happiness}

@DATA   
"""
    #17,12,11,5.86,102,7.03,104,Regular,indisposto,6,Boa,Regular,Boa,no,Humanas,Naturezas,F

    log.write(header)
    log.close()
    listOfuser = plus()
    for i in range(1,28):
        exportToAloneArff ("aluno"+str(i), listOfuser[i-1])


def exportToAloneArff (user, attributes):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/ARFF/merge-data.arff", "a+")
        #listOfuser = plus()
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            if objV[1].find("scores") != -1:
                name = objV[0]
                objson = json.loads(str(objV[1]))
                #t = objson[0]["scores"]["sadness"]
                #print (t)
                sadness = objson[0]["scores"]["sadness"]
                neutral = objson[0]["scores"]["neutral"]
                contempt = objson[0]["scores"]["contempt"]
                disgust = objson[0]["scores"]["disgust"]
                anger = objson[0]["scores"]["anger"]
                surprise = objson[0]["scores"]["surprise"]
                fear = objson[0]["scores"]["fear"]
                happiness = objson[0]["scores"]["happiness"]
                emotions = [sadness, neutral, contempt, disgust, anger, surprise, fear, happiness]
                classification = ""
                if max(emotions) == sadness:
                    classification = "sadness"
                elif max(emotions) == neutral:
                    classification = "neutral"
                elif max(emotions) == contempt:
                    classification = "contempt"
                elif max(emotions) == disgust:
                    classification = "disgust"
                elif max(emotions) == anger:
                    classification = "anger"
                elif max(emotions) == surprise:
                    classification = "surprise"
                elif max(emotions) == fear:
                    classification = "fear"
                elif max(emotions) == happiness:
                    classification = "happiness"


                instance = name + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"]) + "," + attributes + "," +  user + "," +classification
                #log.write(instance + "," + attributes + "\n")
                log.write(instance + "\n")
        log.close()

def plus():
    aluno1 ="17,12,11,5.86,102,7.03,104,Regular,indisposto,6,Boa,Regular,Boa,no,Humanas,Naturezas,F,yes"
    aluno2="8,15,17,3.47,59,5.13,81,Regular,Normal,6,Regular,Regular,Regular,no,Exatas,Linguagens,F,no"
    aluno3 ="8,20,12,2.85,69,4.92,76,Regular,Normal,8,Boa,Bom,Regular,no,Linguagens,Exatas,F,no"
    aluno4 = "20,20,0,5.0,130,6.5,92,Bom,disposto,5,Boa,Bom,Boa,yes,Exatas,Linguagens,M,yes"
    aluno5 = "18,21,1,4.61,118,6.05,76,Bom,disposto,6,Boa,Bom,Boa,no,Naturezas,Humanas,F,no"
    aluno6 = "24,10,6,7.05,136,8,90,Regular,Normal,3,Boa,Otimo,Regular,no,Humanas,Naturezas,F,yes"
    aluno7 = "11,27,2,2.89,92,4.84,88,Bom,Normal,6,Regular,Bom,Regular,yes,Humanas,Exatas,F,no"
    aluno8 = "16,24,0,4.0,117,5.85,90,Bom,Normal,6,Ruim,Regular,Regular,yes,Exatas,Naturezas,M,no"
    aluno9 = "14,10,16,5.83,87,7.25,94,Regular,Normal,5,Boa,Regular,Regular,no,Humanas,Exatas,M,yes"
    aluno10 = "22,17,1,5.64,143,7.33,95,Bom,indisposto,7,Boa,Regular,Ruim,no,Exatas,Humanas,F,yes"
    aluno11 = "20,20,0,5.0,132,6.6,115,Bom,Normal,7,Regular,Bom,Regular,yes,Exatas,Linguagens,M,yes"
    aluno12 = "15,3,22,8.33,79,8.77,92,Regular,Normal,4,Regular,Bom,Boa,yes,Naturezas,Exatas,F,yes"
    aluno13 = "10,25,5,2.85,88,5.02,92,Regular,Normal,5,Boa,Regular,Regular,no,Naturezas,Linguagens,M,no"
    aluno14 = "12,7,21,6.31,70,7.36,76,Bom,disposto,5,Boa,Regular,Otima,no,Exatas,Linguagens,M,yes"
    aluno15 = "19,14,7,5.75,114,6.9,99,Otimo,Normal,7,Ruim,Regular,Pessima,no,Humanas,Exatas,F,yes"
    aluno16 = "23,17,0,5.75,145,7.25,91,Bom,Normal,8,Boa,Regular,Regular,no,Exatas,Linguagens,M,yes"
    aluno17 = "9,16,15,3.59,64,5.12,110,Bom,disposto,6,Otima,Bom,Boa,yes,Exatas,Linguagens,M,no"
    aluno18 = "11,21,8,3.43,90,5.62,94,Bom,Normal,5,Boa,Bom,Regular,no,Naturezas,Linguagens,F,no"
    aluno19 = "13,19,8,4.06,88,5.5,94,Bom,Normal,5,Boa,Regular,Regular,no,Naturezas,Exatas,M,no"
    aluno20 = "21,11,8,6.56,129,8,99,Regular,Normal,2,Boa,Bom,Boa,yes,Exatas,Linguagens,M,yes"
    aluno21 = "14,11,15,5.60,88,7.03,90,Regular,Normal,2,Boa,Bom,Boa,no,Exatas,Naturezas,M,yes"
    aluno22 = "1,2,37,3.33,7,4.66,90,Regular,Normal,7,Boa,Bom,Boa,no,Linguagens,Exatas,F,no"
    aluno23 = "9,15,16,3.75,61,5.08,101,Regular,indisposto,7,Regular,Bom,Regular,no,Naturezas,Humanas,F,no"
    aluno24 = "12,17,11,4.13,82,5.65,105,Pessimo,indisposto,5,Regular,Bom,Regular,yes,Humanas,Exatas,F,no"
    aluno25 = "16,8,16,6.66,92,7.66,91,Regular,Normal,6,Regular,Regular,Ruim,no,Exatas,Naturezas,M,yes"
    aluno26 = "13,12,15,5.2,85,6.8,93,Ruim,Normal,5,Regular,Regular,Regular,yes,Humanas,Naturezas,M,yes"
    aluno27 = "15,25,0,3.75,112,5.6,80,Regular,Normal,5,Regular,Regular,Regular,no,Humanas,Exatas,F,no"

    lis = list()
    lis.append(aluno1)
    lis.append(aluno2)
    lis.append(aluno3)
    lis.append(aluno4)
    lis.append(aluno5)
    lis.append(aluno6)
    lis.append(aluno7)
    lis.append(aluno8)
    lis.append(aluno9)
    lis.append(aluno10)
    lis.append(aluno11)
    lis.append(aluno12)
    lis.append(aluno13)
    lis.append(aluno14)
    lis.append(aluno15)
    lis.append(aluno16)
    lis.append(aluno17)
    lis.append(aluno18)
    lis.append(aluno19)
    lis.append(aluno20)
    lis.append(aluno21)
    lis.append(aluno22)
    lis.append(aluno23)
    lis.append(aluno24)
    lis.append(aluno25)
    lis.append(aluno26)
    lis.append(aluno27)

    return lis
