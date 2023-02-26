# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [3, 5, 7, 9]

# plt.grid(True)
# plt.xlabel('My x Values')
# plt.ylabel('My y Values')
# plt.title('My Frist Graph')
# plt.axis([0, 5, 2, 10])
# plt.plot(x,y,'b-*', linewidth=3, markersize=20)
# plt.show()


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [3, 5, 7, 9]
# z = [10, 8, 6, 4]

# plt.grid(True)
# plt.xlabel('My x Values')
# plt.ylabel('My y Values')
# plt.title('My Frist Graph')
# plt.axis([0, 5, 2, 11])

# plt.plot(x,y,'b-*', linewidth=3, markersize=7, label='Blue Line')
# plt.plot(x, z, 'r:o', linewidth=3, markersize=7, label='Red Line')
# plt.legend(loc='best')

# plt.show()

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)
#y3 = np.(x) - 4

plt.grid(True)
plt.xlabel('My x Values')
plt.ylabel('My y Values')
plt.title('My Frist Graph')
# plt.axis([0, 5, 2, 11])

plt.plot(x,y1, 'b-*',linewidth=3, markersize=7, label='Blue Line')
plt.plot(x,y2, 'r-o',linewidth=3, markersize=7, label='Red Line')
# plt.plot(x,y3, 'g-^',linewidth=3, markersize=7, label='Green Line')
plt.legend(loc='best')

plt.show()