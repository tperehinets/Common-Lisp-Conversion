from DecisionTree import DecisionTree

#use regex for sorting common lisp nodes
import re

#returns a line representation of a parantheses tree
def cl_tree_to_dictionary(file):
      #open Common Lisp file
      file = open(file, "r")
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
         else:
            s += line
      file.close()
      print(s)
      return s


"""
creates a python tree from the string representation of the tree
"""
def str_to_tree(s):
   #function to get a word between paranthesis
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

   
#((98)((105)((89)((66)(T INGEST1 NIL)(T EAT1 16))((11)(T DRINK1 16)(T DRINK2 18)))((50)((74)(T INHALE1 NIL)(T BREATHE1 TAKEBREATH1 20))(T SMOKE1 99 20)))(T TAKE2 2))
#((132)((111)((183)((10)(T GET4 RECEIVE1 NIL)(T GIVE1 GIVE11 16))(T RETURN2 GIVEB 8))((129 131 81)(G . 4)(T KEEP2 4)))(T TAKE1 NIL))

   #stack to keep track of the nodes, start from the empty tree that will get its value
   start, end = 2, 0
   # word, start, end, leaf, last_child = get_word(s, start, end)
   stack = [DecisionTree()] 
   stack[0].index = 0.5

   #root that would be returned
   root = None

   #
   ret = False

   while len(stack)>0: 
      #pop a current node out of stack
      root = stack[-1]

      ret_root = root
      while root.right and root.left:
         ret_root = root
         root = stack.pop()
         print("popped from the loop", root.val)
         ret = True    

      if len(stack)==0 and ret:
         return ret_root
         

      word, start, end, leaf, last_child = get_word(s, start, end)

      child = DecisionTree(word)



      #BOTH ARE IMPLEMENTED IN GET_WORD() FUNCTION
      #(T EAT1 16)) ( - is a leaf, )) - is the last child

      #check if the word is a leaf 
      #if it's a leaf, then it wil not be appended to the stack
      #the solution is integrated into the get_word() function
   

      #check if the word is the last child, meaning that it ends with "))". If it has a sibling, it will end with ")"
      #then, the root node is deleted from the stack

      #check
      print(word, last_child, leaf)

      #append child
      child = DecisionTree(word)
      if root.left == None:
         root.left = child
         child.index = round(2 * root.index)

         if not leaf:
            stack.append(child)
         
         if last_child:
            print("I popped", root.val)
            stack.pop()
            

      elif root.right == None:
         root.right = child
         child.index = round(2 * root.index + 1)

         if not leaf:
            stack.append(child)

         else:
            print("I popped", root.val)
            stack.pop()

      print(len(stack))
      print(root)
      #return root of the tree  
      if len(stack)==1 or len(stack)==0:
         return root

  
      

(str_to_tree(cl_tree_to_dictionary("./Trees/INGEST.TRE")).tree_to_csv("./CSVs/INGEST.csv")) #successfull
(str_to_tree(cl_tree_to_dictionary("./Trees/AND.TRE")).tree_to_csv("./CSVs/AND.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/ATRANS.TRE")).tree_to_csv("./CSVs/ATRANS.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/BELIEV.TRE")).tree_to_csv("./CSVs/BELIEV.csv")) #successful
(str_to_tree(cl_tree_to_dictionary("./Trees/SC.TRE")).tree_to_csv("./CSVs/SC.csv")) #success
#(str_to_tree(cl_tree_to_dictionary("./Trees/DK.TRE")).tree_to_csv("./CSVs/DK.csv")) #ask what NIL represents; handle NIL as a child
#(str_to_tree(cl_tree_to_dictionary("./Trees/DO.TRE")).tree_to_csv("./CSVs/DO.csv")) #handle one line tree
#(str_to_tree(cl_tree_to_dictionary("./Trees/EKC.TRE")).tree_to_csv("./CSVs/EKC.csv")) #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/EKE.TRE")).tree_to_csv("./CSVs/EKE.csv")) #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/BELIEV.TRE")).tree_to_csv("./CSVs/BELIEV.csv")) #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/EKS.TRE")).tree_to_csv("./CSVs/EKS.csv"))  #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/EVT.TRE")).tree_to_csv("./CSVs/EVT.csv"))  #handle NIL as an input
(str_to_tree(cl_tree_to_dictionary("./Trees/GO.TRE")).tree_to_csv("./CSVs/GO.csv")) #not right
#(str_to_tree(cl_tree_to_dictionary("./Trees/GRASP.TRE")).tree_to_csv("./CSVs/GRASP.csv")) #one line tree
(str_to_tree(cl_tree_to_dictionary("./Trees/KAUS.TRE")).tree_to_csv("./CSVs/KAUS.csv")) #ask Alexis about the representation
#(str_to_tree(cl_tree_to_dictionary("./Trees/MFEEL.TRE")).tree_to_csv("./CSVs/MFEEL.csv"))  #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/MTRANS.TRE")).tree_to_csv("./CSVs/MTRANS.csv"))  #handle NIL as an input
#(str_to_tree(cl_tree_to_dictionary("./Trees/PROPEL.TRE")).tree_to_csv("./CSVs/PROPEL.csv"))  #handle NIL as an input 
(str_to_tree(cl_tree_to_dictionary("./Trees/PTRANS.TRE")).tree_to_csv("./CSVs/PTRANS.csv")) #not right
#(str_to_tree(cl_tree_to_dictionary("./Trees/STATE.TRE")).tree_to_csv("./CSVs/STATE.csv"))  #handle NIL as an input 
(str_to_tree(cl_tree_to_dictionary("./Trees/SCALE.TRE")).tree_to_csv("./CSVs/SCALE.csv"))  #handle NIL as an input 











