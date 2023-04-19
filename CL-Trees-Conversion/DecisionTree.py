import csv

class DecisionTree:
        #constructor
        def __init__(self, val=0, left=None, right=None) -> None:
                self.val = val
                self.right = right
                self.left= left
                self.index =1
              

        '''
        breadth-first traversal of the tree
        returns an array with the nodes in the breath-first sequence and their position "T" or "F"
        '''
        def BFT(self):
               #queue to keep track of nodes
                q = []
                true_false = []
                q.append(self)

                visited = []

                while q:
                     node = q.pop(0)

                     if node:
                         q.append(node.left)
                         q.append(node.right)  
                                                  

                     visited.append(node)

                return visited
        
        #returns a string representation of a tree in breadth-first traversal
        def __str__(self):
              nodes = self.BFT()
              string = ""
              for i in nodes:
                    if i:
                        string+= str(i.val) + "\n"
                   
              return string
              
        #ADD A LINE
        #writes a tree as a csv file
        def tree_to_csv(self, filename):
              visited = self.BFT()
              with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Index", "Value"])
                for i in visited:
                    if i:
                        writer.writerow([i.index, i.val])
                    
    
