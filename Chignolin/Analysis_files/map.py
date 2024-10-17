import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Rank two states
rank_two_states = np.array([
    0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.729, 0.000, 0.000, 0.000,
    1.195, 0.000, 0.000, 0.000, 0.000, 1.754, 0.000, 0.000, 1.497, 0.000,
    0.000, 0.000, 1.145, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 4.319,
    0.000, 0.000, 1.650, 0.000, 0.000, 0.000, 1.827, 0.000, 0.000, 0.000,
    0.000, 0.000, 0.000, 0.000, 0.000
])

in_name = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45
])


# Create contact list
cont_list = []
coeff_list = []
counter = 0
for i in range(10):
    for j in range(i):
          cont_list.append([i, j])
          coeff_list.append(rank_two_states[counter])
          counter += 1
print(cont_list)
print(coeff_list)
n = 45
colors = plt.cm.viridis(np.linspace(0, 1, n))  # Example colormap

fig, ax = plt.subplots(figsize=(4.8, 7))
ax.axis('off')
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-8, 6)

coords = np.array([
    [-2.8, -7],
    [-3.4, -4],
    [-3.2, -1],
    [-2.8, 2],
    [-1.6, 4.5],
    [1.6, 4.5],
    [2.8, 2],
    [3.2, -1],
    [3.4, -4],
    [2.8, -7]
])

for i in range(10):
    x, y = coords[i]
    circle = plt.Circle((x, y), 0.7, color='black')
    ax.add_patch(circle)

for c in range(len(cont_list)):
    i, j = cont_list[c]
    alpha = coeff_list[c]/max(coeff_list)
    ax.plot([coords[i, 0], coords[j, 0]], [coords[i, 1], coords[j, 1]], 
            color='black', 
            lw=alpha*10, alpha=alpha, zorder=0)

for i in range(10):
    x, y = coords[i]
    circle = plt.Circle((x, y), 0.6, color='darkgrey')
    ax.text(x, y, f'{i + 1}', fontsize=20, ha='center', va='center', fontweight='medium', c='k')
    ax.add_patch(circle)

norm = matplotlib.colors.Normalize(vmin=0, vmax=45)
sm = plt.cm.ScalarMappable(norm=norm, cmap=plt.cm.Blues)



fig.savefig('contactsDeepTDA_ranking.png', dpi=300, bbox_inches='tight')
plt.title('Deep-TDA Lasso',fontsize=16)
plt.show()

