#Common Lisp tree will be represented as that Python Decision Tree
from DecisionTree import DecisionTree

#use regex for sorting common lisp nodes
import re

#returns a line representation of a parantheses tree
#((132)((111)((183)((10)(T GET4 RECEIVE1 NIL)(T GIVE1 GIVE11 16))(T RETURN2 GIVEB 8))((129 131 81)(G . 4)(T KEEP2 4)))(T TAKE1 NIL))
def cl_tree_to_dictionary(file):
      #open Common Lisp file
      file = open(file, "r")
      #initial string that will be returned
      s = ""
      for line in file.readlines():  
         line = line.strip()
         #cut a comment out of a line
         line = re.sub(";.*", "", line).strip()
         #Make this transformation 
         #((T (DRINK2)) 18) --> (T DRINK2 18)
         if re.match("^(\(\([A-Z])", line):
            line= line.replace("(", "").replace(")", "")
            s+= "(" + line + ")" 
         #transform NIL into (NIL) so the code that includes paranthesis would work
         elif line=="NIL":
            line = "(" + line + ")"
            s+=line
         else:
            s += line
      file.close()
      print(s)
      return s

#function to get a word between paranthesis (95)) --> return 98
def get_word(s, start, end):
   #return if the new word is a leaf
   leaf = False

   if s[start-2] != "(":
      leaf = True

   while s[end] !=(")"):
      end+=1
   word = s[start:end].replace("(", "")

   last_child = False

   if s[end+1]==")":
      last_child = True
   #get start that will be the first character of a new word and will be used for the next iteration
   while s[end] ==")" or s[end] =="(":
      end+=1
      #if start went beyond the word limit, break the loop
      if end>=len(s):
         break
   #so the first loop would work
   start = end

   
   return word, start, end, leaf, last_child


"""
creates a python tree from the string representation of the tree
"""
def str_to_tree(s):

   #stack to keep track of the nodes, start from the empty tree that will get its value
   start, end = 2, 0
   # word, start, end, leaf, last_child = get_word(s, start, end)
   stack = [DecisionTree()] 
   stack[0].index = 0.5

   #root that would be returned
   root = None
   ret = False

   #on the second iteration, the root will be the root of the whole tree. It will be popped out of the stack after its right child is appended, so 
   #it's saved in ret variable
   i = 0
   ret = None

   while len(stack)>0: 
      #pop a current node out of stack
      root = stack[-1]

      #mark the iteration when the root of the tree is saved
      if i<2:
         ret = stack[-1]
         i+=1
      else: 
         print("The root that will be returned ", ret)
        

      word, start, end, leaf, last_child = get_word(s, start, end)

      child = DecisionTree(word)


      #IMPLEMENTED IN GET_WORD() FUNCTION
      #(T EAT1 16)) ( - is a leaf
      #if it's a leaf, then it wil not be appended to the stack
      #the solution is integrated into the get_word() function

      #check if a word is a leaf
      print("Word ",word, "Leaf ", leaf)


      #append child
      child = DecisionTree(word)
      if root.left == None:
         root.left = child
         print(child.val, "Added as left child to ", root.val)
         child.index = round(2 * root.index)

         if not leaf:
            print("Appended left child to the stack", child.val)
            stack.append(child)
            

      elif root.right == None:
         print(child.val, "Added as right child to ", root.val)
         root.right = child
         child.index = round(2 * root.index + 1)

         #pop as both right abd left children were atted to the root
         print("The root ", stack[-1].val, " is popped out of the stack. It now has left and right children")
         stack.pop()

         if not leaf:
            print("Appended right child to the stack", child.val)
            stack.append(child)

         
      print("Length of the stack ", len(stack))
      print("Current root ", root)

      # #return root of the tree of all the nodes were popped out
      # if len(stack)==1 or len(stack)==0:
      #    return ret

      #return the root of the tree if the string was fully read
      if len(s)==end:
         return ret


   

  
      
#Discrimination Nets conversion
(str_to_tree(cl_tree_to_dictionary("./Trees/MFEEL.TRE")).tree_to_csv("./CSV/MFEEL.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/INGEST.TRE")).tree_to_csv("./CSV/INGEST.csv")) #successfull
(str_to_tree(cl_tree_to_dictionary("./Trees/AND.TRE")).tree_to_csv("./CSV/AND.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/ATRANS.TRE")).tree_to_csv("./CSV/ATRANS.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/BELIEV.TRE")).tree_to_csv("./CSV/BELIEV.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/SC.TRE")).tree_to_csv("./CSV/SC.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/DK.TRE")).tree_to_csv("./CSV/DK.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/EKC.TRE")).tree_to_csv("./CSV/EKC.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/EKE.TRE")).tree_to_csv("./CSV/EKE.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/EKS.TRE")).tree_to_csv("./CSV/EKS.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/EVT.TRE")).tree_to_csv("./CSV/EVT.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/KAUS.TRE")).tree_to_csv("./CSV/KAUS.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/MTRANS.TRE")).tree_to_csv("./CSV/MTRANS.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/PTRANS.TRE")).tree_to_csv("./CSV/PTRANS.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/STATE.TRE")).tree_to_csv("./CSV/STATE.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/SCALE.TRE")).tree_to_csv("./CSV/SCALE.csv"))  #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/GO.TRE")).tree_to_csv("./CSV/GO.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/PROPEL.TRE")).tree_to_csv("./CSV/PROPEL.csv"))  #successful

#I do not understand how one-line trees look like on the graph, so I did not made their conversion in the code
#If you need this edge case, I can add it after I understand how they work
#(str_to_tree(cl_tree_to_dictionary("./Trees/DO.TRE")).tree_to_csv("./CSV/DO.csv")) #handle one line tree
#(str_to_tree(cl_tree_to_dictionary("./Trees/GRASP.TRE")).tree_to_csv("./CSV/GRASP.csv")) #one line tree














