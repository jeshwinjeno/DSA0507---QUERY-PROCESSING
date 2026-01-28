import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3]
y1 = [2,4,6]
y2 = [1,3,5]

plt.plot(x,y1,label="Line 1")
plt.plot(x,y2,label="Line 2")
plt.legend()
plt.show()
