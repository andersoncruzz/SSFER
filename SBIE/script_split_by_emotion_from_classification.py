# -*- coding: utf-8 -*-

import os
import json
import shutil
import operator
import cv2

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

def copy (path_input, path_output):
    img = cv2.imread(path_input)
    img = cv2.resize(img, (213, 160))
    cv2.imwrite(path_output, img)

def main():

    microsoft = False

    if microsoft:
        PATH = "experimento_pkg/logs-MICROSOFT"
    else:
        PATH = "experimento_pkg/logs_SSFER_2"

    users = os.listdir(PATH)
    for user_type in users:
        if user_type == "MatheusLima.csv":
            continue

        with open(os.path.join(PATH, user_type)) as fp:
            user = user_type.split(".")[0]
            print(user)
            if microsoft:
                user_path = "/home/anderson/Projetos/SBIE-logs-photos-split/microsoft/" + user
            else:
                user_path = "/home/anderson/Projetos/SBIE-logs-photos-split/SSFER_65/" + user

            makedirs(user_path)

            user_path_original = "/home/anderson/Projetos/exp_SBIE/logs-photos/" + ALUNOS[ALUNOS_ID.index(user)]

            for line in fp:
                objs = line.replace("\n", "").split("$")
                obj = json.loads(objs[1])
                if type(obj) is list and obj != []:

                    # print(objs)
                    # print(obj[0]["scores"])
                    # print(max(obj[0]["scores"].items(), key=operator.itemgetter(1))[0])
                    #
                    # print(objs[0].split("-")[1])

                    emotion = max(obj[0]["scores"].items(), key=operator.itemgetter(1))[0]
                    if obj[0]["scores"][emotion] > 0.65:
                        makedirs(os.path.join(user_path, emotion))
                        # shutil.copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, emotion, objs[0]))
                        copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, emotion, objs[0]))
                        print(objs[0])
                    else:
                        #FOTOS SEM CLASSIFICACAO
                        makedirs(os.path.join(user_path, "no_classification"))
                        # shutil.copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, "no_classification", objs[0]))
                        copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, "no_classification", objs[0]))
                else:
                    #FOTOS SEM CLASSIFICACAO
                    makedirs(os.path.join(user_path, "no_classification"))
                    # shutil.copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, "no_classification", objs[0]))
                    copy(os.path.join(user_path_original, objs[0]), os.path.join(user_path, "no_classification", objs[0]))

                    # shutil.copy(, user_path)


if __name__ == '__main__':
    main()
