class Matrix:
    def __init__(self, m, n):
        """Initialises (with zeros) a matrix of dimensions m by n."""
        self.matrix = [[0 for _ in range(n)] for _ in range(m)]
        self.n_row = m
        self.n_col = n
            

    def __str__(self):
        """Returns a string representation of this matrix as integers in the form:
          a b c
          d e f
          g h i
        Used as follows: s = str(m1)
        """
        
        str_list = [' '.join(map(str, self.matrix[i])) for i in range(self.n_row)]
        string = '\n'.join(str_list)
        
        return string

    def get(self, key):
        """Returns the (i,j)th entry of the matrix, where key is the tuple (i, j)

        Used as follows: x = matrix.get((0,0))
        * raises IndexError if (i,j) is out of bounds
        """
        row_valid = key[0] < self.n_row and key[0] >= 0
        col_valid = key[1] < self.n_col and key[1] >= 0
        
        if not row_valid or not col_valid:
            raise IndexError
        
        return self.matrix[key[0]][key[1]]

    def set(self, key, data):
        """Sets the (i,j)th entry of the matrix, where key is the tuple (i, j)

        and data is the number being added.
        Used as follows: matrix.set((0,0), 1)
        * raises IndexError if (i,j) is out of bounds
        * raises TypeError if data is not an integer
        """
        row_valid = key[0] < self.n_row and key[0] >= 0
        col_valid = key[1] < self.n_col and key[1] >= 0
        
        if not row_valid or not col_valid:
            raise IndexError
    
        if not isinstance(data, int):
            raise TypeError

        self.matrix[key[0]][key[1]] = data

    def add(self, other):
        """Adds self to another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.add(m2) => m1 + m2
        or: m1.add(3) => m1 + 3
        * raises TypeError if other is not a Matrix object or an integer
        * raises ValueError if the other Matrix does not have the same dimensions
        """
        
        is_int = isinstance(other, int)
        is_matrix = isinstance(other, Matrix)
        if not is_int and not is_matrix:
            raise TypeError
        if is_matrix and (self.n_row != other.n_row or self.n_col != other.n_col):
            raise ValueError
        
        return_matrix = Matrix(self.n_row, self.n_col)
        
        if is_int:
            return_matrix.matrix = [[self.matrix[j][i] + other for i in range(self.n_col)] for j in range(self.n_row)]
        else:
            return_matrix.matrix = [[sum(x) for x in zip(self.matrix[i], other.matrix[i])] for i in range(self.n_row)]
            
        return return_matrix

    def mul(self, other):
        """Multiplies self with another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.mul(m2) m1 x m2 (matrix multiplication, not point-wise)
        or: m1.mul(3) => m1*3
        * raises TypeError if the other is not a Matrix object or an integer
        * raises ValueError if the other Matrix has incorrect dimensions
        """
        is_int = isinstance(other, int)
        is_matrix = isinstance(other, Matrix)
        if not is_int and not is_matrix:
            raise TypeError
        if is_matrix and self.n_col != other.n_row:
            raise ValueError
        
        if is_int:
            return_matrix = Matrix(self.n_row, self.n_col)
            return_matrix.matrix = [[self.matrix[j][i] * other for i in range(self.n_col)] for j in range(self.n_row)]
        else:
            return_matrix = Matrix(self.n_row, other.n_col)
            return_matrix.matrix = [[mul_helper(self.matrix[j], col(other.matrix, i)) for i in range(other.n_col)] for j in range(self.n_row)]

        return return_matrix

def mul_helper(row, col):
    return sum([row[i] * col[i] for i in range(len(row))])

def col(matrix, index):
    return [matrix[i][index] for i in range(len(matrix))]

if __name__ == '__main__':

    matrix = Matrix(4,3)
    matrix1 = matrix.add(1)
    print(str(matrix1))
