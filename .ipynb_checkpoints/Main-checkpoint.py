#Driver for project, import and call functions here

#
# Created doc, imported Data_and_Validation and Fig2_Refractor
# Fig2_Refractor takes an array to test as an argument
#
#

import numpy as np

from Data_and_Validation import create_data, validate_data
from Fig2_Refractor import fig2_refractor

# static variables for testing, feel free to randomize variables as they are normalized within fig2
sa = np.array([-0.8805, 2.4457, -2.3205, -0.6008, 4.3338, 1.8333, -2.8744, 3.3924, 1.2878])
fig2_refractor(sa)