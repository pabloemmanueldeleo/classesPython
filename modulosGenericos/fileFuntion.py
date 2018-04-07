# @Date:   2018-04-07T13:06:02-03:00
# @Last modified time: 2018-04-07T13:06:40-03:00
import json
'''
* DESCRIPCION *
Funciones de JSON para leer, sumar y guardar.

* Example *
dic = ['persp','top','front','side']
saveJSONFile(dic,'F:\Repositores\GitHub\classesPython\modulosGenericos\misCamaras.niko')
for o in loadJSONFile('F:\Repositores\GitHub\classesPython\modulosGenericos\misCamaras.niko'):
    print o
'''

def saveJSONFile(dataBlock, filePath):
    outputFile = open(filePath, 'w')
    JSONData = json.dumps(dataBlock, sort_keys=True, indent=4)
    outputFile.write(JSONData)
    outputFile.close()
    return filePath


def loadJSONFile(filePath):
    inputFile = open(filePath, 'r')
    JSONData = json.load(inputFile)
    inputFile.close()
    return JSONData


def writeJSONFile(dataBlock, filePath):
    f = open(filePath, 'a')
    d = json.dumps(dataBlock, sort_keys=True, indent=4)
    f.write(d)
    f.close()
