import os
import json


ALUNOS = ["Adrianeleite", "Amandacruz", "Artumirapriscila", "Brendo", "BrunaEvellyn", \
          "Emilyoliveira", "Giovanamaia", "Henrique", "Joeyramone", "Ligiabarbosa", \
          "Patrick", "Rayssamemoria", "RicardoTorres", "Shalonsouza", "Tallytarebelo", \
          "Caio", "daysonhuende", "emillyfabieli", "francicleysantos", "gabrielarruda", \
          "juliosousa", "kellenmedeiros", "milenalimadeoliveira", "nalyssarodrigues", "thiagosilvaleite", \
          "vitorvasconcelos", "viviantrindade"]

ALUNOS_ID = ["aluno1", "aluno2", "aluno3", "aluno4", "aluno5", \
             "aluno6", "aluno7", "aluno8", "aluno9", "aluno10", \
             "aluno11","aluno12", "aluno13", "aluno14", "aluno15", \
            "aluno16", "aluno17", "aluno18", "aluno19", "aluno20", \
             "aluno21", "aluno22", "aluno23", "aluno24", "aluno25", \
             "aluno26", "aluno27"]

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    LOG_PATH = "/home/anderson/Projetos/exp_SBIE/logs-photos/file_photos"
    OLD_PATH = "experimento_pkg/logs-classification"
    NEW_PATH = "experimento_pkg/logs-MICROSOFT"

    makedirs(NEW_PATH)

    for user_type in os.listdir(OLD_PATH):
        if user_type == "MatheusLima.csv":
            continue

        with open(os.path.join(OLD_PATH, user_type)) as fp:
            user = user_type.split(".")[0]
            print(user)

            for line in fp:
                objs = line.replace("\n", "").split("$")
                obj = json.loads(objs[1])
                # if type(obj) is list and obj != []:
                if type(obj) is list:
                    # print(objs)
                    # print(obj[0]["scores"])
                    # print(max(obj[0]["scores"].items(), key=operator.itemgetter(1))[0])
                    #
                    # print(objs[0].split("-")[1])


                    print(objs[0])
                    l = objs[0].split("-")
                    if l[1] != "aluno112":
                        if l[1] == "aluno5" or l[1] == "aluno8":
                            img = l[0] + "-" + ALUNOS[ALUNOS_ID.index(l[1])] + " -" + l[2] + "-" + l[3] + "-" + l[
                                4] + "-" + l[5]
                        else:
                            img = l[0] + "-" + ALUNOS[ALUNOS_ID.index(l[1])] + "-" + l[2] + "-" + l[3] + "-" + l[4] + "-" + l[5]
                    else:
                        img = l[0] + "-" + "Patrick2" + "-" + l[2] + "-" + l[3] + "-" + l[4] + "-" + \
                              l[5]
                    print(img)

                    if img in open(os.path.join(LOG_PATH, ALUNOS[ALUNOS_ID.index(user)] + ".txt")).read():
                        f = open(os.path.join(NEW_PATH, user + ".csv"), "a+")
                        f.write(img + "$" + objs[1] + "\n")
                        f.close()
                    else:
                        print("NAO")
if __name__ == '__main__':
    main()

