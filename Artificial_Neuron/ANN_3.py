import matplotlib.pylab as plt
import numpy as np

print("\n*************************************************")
print("* Written by: Natalie Jane Pacificar BSCS 2B-AI *")
print("*************************************************\n")
print("ENTER WEIGHTS in Integer Values\n")

x = np.arange(-8, 8, 0.1)

w1 = 2 * int(input("w1: ")) + 1
w2 = 2 * int(input("w2: ")) + 1
w3 = 2 * int(input("w3: ")) + 1

l1 = 'w1 = {}'.format(w1)
l2 = 'w2 = {}'.format(w2)
l3 = 'w3 = {}'.format(w3)

for w, l in [(w1,l1), (w2,l2), (w3,l3)]:
    f = 1 / (1 + np.exp(-x*w))
    plt.plot(x, f, label = l)

plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.show()

#Code Attributions:
# Snippet from the book, 
# 'An introduction to neural networks for beginners by Andy Thomas'
