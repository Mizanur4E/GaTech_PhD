import numpy as np
import matplotlib.pyplot as plt
""" A function will take dimension, Orthogonality threshold and sample size to test How many vectors are orthogonal or nearly orthogonal."""


def generate_random_bipolar_vectors(D, S, orthoTh):
    # Generate S random bipolar vectors of dimension D
    random_vectors = np.random.choice([-1, 1], size=(S, D))

    # Initialize count for nearly orthogonal vectors
    orthogonal_count = 0

    # Check orthogonality using dot product
    for i in range(1,S):
        dot_product = np.dot(random_vectors[0], random_vectors[i])

        # Check if the dot product is less than the orthogonality threshold
        if dot_product <= orthoTh:
            orthogonal_count += 1

    return orthogonal_count



D_arr = [ 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 5000]
Count = []
N = 100000

#loop over all dimension and generates N number of samples randomly and count the nearly orthonal vectors
for D in D_arr:
  th = 0.01*D
  Count.append(generate_random_bipolar_vectors(D, N, th))


plt.figure(figsize=(10, 6))
plt.plot(D_arr, Count, marker='o')
plt.title(f'Nearly Orthogonality Trends with Dimension: N = {N}')
plt.xlabel('Dimension')
plt.ylabel('# Nearly Orthogonals')
plt.grid(True)
plt.show()
