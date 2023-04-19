#use regex to preprocess Lisp code
import re
import csv

'''
Function converts ATN into csv file. It reads a line by line of the graph defined in lisp.
It deletes comments out of the code
It identifies lines that consist source, edge label, and defines them 
'''
def convert(file, csv_f):
    #open Common Lisp file
    file = open(file, "r")

    for line in file.readlines():
        #delete extra spaces
        line = line.strip()

        #ignore comments and definind of the graph 
        if re.match(";.*", line) or re.match("^\(mapcar.*", line):
            continue

        #delete the comment after the line
        line = re.sub(';.*', '', line).strip()

        #regex for the line with nodes and edges
        pattern = '\([^()]+\)|\S+'
       
        #split this line into the subparts like ['(S', '(FIRS SNT1)', '(INF3 V0)', 'V0)']
        subparts = re.findall(pattern, line)

        #define a source, which is the first node in the line
        source = subparts[0].replace("(", "")

        #for each following node, define its edge label and the destination node
        for i in range(1, len(subparts)):
            #check if it's not empty
            if subparts[i][0] == ")":
                continue
            #check if the destination has an edge name
            edge_label = '' #empty by defaul if there is none for some destinations
            if subparts[i][0]=="(":
                #split this part into edge label and destination
                p = subparts[i].split()
                edge_label = p[0][1::]
                destination = p[1].replace(")", "")

            else:
                destination = subparts[i].replace(")", "")

            #write source, edge_label and destination to csv file
            with open(csv_f, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([source, edge_label, destination])
                csv_file.close()
                    

            print(source, edge_label, destination)

            


print(convert("surf.lisp", "surf.csv"))


