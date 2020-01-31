import os
from PATHs import softPlanRoot,softPlanClasses
from InputCampo import InputCampo
from InputId import InputId
from CriarDiretorios import CriarDiretorios
from CriarArquivos import CriarArquivos

campoASerCriado = InputCampo()
tipoDoId = InputId()

for classe in softPlanClasses:
    CriarDiretorios(classe,campoASerCriado)
    CriarArquivos(classe,campoASerCriado,tipoDoId)

