# import numpy library
import numpy as np

# Creating random vector of size 20 having only float in the range 1-20.
randomVector = np.random.uniform(1, 20, 20)

# Reshaping the array to 4 by 5
modifiedArray = randomVector.reshape(4, 5)

# Replacing the max in each row by 0
modifiedArray[np.arange(4), modifiedArray.argmax(axis=1)] = 0

# Print the output
print(modifiedArray)