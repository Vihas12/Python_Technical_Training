
"""     Data Structure are different ways of organizing data on your computer that can be used effectively

        ALGORITHM: These are the steps by step process to solve the problem                                     
        
        
                                            DATA STRUCTURE
                                                  |
                    ------------------------------------------------------------------
                    |                                                                |
                PRIMITIVE                                                      NON PRIMITIVE
                                                                                     |
                                                                        -----------------------------
                                                                        |                           |
                                                                      LINEAR                   NON LINEAR
        """

# Q.
a,b,c = map(int, input("Enter 3 numbers: ").split())          #to take the input from the user that is space seperataed
li=list(int(x) for x in input().split())                      #to take the input from the user in the list is space seperataed
if a == len(li):
  for i in li:
    if i >= b and i <= c:
      print(i, end=" ")
else:
  print("Invalid Input")
  exit()