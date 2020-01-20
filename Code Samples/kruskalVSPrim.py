# Jeff Peterson
# Oct. 11th, 2018
# kruskalVSPrim.py

# This project was a for-fun class project where our task
# was to test and compare any two algorithms, in whatever
# language we liked. This project was not only to satisfy
# a curiosity I posessed, but to also test my Python cap-
# abilities. 

# This project utilizes the networkx library for graph
# implementation, and also houses the kruskal and prim
# algorithms. This programs runs the two side-by-side
# and compares the results in a clean texts document.

import time
import matplotlib.pyplot as plt
import networkx as nx
import math

def main():
    #create results files
    file = open('results.txt', 'w')
    primFile = open('primResults.txt', 'w')
    #default test parameters and varible declarations
    nodeCount = 800
    numberOfGraphs = 100
    densityDivisor = 20
    j = 1
    KruskalGraphArray = [0] * nodeCount
    PrimGraphArray = [0] * nodeCount
    timeComposites = [0] * nodeCount
    stdDevAve = [0] * nodeCount
    total = 0
    devTotal = 0
    # density divisor defines the number of tests, and also the
    # steps between density of the graphs for more precise testing
    while j <= densityDivisor:
        total = 0
        devTotal = 0
        timeComposites.clear()
        stdDevAve.clear()
        KruskalGraphArray.clear()
        PrimGraphArray.clear()
        edgeCount = (j/densityDivisor) * (nodeCount * (nodeCount - 1))
        print("nodeCount: {%i}, edgeCount: {%i}, density: {%.3F}" % (nodeCount, edgeCount, j/densityDivisor))
        #number of graphs to gen
        for i in range(numberOfGraphs):
            G = nx.gnm_random_graph(nodeCount, edgeCount, int(time.time())) #gen random graph
            K = G.copy() # two copies for each graph
            
            KruskalGraphArray.append(G) #store graphs in arrays
            PrimGraphArray.append(K)

        print("%i random graphs generated." % numberOfGraphs)

        #solve every graph in the Kruskal set
        timeComposites.clear()
        for i in range(numberOfGraphs):

            start = time.time()
            H = nx.minimum_spanning_tree(KruskalGraphArray[i], 'weight', 'kruskal')
            end = time.time() - start
            
            timeComposites.append(end)

        # average out how long it took for kruskal to complete
        for k in timeComposites:
            total = total + k

        ave = total / len(timeComposites)
        # calculate standard devation
        for k in timeComposites:
            stdDevAve.append((k + ave) * (k + ave))
        for k in stdDevAve:
            devTotal = devTotal + k

        stdDev = math.sqrt(devTotal)
        
        print("Average time for kruskal set: %.4F" % ave)
        file.write("(%.3F, %.4F) +- (%.6F, %6F)\n" % (j/densityDivisor, ave, stdDev, stdDev))

        #solve every graph in the Prim set
        timeComposites.clear()
        stdDevAve.clear()
        devTotal = 0
        total = 0
        for i in range(numberOfGraphs):
            
            start = time.time()
            H = nx.minimum_spanning_tree(PrimGraphArray[i], 'weight', 'prim')
            end = time.time() - start
            
            timeComposites.append(end)

        # Calculate average time to ocmplete
        for k in timeComposites:
            total = total + k

        ave = total / len(timeComposites)

        # Calculate standard deviation
        for k in timeComposites:
            stdDevAve.append((k + ave) * (k + ave))

        for k in stdDevAve:
            devTotal = devTotal + k

        stdDev = math.sqrt(devTotal)
            
        #total = total / len(timeComposites)
        print("Average time for prim set: %.4F" % ave)
        primFile.write("(%.3F, %.4F) +- (%.6F, %6F)\n" % (j/densityDivisor, ave, stdDev, stdDev))
        j = j + 1
    #close files
    file.close()
    primFile.close()

#defining entry point
if __name__ == '__main__':
    main()
