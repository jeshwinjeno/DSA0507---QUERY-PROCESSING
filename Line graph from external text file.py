import matplotlib.pyplot as plt

# Create a text file
with open("data.txt", "w") as f:
    f.write("1 10\n2 20\n3 15\n4 25")

x, y = [], []
with open("data.txt") as file:
    for line in file:
        a, b = line.split()
        x.append(int(a))
        y.append(int(b))

plt.plot(x, y)
plt.title("Line Graph from File")
plt.show()
