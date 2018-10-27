import os

fileDir = os.path.dirname(os.path.realpath(__file__))
pwd = os.path.join(fileDir, "..", "emotions_database_originals")

def getDivisionDatabasesForExperimental():
    return "training", "testing", "validation"


def getDataAndLabelsPath():
    # CIFE_DATA = os.path.join(pwd, 'CIFE-data-tr-ts.npy')
    # CIFE_LABELS = os.path.join(pwd, 'CIFE-label-tr-ts.npy')
    #
    # CK_DATA = os.path.join(pwd, 'ck+-data.npy')
    # CK_LABELS =  os.path.join(pwd, 'ck+-label.npy')
    #
    # FER_DATA = os.path.join(pwd, 'fer_data.npy')
    # FER_LABELS = os.path.join(pwd, 'fer_labels.npy')
    #
    # JAFFE_DATA = os.path.join(pwd, 'JAFFE-data.npy')
    # JAFFE_LABELS = os.path.join(pwd, 'JAFFE-label.npy')
    #
    # KDEF_DATA = os.path.join(pwd, 'KDEF-data.npy')
    # KDEF_LABELS = os.path.join(pwd, 'KDEF-label.npy')
    #
    # NOVAEMOTIONS_DATA = os.path.join(pwd, 'novaemotions-data.npy')
    # NOVAEMOTIONS_LABELS = os.path.join(pwd, 'novaemotions-label.npy')
    #
    # RAFD_DATA = os.path.join(pwd, 'RafD-data.npy')
    # RAFD_LABELS = os.path.join(pwd, 'RafD-label.npy')
    return getDataPath(), getLabelsPath()

def getDataPath():
    CIFE_TR_DATA = os.path.join(pwd, 'CIFE-data-tr.npy')
    CIFE_TS_DATA = os.path.join(pwd, 'CIFE-data-ts.npy')
    CK_DATA = os.path.join(pwd, 'ck+-data.npy')
    FER_DATA = os.path.join(pwd, 'fer_data.npy')
    JAFFE_DATA = os.path.join(pwd, 'JAFFE-data.npy')
    KDEF_DATA = os.path.join(pwd, 'KDEF-data.npy')
    NOVAEMOTIONS_DATA = os.path.join(pwd, 'novaemotions-data.npy')
    RAFD_DATA = os.path.join(pwd, 'RafD-data.npy')
    return [CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA]
    # return [RAFD_DATA]
def getLabelsPath():
    CIFE_TR_LABELS = os.path.join(pwd, 'CIFE-label-tr.npy')
    CIFE_TS_LABELS = os.path.join(pwd, 'CIFE-label-ts.npy')
    CK_LABELS =  os.path.join(pwd, 'ck+-label.npy')
    FER_LABELS = os.path.join(pwd, 'fer_labels.npy')
    JAFFE_LABELS = os.path.join(pwd, 'JAFFE-label.npy')
    KDEF_LABELS = os.path.join(pwd, 'KDEF-label.npy')
    NOVAEMOTIONS_LABELS = os.path.join(pwd, 'novaemotions-label.npy')
    RAFD_LABELS = os.path.join(pwd, 'RafD-label.npy')
    return [CIFE_TR_LABELS, CIFE_TS_LABELS, CK_LABELS, FER_LABELS, JAFFE_LABELS, KDEF_LABELS, NOVAEMOTIONS_LABELS, RAFD_LABELS]
