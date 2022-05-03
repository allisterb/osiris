from logging import debug
import pandas as pd

def edges_to_gml_file(df:pd.DataFrame, file_name):
    #Utility functions
    def progress(v):
        debug(v)

    f = open(file_name, "w")
    #helpers
    s = " "
    ss = s+s
    sss = s+s+s
    ssss = s+s+s+s
    nl = "\n"

    #loop helpers
    added = []
    ind = 0

    #Root node
    f.write("graph"+nl)
    f.write("["+nl)

    #Write an edge
    def write_edge(r):
        f.write( ss + "edge" + nl)
        f.write( ss + "[" + nl)
        f.write( ssss + "source" + s + '"' + str(r['src']) + '"' + nl)
        f.write( ssss + "target" + s + '"' + str(r['dst']) + '"' + nl)
        f.write( ssss + "value" + s + str(r['edge_value']) + '"' + nl)
        f.write( ss + "]"+ nl)

    #Write a node
    def write_node(r):
        f.write( ss + "node" + nl)
        f.write( ss + "[" + nl)
        f.write( ssss + "id" + s + '"' + str(r['src']) + '"' + nl)
        f.write( ssss + "label" + s + '"' + str(r['src_label']) + '"' + nl)
        f.write( ss + "]"+ nl)

    #Generate nodes
    for i, r in df.iterrows():
        #increment, as index not reliable
        ind += 1
        #Check for duplicates
        if (r['AUTHOR_ID'] not in added):
            #Add to list
            added.append(r['AUTHOR_ID'])
            write_node(r)
        #print the progress    
        progress(ind)

    debug(nl+"Printing nodes over")

    #flush index
    ind = 0    
    #Generate edges    
    for i, r in df.iterrows():
        #increment, as index not reliable
        ind += 1
        if(r['AUTHOR_ID'] < r['CO-AUTHOR_ID']):
            write_edge(r)
        #print the progress            
        progress(ind)

    debug(nl+"Printing nodes and edges over")

    #closing node
    f.write("]"+nl)
    f.close()
