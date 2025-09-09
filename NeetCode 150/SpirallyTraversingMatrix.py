class Solution:
    def spirallyTraverse(self, mat):
       # code here
       
       rows = len(mat)
       cols = len(mat[0])
       
       # left -> right
       # top -> bottom
       # right -> left
       # bottom -> top
       
       # initial state
       top = 0
       bottom = rows-1
       left = 0
       right = cols-1
       
       output = []
       
       while top<= bottom and left<=right:
           for i in range(left,right+1):
               output.append(mat[top][i])
           top+=1
           
           for i in range(top,bottom+1):
               output.append(mat[i][right])
           right-=1
           
           if top<=bottom:
               for i in range(right,left-1,-1):
                   output.append(mat[bottom][i])
               bottom-=1
           
           if left<=right:
               for i in range(bottom,top-1,-1):
                   output.append(mat[i][left])
               left+=1
       
       return output
