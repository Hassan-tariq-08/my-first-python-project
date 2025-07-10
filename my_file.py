import numpy as np
import time

x = np.linspace(0, 1, 201)
y = np.random.random(201)

header = "X-Column, Y-Column\nThis is a second line"

with open('AD_data.dat', 'w') as f:
    np.savetxt(f, [], header=header)
    
    for i in range(201):
        data = np.column_stack((x[i], y[i]))
        np.savetxt(f, data.reshape(1, -1))  # Write one row at a time
        f.flush()  # Force immediate write to disk
        time.sleep(0.05)
