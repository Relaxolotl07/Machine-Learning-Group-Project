#Driver for project, import and call functions here

#
# Created doc, imported Data_and_Validation and Fig2_Refractor
# Fig2_Refractor takes an array to test as an argument
#
#

import numpy as np

from Data_and_Validation import create_data, validate_data
from Fig2_Refractor import fig2_refractor

n= 10000
low  = -2.3205
high = 4.3338
# static variables for testing, feel free to randomize variables as they are normalized within fig2
sa = np.array([-0.8805, 2.4457, -2.3205, -0.6008, 4.3338, 1.8333, -2.8744, 3.3924, 1.2878])
n_1 = 1500
sa1 = np.random.uniform(-5, 5, n_1)
print(sa1)
""" sa1 = np. """
sa2 = create_data(n_1, low, high)
""" sa3 = create_data(n, low, high)
sa4 = create_data(n, low, high)
 """
print(f"Fixed Data: {sa} \n")
fig2_refractor(sa)
""" print(f"Random 1 Data: {sa1} \n")
fig2_refractor(sa1, n_1) """
print(f"Random 2 Data: {sa2}\n")
fig2_refractor(sa2, n_1, 50)
""" print(f"Random 3 Data: {sa3}\n")
fig2_refractor(sa3) """
""" print(f"Random 4 Data: {sa4}\n")
fig2_refractor(sa4)  """