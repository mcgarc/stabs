import itertools
import numpy as np
import time
from BK import BKgraph

start_time = time.time()

DIM = 4

I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])

pauli = {'I':I, 'X':X, 'Y':Y, 'Z':Z}

# Build a list of all the combinations of puali operators, it is useful to
# create a dictionary where keys are the string representation, and values are
# the matrix
stabs = {}
for combo in itertools.product('IXYZ', repeat=DIM):
    # Get a string representation of the stabiliser
    combo_str = ''.join(combo)
    # Get a matrix representation of the stabiliser
    mat = pauli[combo[0]]
    for m in combo[1:]:
        mat = np.kron(mat, pauli[m])
    stabs[combo_str] = mat

# Now look for all the combinations that commute. Identity will commute with
# all of them, so we can discard it
del stabs['I'*DIM] 
commuters = {}
N = len(stabs)
for i in range(N):
    a_str = list(stabs.keys())[i]
    a = stabs[a_str]
    commuters[a_str] = []
    for j in range(i):
        b_str = list(stabs.keys())[j]
        b = stabs[b_str]
        commutator = np.matmul(a, b) - np.matmul(b, a)
        if not np.any(commutator):
            # Order a and b
            x, y = sorted((a_str, b_str))
            commuters[x].append(y)
            commuters[y].append(x)

graph_time = time.time()
print(f'Commuter graph built in {graph_time - start_time:.3}s')

# Now for all the stabilisers that commute, we need to find the groups of
# 2^DIM - 1that mutually commute (ignoring the 2^DIMth, which is the identity)
# Same as finding maximal cliques. Use BK algo
bk = BKgraph(commuters)
out = bk.output_strs()

#out = [ ' '.join(_) for _ in out ]
print(f'Total runtime: {time.time() - start_time:.3}s')
print(f'No. of stabilizers found: {len(out)}')
