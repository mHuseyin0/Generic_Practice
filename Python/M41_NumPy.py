import numpy as np

def printWithDash(*args):
    print(f"\n")
    for i in args:
        print(i, end=" ")
    print(f"\n\n"+"-"*50)

if __name__ == "__main__":
    array1 = np.array([[2,4],[6,8]])
    array2 = np.array([[2,4],[6,8]])
    array3 = np.full((1,1,1,1), 1)
    array4 = np.full((2,2,2,2), 10)
    array5 = np.array([1,2,3,4,5,6,7,8,9])
    np.random.shuffle(array1)
    printWithDash(f"array1 == array2:\n", array1 == array2)
    printWithDash(f"array1 == array2:\n", array1 == array2)
    printWithDash(f"array1:\n", array1)
    printWithDash(f"array1/2:\n", array1/2)
    printWithDash(f"np.arange(5):\n", np.arange(5))
    printWithDash(f"np.arange(5,10):\n", np.arange(5,10))
    printWithDash(f"np.arange(5,10,2):\n", np.arange(5,10,2))
    printWithDash(f"np.arange(7, 11, dtype='complex'):\n", np.arange(7, 11, dtype='complex'))
    printWithDash(f"np.zeros((2,3,4,5)):\n", np.zeros((2,3,4,5)))
    printWithDash(f"np.zeros_like(array1):\n", np.zeros_like(array1))
    printWithDash(f"np.ones((1,1,1,1),dtype='int'):\n", np.ones((1,1,1,1),dtype="int"))
    printWithDash(f"np.ones_like(array1):\n", np.ones_like(array1))
    printWithDash(f"np.empty((2,2,2,2)):\n", np.empty((2,2,2,2),dtype="str"))
    printWithDash(f"np.empty_like(array1):\n", np.empty_like(array1))
    printWithDash(f"np.full((3,3,3,3), '3'):\n", np.full((3,3,3,3), "3"))
    printWithDash(f"np.full_like(array1, '1'):\n", np.full_like(array1, "1"))
    printWithDash(f"\nLinspace (Linear Space) Function")
    printWithDash(f"np.linspace(51, 100, dtype='int'):\n", np.linspace(51, 100, dtype="int"))
    printWithDash(f"np.linspace(50, 100, endpoint=False):\n", np.linspace(50, 100, endpoint=False))
    printWithDash(f"np.linspace(50, 100, 3, dtype='str'):\n", np.linspace(50, 100, 3, dtype="str"))
    printWithDash(f"np.linspace(50, 100, 3, retstep=True):\n", np.linspace(50, 100, 3, retstep=True))
    printWithDash(f"np.linspace(array3, array4, 4, axis=4, dtype='int'):\n",
            np.linspace(array3, array4, 4, axis=4, dtype="int"))
    printWithDash(f"np.eye(6, dtype='int'):\n", np.eye(6, dtype="int"))
    printWithDash(f"np.eye(6, 9, dtype='int'):\n", np.eye(6, 9, dtype="int"))
    printWithDash(f"np.eye(6, k=-1, dtype='int'):\n", np.eye(6, k=-1, dtype="int"))
    printWithDash(f"np.eye(6, k=-4, dtype='int'):\n", np.eye(6, k=-4, dtype="int"))
    printWithDash(f"np.eye(6, k=3, dtype='int'):\n", np.eye(6, k=3, dtype="int"))
    printWithDash(f"np.random.rand():\n", np.random.rand())
    printWithDash(f"np.random.rand(4,3,2):\n", np.random.rand(4,3,2))
    printWithDash(f"np.random.randn(2,2,2):\n", np.random.randn(2,2,2))
    printWithDash(f"np.random.randn(2):\n", np.random.randn(2))
    printWithDash(f"np.random.randn():\n", np.random.randn())
    printWithDash(f"np.random.ranf():\n", np.random.ranf())
    printWithDash(f"np.random.ranf(3):\n", np.random.ranf(3))
    printWithDash(f"np.random.randint(100):\n", np.random.randint(100))
    printWithDash(f"np.random.randint(100, 200, size=(3,4,5)):\n", array6 := np.random.randint(100, 200, size=(3,4,5)))
    printWithDash(f"np.random.randint(200, 300, size=10):\n", np.random.randint(200, 300, size=10))
    printWithDash(f"np.random.permutation(10):\n", np.random.permutation(10))
    printWithDash(f"np.random.permutation(array6):\n", np.random.permutation(array6)) # Reorders only the biggest dimension
    printWithDash(f"np.random.choice(array5):\n", np.random.choice(array5))
    printWithDash(f"array6.ndim:\n", array6.ndim)
    printWithDash(f"array6.shape:\n", array6.shape)
    printWithDash(f"array6.size:\n", array6.size) # Number of elements in the array
    printWithDash(f"array6.dtype:\n", array6.dtype) # All elements must be the same type in np arrays.
    printWithDash(f"array6.itemsize:\n", array6.itemsize) # How many bytes per each element
    printWithDash(f"array7:\n", array7 := np.zeros((2,2,2,2)))
    printWithDash(f"array7.astype(np.int8):\n", array7.astype(np.int8))
    printWithDash(f"array7:\n", array7)

    counter = 1
    array8 = np.full((3,3,3), fill_value=0, dtype=int)
    printWithDash(f"array8:\n", array8)
    for i in range(3):
        layer = np.empty((3,3))
        for j in range(3):
            row = np.empty(3)
            for k in range(3):
                row[k] = counter
                counter += 1
            layer[j] = row
        array8[i] = layer

    printWithDash(f"array8:\n", array8)
    printWithDash(f"array8[0][1][2]:\n", array8[0][1][2])

    index1 = np.array([0,5,8])
    index2 = np.array([0,2]), np.array([1,2]), np.array([0,0])
    array9 = np.arange(11)
    array10 = np.arange(7,18)
    array11 = np.arange(1,4)
    array12 = np.full((3,1), fill_value=0)
    array12[0][0] = 10
    array12[1][0] = 100
    array12[2][0] = 1000
    array13 = np.arange(1,4)

    printWithDash(f"array9:\n", array9)
    printWithDash(f"array9[1,2,1,2,1,2,3,3,3]:\n", array9[[1,2,1,2,1,2,3,3,3]])
    printWithDash(f"array9[index1]:\n", array9[index1])
    printWithDash(f"array8[index2]:\n", array8[index2])
    printWithDash(f"array8[[0,2],[1,2],[0,0]]:\n", array8[[0,2],[1,2],[0,0]])
    printWithDash(f"array8[array8 % 3 == 0]:\n", array8[array8 % 3 == 0])
    printWithDash(f"array9[array10 > 15] + 100:\n", array9[array10 > 10] + 100)
    printWithDash(f"array9:\n", array9)
    printWithDash(f"array10:\n", array10)
    printWithDash(f"array9 + array10:\n", array9 + array10)
    printWithDash(f"array8:\n", array8)
    printWithDash(f"array11:\n", array11)
    printWithDash(f"array11 + array8:\n", array8 + array11)
    printWithDash(f"array12:\n", array12)
    printWithDash(f"array13:\n", array13)
    printWithDash(f"array12 * array13:\n", array12 * array13)
    printWithDash(f"np.reshape(array9, (9,3), order='C'):\n", np.reshape(array8, (9,3), order="C"))
    printWithDash(f"np.reshape(array9, (3,9), order='F'):\n", np.reshape(array8, (9,3), order="F"))
    printWithDash(f"np.reshape(array9, (3,9), order='A'):\n", np.reshape(array8, (9,3), order="A"))
    printWithDash(f"array8:\n", array8)
    array8.reshape((3,9)) # Reshaping does not effect the original array
    printWithDash(f"array8:\n", array8)
    printWithDash(f"array8.resize(8, 4):\n", np.resize(array8, (8,4)))
    printWithDash(f"array8:\n", array8)
    array8.resize((3,9)) # Resizing does effect the original array
    printWithDash(f"array8:\n", array8)
    array8.resize((3,3,3)) # Resizing does effect the original array
    printWithDash(f"array8:\n", array8)
    printWithDash(f"array8.flatten('C'):\n", array8.flatten("C"))
    printWithDash(f"array8.flatten('F'):\n", array8.flatten("F"))
    printWithDash(f"array8:\n", array8)
    printWithDash(f"np.ravel(array8, 'C'):\n", np.ravel(array8, "C"))
    printWithDash(f"array8.ravel():\n", array8.ravel())
    printWithDash(f"array8:\n", array8)
    printWithDash(f"array6:\nShape: {array6.shape}\n\n", array6)
    printWithDash(f"np.transpose(array6):\nShape: {np.transpose(array6).shape}\n\n", np.transpose(array6))
    # When the axes are not specified, they reversed in order. (3,4,5) --> (5,4,3)
    printWithDash(f"array6.T:\nShape: {array6.T.shape}\n\n", array6.T)
    printWithDash(f"np.transpose(array6, (2,1,0)):\nShape: {np.transpose(array6, (2,1,0)).shape}\n\n", np.transpose(array6, (2,1,0)))
    printWithDash(f"array6.transpose((1,2,0)):\nShape: {array6.transpose((1,2,0)).shape}\n\n", array6.transpose((1,2,0)))
    printWithDash(f"array6:\nShape: {array6.shape}\n\n", array6)
    printWithDash(f"np.swapaxes(array6, 1, 2):\nShape: {np.swapaxes(array6, 1, 2).shape}\n\n", np.swapaxes(array6, 1, 2))
    printWithDash(f"array6.swapaxes(1, 0):\nShape: {array6.swapaxes(1, 0).shape}\n\n", array6.swapaxes(1, 0))
    # If axis is not specified, arrays will be flattened before being concatenated.
    # Dimensions must be same to concatenate two arrays.
    # Also axes must be same except the ones we concatenate.
    # Vstack function always concatenates arrays vertically. Other axes must be the same.
    # hstack function always concatenates arrays horizontally. Other axes must be the same.
    # However, they behave different for 1-D arrays. hstack concatenates them normally and returns a 1-D array.
    # Vstack concatenate them only if their length is the same and returns a 2-D array. Otherwise an error raises.
    printWithDash(f"array8:\n", array8)
    printWithDash(f"np.split(array8.flatten(), 3):\n", np.split(array8.flatten(), 3))
    printWithDash(f"np.hsplit(array8, 3):\n{np.hsplit(array8, 3)[0]}--\n{np.hsplit(array8, 3)[1]}--\n{np.hsplit(array8, 3)[2]}--")
    printWithDash(f"np.vsplit(array8, 3):\n{np.vsplit(array8, 3)[0]}--\n{np.vsplit(array8, 3)[1]}--\n{np.vsplit(array8, 3)[2]}--")
    # axis=0 for vsplit and axis=1 for hsplit
    printWithDash(f"np.split(array8, 3, axis=2):\n", np.split(array8, 3, axis=2))
    printWithDash(f"np.insert(array5, 5, 50):\n", np.insert(array5, 5, 50))
    printWithDash(f"np.insert(array5, (5,10), 50):\n", np.insert(array5, (5,9), 50))
    printWithDash(f"np.insert(array8, 0, 0,axis=0):\n", np.insert(array8, 0, 0, axis=0))
    printWithDash(f"np.insert(array8, 0, 0,axis=1):\n", np.insert(array8, 0, 0, axis=1))
    printWithDash(f"np.insert(array8, 0, 0,axis=2):\n", np.insert(array8, 0, 0, axis=2))
    printWithDash(f"np.insert(array8, 0, 0):\n", np.insert(array8, 0, 0))
    # When axis is not specified, array is flattened before inserting.
    printWithDash(f"np.append(array8, 0):\n", np.append(array8, 0))
    array14 = np.linspace(100,2700,num=27, dtype="int")
    array14.resize((3,3,3))
    printWithDash(f"array14:\n", array14)
    printWithDash(f"np.append(array8, np.split(array8, 3, axis=0)[0], axis=0):\n", np.append(array8, np.split(array8, 3, axis=0)[0], axis=0))
    printWithDash(f"np.append(array8, np.arange(1,10).reshape((1,9)).transpose((1,0))):\n", np.append(array8, np.arange(1,28).reshape((3,3,3)), axis=1))
    printWithDash(f"np.append(array8, array14, axis=2):\n", np.append(array8, array14, axis=2))
    printWithDash(f"np.delete(array8, 1, axis=0):\n", np.delete(array8, 1, axis=0))
    printWithDash(f"np.delete(array8, 1, axis=1):\n", np.delete(array8, 1, axis=1))
    printWithDash(f"np.delete(array8, 1, axis=2):\n", np.delete(array8, 1, axis=2))

    # Matrices (Always 2-D unlike arrays)
    printWithDash("array1.dot(array2):\n" ,array1.dot(array2))
    matrix1 = np.matrix("1,2;3,4")
    matrix2 = np.matrix("1 2;3 4")
    printWithDash(f"matrix1:\n", matrix1)
    printWithDash(f"matrix2:\n", matrix2)
    # * operator does not give matrix multiplication with arrays unlike matrix objects
    # Howewer + operator and .T to transpose will work with both of them
    printWithDash(f"matrix1 * matrix2:\n", matrix1 * matrix2)
    printWithDash(f"matrix2.T:\n", matrix2.T)
    printWithDash(f"np.linalg.inv(matrix2):\n", np.linalg.inv(matrix2))
    printWithDash(f"np.linalg.matrix_power(matrix1,2):\n", np.linalg.matrix_power(matrix1,2))
    printWithDash(f"np.linalg.matrix_power(matrix1,0):\n", np.linalg.matrix_power(matrix1,0))
    printWithDash(f"np.linalg.matrix_power(matrix1,-1):\n", np.linalg.matrix_power(matrix1,-1))
    printWithDash(f"np.linalg.solve(matrix2, np.array([5,6])):\n", np.linalg.solve(matrix2, np.array([5,6])))
    # Finds x and y values for the following equations:
    # x + 2y = 5
    # 3x + 4y = 6
    # Parameters can be as many as wanted
    printWithDash(np.linalg.det(matrix1))

    choice = 1#input("Enter 1 to display syntax of numpy and numpy.linspace(), any other thing to quit: ")
    if (choice == "1"):
        #help(np)
        help(np.linspace)

    # Revise all the document, especially insert function
