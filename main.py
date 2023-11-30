import time
from random import randint
class Matrix:

  def __init__(self, matrixList):
    self.matrix = matrixList

  def __str__(self):
    output = ""
    for row in self.matrix:
      output += str(row) + "\n"
    return output

  def det_with_cofactor(self):
    if len(self.matrix) == len(self.matrix[0]):

      if len(self.matrix) != 2:
        count = 1
        new_matrix_shell = []
        for row in range(0, len(self.matrix)):

          new_row = []

          for column in range(0, len(self.matrix[row])):

            create_minor_matrix = []
            for new_rowr in range(0, len(self.matrix)):
              if new_rowr != row:

                create_minor_matrix.append([])
                for new_column in range(0, len(self.matrix[row])):

                  if new_column != column:

                    create_minor_matrix[len(create_minor_matrix) - 1].append(
                        self.matrix[new_rowr][new_column])

            new_minor = self.minorDet(create_minor_matrix)
            if count % 2 == 0:
              new_minor *= -1
            new_row.append(new_minor)
            count += 1
          new_matrix_shell.append(new_row)
        print(new_matrix_shell)
        current_count = 1
        running_total = 0
        
        for column in range(0, len(new_matrix_shell[0])):
          running_total += self.matrix[0][column] * new_matrix_shell[0][column]
          current_count += 1
        
        return {"det": running_total, "cofactor": new_matrix_shell}
    else:
      raise Exception(
          "Can't find Det of matrix. row count must equal column count")
    return {"det": 2, "cofactor": ["error"]}

  def det(self):
    if len(self.matrix) == len(self.matrix[0]):
      #find the inverse
      return self.minorDet(self.matrix)
    else:
      raise Exception(
          "Can't find Det of matrix. row count must equal column count")

  def minorDet(self, minorMatrix):

    if len(minorMatrix) == len(minorMatrix[0]):
      #find the inverse
      if len(minorMatrix) != 2:
        new_matrix_shell = []
        for row in range(0, len(minorMatrix)):

          new_row = []

          for column in range(0, len(minorMatrix[row])):

            create_minor_matrix = []
            for new_rowr in range(0, len(minorMatrix)):
              if new_rowr != row:

                create_minor_matrix.append([])
                for new_column in range(0, len(minorMatrix[row])):

                  if new_column != column:

                    create_minor_matrix[len(create_minor_matrix) - 1].append(
                        minorMatrix[new_rowr][new_column])

            new_minor = self.minorDet(create_minor_matrix)
            new_row.append(new_minor)

          new_matrix_shell.append(new_row)
        running_total = 0
        current_count = 1
        for column in range(0, len(new_matrix_shell[0])):

          if current_count % 2 == 0:
            #even multiply by  -1
            running_total += minorMatrix[0][column] * new_matrix_shell[0][
                column] * -1

          else:
            running_total += minorMatrix[0][column] * new_matrix_shell[0][
                column]
          current_count += 1
        return running_total
      else:
        return minorMatrix[0][0] * minorMatrix[1][1] - minorMatrix[0][
            1] * minorMatrix[1][0]
    else:
      raise Exception(
          "Can't find Det of matrix. row count must equal column count")

  def inverse(self):
    if len(self.matrix) == len(self.matrix[0]):
      #find the inverse
      det_cof = self.det_with_cofactor()
      if det_cof["det"] == 0:
        raise Exception("No inverse found det is 0")
      temp_matrix = det_cof["cofactor"]
      #transpose matrix

      for row in range(0, len(temp_matrix)):
        for column in range(1, len(temp_matrix)):
          temp_value = temp_matrix[row][column]
          temp_matrix[row][column] = temp_matrix[column][row]
          temp_matrix[column][row] = temp_value
      back_row_index = len(temp_matrix) - 1
      for row in range(1, len(temp_matrix)):
        temp_value = temp_matrix[row][back_row_index]
        temp_matrix[row][back_row_index] = temp_matrix[back_row_index][row]
        temp_matrix[back_row_index][row] = temp_value

      for row in range(0, len(temp_matrix)):
        for column in range(0, len(temp_matrix)):
          temp_matrix[row][column] *= (1 / det_cof["det"])
      newMatrix = Matrix(temp_matrix)
      return newMatrix
    else:
      raise Exception(
          "Can't find inverse of matrix. row count must equal column count")

  def __mul__(self,other):
    if type(other) == int or type(other) == float:
      #just a scalar multiplier
      matrix_shell = []
      for row_i in range(0,len(self.matrix)):
        matrix_shell.append([])
        for column_i in range(0,len(self.matrix[0])):
          matrix_shell[row_i].append(self.matrix[row_i][column_i]*other)
      return Matrix(matrix_shell)
    elif isinstance(other,Matrix):
      #do a matrix multiply

      #check if self.columns = other.row
      if len(self.matrix[0]) == len(other.matrix):
        #safe to multiply

        #loop through eacho row and multiply by each columm
        matrix_shell = []
        for row_i in range(0,len(self.matrix)):
          matrix_shell.append([])
          for other_column_i in range(0,len(other.matrix[0])):
            running_total = 0
            for column_i in range(0,len(self.matrix[0])):
              running_total += self.matrix[row_i][column_i]*other.matrix[column_i][other_column_i]
            matrix_shell[row_i].append(running_total)
        return Matrix(matrix_shell)
      else:
        raise Exception("Cannot multiply: columns must equal row")
      
  def __rmul__(self,other):
    if type(other) == int or type(other) == float:
      #just a scalar multiplier
      matrix_shell = []
      for row_i in range(0,len(self.matrix)):
        matrix_shell.append([])
        for column_i in range(0,len(self.matrix[0])):
          matrix_shell[row_i].append(self.matrix[row_i][column_i]*other)
      return Matrix(matrix_shell)

if __name__ == "__main__":

  print(Matrix([[1,3,-2],[-3,1,1],[-3,11,-4]]).inverse())
  total_time_count = 0
  total_matrix_time_count = 0
  matrix_size = 4
  itr = 1000
  exceptionsFound = 0
