import os
from Inputs import Inputs
from PATHs import softPlanRoot,softPlanClasses
from InputCampo import InputCampo

def EscreverNoArquivo(classe,campo,tipoDoId):
    try:
        arquivo = open(softPlanRoot + campo + classe + "/" + campo + classe +".cs",'w+')
        arquivo.write("""namespace Softplan.Nugep.Entities."""+ campo + classe + """s
{
    public class """ + campo+classe+""" : SimpleId<""" + tipoDoId + """>
    {
    }
}""")
    except OSError:
        print("Creation of the Class %s failed" %softPlanRoot)
    else:
        print("Successfully created the Class %s " %softPlanRoot)
    finally:
        arquivo.close()