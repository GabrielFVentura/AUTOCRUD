# def CriarDiretorios():
#     try:
#         os.mkdir(path+i)
#     except OSError:
#         print("Creation of the Directory %s failed" % path)
#     else:
#         print("Successfully created the Directory %s " % path)

# def CriarArquivos():
#      try:
#         arquivo = open(path+i+"/"+campoASerCriado+i+".cs", "w+") 
#         EscreverNoArquivo()
#         arquivo.close()
#      except OSError:
#         print("Creation of the File %s failed" % path)
#      else:
#         print("Successfully created the File %s " % path)

# def EscreverNoArquivo():
#     try:
#         arquivo = open(path+i+"/"+campoASerCriado+i+".cs",'w+')
#         arquivo.write("""namespace Softplan.Nugep.Entities."""+ campoASerCriado+i+"""s
# {
#     public class """ + campoASerCriado+i+""" : SimpleId<""" + tipoDoId + """>
#     {
#     }
# }""")
#     except OSError:
#         print("Creation of the Class %s failed" % path)
#     else:
#         print("Successfully created the Class %s " % path)
#     finally:
#         arquivo.close()

