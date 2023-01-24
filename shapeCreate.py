import math

shapeAngles = {
    "triangle" : (0, 120, 240),
    "square" : (0, 90, 180, 270),
    "pentagon" : (0, 72, 144, 216, 288),
    "hexagon" : (0, 60, 120, 180, 240, 300),
    "octagon" : (0, 45, 90, 135, 180, 225, 270, 315)
}

##
# shapeStr - Enter a string from above shapes
# height - Number of layers for structure
# width - Width of the structure
# angOffset - Angle offset between layers
#
# #
def shape(shapeStr, heightLayers, width, angOffset):

    try:
        angPts = shapeAngles[shapeStr]
    except KeyError:
        print("Shape not supported.")
        exit()
    
    ptsList = []
    
    count = 0
    for h in range(heightLayers):
        for t in angPts:
            t += (count * angOffset)
            x = width * math.cos((t * math.pi) / 180)
            y = width * math.sin((t * math.pi) / 180)
            ptsList.append((x, y, h))
        count += 1

    file = open('vertexListOutput.txt', 'w') #wipe file
    file = open('vertexListOutput.txt', 'a')

    for p in ptsList:
        ptsStr = tupleToFormatedVertixString(p)
        file.write(ptsStr + "\n")
    file.close()

    buildTopology(len(angPts), heightLayers)

        
def tupleToFormatedVertixString(tuple):
    strVar = ""
    for e in tuple:
        strVar += (" " + str(e))
    return "v " + strVar

def buildTopology(numVerPer, layers):
    file = open('vertexListOutput.txt', 'a')
    totalVers = numVerPer * layers
    vers = list(range(1, totalVers + 1))

    facetLst = []
    strVar = ""
    counter = 0

    while counter < len(vers):
        try:
            curr = vers[counter]
            ngh = vers[counter + 1]
            nghAb = vers[counter + numVerPer]
            file.write("f " + str(curr) + " " + str(ngh) + " " + str(nghAb) + "\n")
        except IndexError:
            break

        counter += 1


shape("hexagon", 40, 1, 10)