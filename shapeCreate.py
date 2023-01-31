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

    ### Select topology build
    #buildTopology(len(angPts), heightLayers) #Standard triangle array paneling
    buildTunnelTopology(len(angPts), heightLayers) #Tunnel topology (useful for tubes/tunnels)

        
def tupleToFormatedVertixString(tuple):
    strVar = ""
    for e in tuple:
        strVar += (" " + str(e))
    return "v " + strVar


### Topology Function for Facets (Standard)
def buildTopology(numVerPer, layers):
    file = open('vertexListOutput.txt', 'a')
    totalVers = numVerPer * layers
    vers = list(range(1, totalVers + 1))

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

### Topology Function for Facts (Tunnel)
def buildTunnelTopology(numVerPer, layers):
    file = open('vertexListOutput.txt', 'a')
    totalVers = numVerPer * layers
    vers = list(range(1, totalVers + 1)) #translation index list

    counter = 0
    
    while counter < totalVers:
        
        try:
            if (counter % (2 * numVerPer) == 0):
                currRow = list(range(counter, counter + numVerPer))
                upRow = list(range(counter + numVerPer, counter + (2 * numVerPer)))
                for x in range(len(currRow)):
                    ele1 = vers[currRow[x]]
                    ele2 = vers[upRow[x]]
                    ele3 = vers[upRow[(x + 1) % numVerPer]]
                    ele4 = vers[currRow[(x + 1) % numVerPer]]

                    strVar = "f " + str(ele1) + " " + str(ele2) + " " + str(ele3) + " " + str(ele4) + "\n"
                    #print(strVar)
                    file.write(strVar)

        except IndexError:
            break

        counter += 1



shape("hexagon", 500, 2, 0)