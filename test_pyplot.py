import matplotlib.pyplot as plt

x = [n for n in range(0,20,1)]
y = [n*n for n in range(0,20,1)]

print(x)
print(y)

plt.title("LE SUPER GRAPH")
plt.xlabel("absisse")
plt.ylabel("ordonnée")
plt.grid(which = 'major', axis = 'x', color = 'k', linestyle = '--', linewidth = 0.3)
plt.plot(x, y, color ='r', linestyle = '-')
plt.show()