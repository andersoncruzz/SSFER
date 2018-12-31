import os, sys

def erase(user):
    #2756
    path = "/home/acruz/Documents/EXPERIMENTO-SBIE/logs-photos/BKP-FOTOS/" + user
    dirs = os.listdir(path)

    flag = False
    for file in dirs:
        if flag == True:
            os.remove(path + "/"+ file)
            flag = False
        else:
            flag = True
    # removing
    #os.remove("aa.txt")

def rename(user):
    #2756
    path = "/home/acruz/Documents/EXPERIMENTO-SBIE/logs-photos/BKP-FOTOS/" + user
    dirs = os.listdir(path)

    flag = False
    cont = 0
    for file in dirs:
        cont = cont+1
        auxname = file.split("-")
        print (cont)
        print (file)
        newname = auxname[0]+"-"+user+"-"+auxname[2]+"-"+auxname[3]+"-"+auxname[4]+"-"+auxname[5]
        print (newname)
        os.rename(path+"/"+file, path +"/"+newname)
   
