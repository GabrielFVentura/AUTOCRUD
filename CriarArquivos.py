import os
from Inputs import Inputs
from PATHs import softPlanRoot,softPlanClasses
from InputCampo import InputCampo
from EscreverNoArquivo import EscreverNoArquivo

def CriarArquivos(classe,campo,tipoDoId):
    if (classe != "Entity"):
            try:
                arquivo = open(softPlanRoot + campo + classe + "/" + campo + classe + ".cs", "w+")
                EscreverNoArquivo(classe, campo, tipoDoId)
                arquivo.close()
            except OSError:
                print("Creation of the File %s failed" %
                      softPlanRoot + classe)
            else:
                print("Successfully created the File %s " %
                      softPlanRoot + classe)
    else:
            try:
                arquivo = open(softPlanRoot + campo + classe + "/" + campo + ".cs", "w+")
                EscreverNoArquivo(classe, campo, tipoDoId)
                arquivo.close()
            except OSError:
                print("Creation of Entity File %s Failed")
            else:
                print("Create of Entity File Succesful")

#"C:/SoftplanDirProject/ + "Type" + "/" + "TipoEvento" + Type"
# path+i+"/"+campoASerCriado+i+".cs"
# path = ("C:/SoftplanDirProject/" % campoASerCriado)
