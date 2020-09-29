import matplotlib.pyplot as plt
import numpy as np

with open("./out.txt", "r") as file:
    data = file.read()

data = data.split("\n")
data = list(map(float, data))

plt.clf()
plt.plot(data)
plt.show()
