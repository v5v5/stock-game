from get_list_params import get_list_values
import matplotlib.pyplot as plt
import datetime
import math
import numpy as np

valueCells = get_list_values()

now = datetime.datetime.now()
graph_name = "Total Shareholders' Equity"
y = valueCells[graph_name]
x = np.arange(now.year - len(y), now.year, 1)
plt.plot(x, y) 
plt.xlabel('Years') 
plt.xticks(range(min(x), math.ceil(max(x))+1))
plt.ylabel('Values') 
plt.title(graph_name) 
plt.show() 