#let matrix be 8/8
mat=[[0 for x in range(8)]for x in range(8)]
for row in range(8):
    for col in range(8):
        if (row+col) % 2 ==0:
            mat[row][col]="*"
        else:
            mat[row][col]="_"
for row in mat:
    print(" ".join(row))



















    """for col in range(mat):
         if (row + col) % 2 ==0:
              print("*")"""
        
            
