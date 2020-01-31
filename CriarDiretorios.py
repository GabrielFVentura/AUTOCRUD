import os
from Inputs import Inputs
from PATHs import softPlanRoot,softPlanClasses
from InputCampo import InputCampo

def CriarDiretorios(classe, campo):
    if (classe != "Entity"):
        try:
            os.mkdir(softPlanRoot+campo+classe)
        except OSError:
            print("Creation of the Directory %s failed" %
                  softPlanRoot+classe)
        else:
            print("Successfully created the Directory %s " %
                  softPlanRoot+classe)
    else:
        os.mkdir(softPlanRoot+campo+"s")


# path = ("C:/SoftplanDirProject/" % campoASerCriado)
