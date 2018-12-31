import json

def exportEmotionsCSV():
    #exportToFileEmotionsCSV ("aluno1")
    #users = plus()
    for i in range(1,28):
        exportToFileEmotionsCSV ("aluno"+str(i))

def exportToFileEmotionsCSV (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/MATLAB/"+user+".csv", "a+")
        colun = "timestamp,sadness,neutral,contempt,disgust,anger,surprise,fear,happiness,emotion"
        log.write(colun+"\n")

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
                timestamp = photo.split("-")
                instance = timestamp[0] + "," + str(objson[0]["scores"]["sadness"]) + "," + str(objson[0]["scores"]["neutral"]) + "," + str(objson[0]["scores"]["contempt"]) + "," + str(objson[0]["scores"]["disgust"]) + "," + str(objson[0]["scores"]["anger"]) + "," + str(objson[0]["scores"]["surprise"]) + "," + str(objson[0]["scores"]["fear"]) + "," + str(objson[0]["scores"]["happiness"]) + ","  + classification
                log.write(instance + "\n")
        log.close()

def calcula():
    #exportToFileEmotionsCSV ("aluno1")
    #users = plus()
    for i in range(1,28):
        media ("aluno"+str(i))

def media (user):
    with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv") as fp:
        #log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-PreProcessedClassification/MATLAB/"+user+".csv", "a+")
        #colun = "timestamp,sadness,neutral,contempt,disgust,anger,surprise,fear,happiness,emotion"
        #log.write(colun+"\n")
        acum = [0,0,0,0,0,0,0,0]
        cont = 0
        for line in fp:
            obj = line.replace("\n", "")
            objV = obj.split("$")
            #print obj
            if objV[1].find("scores") != -1:
                photo = objV[0]
                objson = json.loads(str(objV[1]))
                acum[0] = acum[0] + objson[0]["scores"]["sadness"]
                acum[1] = acum[1] + objson[0]["scores"]["neutral"]
                acum[2] = acum[2] + objson[0]["scores"]["contempt"]
                acum[3] = acum[3] + objson[0]["scores"]["disgust"]
                acum[4] = acum[4] + objson[0]["scores"]["anger"]
                acum[5] = acum[5] + objson[0]["scores"]["surprise"]
                acum[6] = acum[6] + objson[0]["scores"]["fear"]
                acum[7] = acum[7] + objson[0]["scores"]["happiness"]
                cont = cont + 1
        print (user)
        print (str(acum[0]/cont)[0:6] + "\t" + str(acum[1]/cont)[0:6] + "\t" + str(acum[2]/cont)[0:6] + "\t" + str(acum[3]/cont)[0:6] + "\t" + str(acum[4]/cont)[0:6] + "\t" + str(acum[5]/cont)[0:6] + "\t" + str(acum[6]/cont)[0:6] + "\t"  + str(acum[7]/cont)[0:6])
        print ("cont : " + str(cont))
        print ("media sadness: " + str(acum[0]/cont))
        print ("media neutral: " + str(acum[1]/cont))
        print ("media contempt: " + str(acum[2]/cont))
        print ("media disgust: " + str(acum[3]/cont))
        print ("media anger: " + str(acum[4]/cont))
        print ("media surprise: " + str(acum[5]/cont))
        print ("media fear: " + str(acum[6]/cont))
        print ("media happiness: " + str(acum[7]/cont))
        total = (acum[0]/cont) + (acum[1]/cont) + (acum[2]/cont) + (acum[3]/cont) + (acum[4]/cont) + (acum[5]/cont) + (acum[6]/cont) + (acum[7]/cont)
        print ("total: " + str(total))
        print ("\n\n\n")
