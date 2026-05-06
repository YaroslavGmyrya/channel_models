import numpy as np
import sys
from itertools import batched
from dataclasses import dataclass
from pprint import pprint

import numpy as np
from itertools import batched


@dataclass
class MatrixCell:
    state: str
    bit: str
    metric: int


def conv_coder(bits, polynomes):
    if len(polynomes) <= 1:
        print("Function wait two and more polynomes!") 
        sys.exit(1)

    bin_poly = [bin(x)[2:] for x in polynomes]
    max_len = max(len(x) for x in bin_poly)
    bin_poly = [x.zfill(max_len) for x in bin_poly]

    ones_pos = []
    for el in bin_poly:
        tmp = [i for i, b in enumerate(el) if b == "1"]
        ones_pos.append(tmp)

    register = np.zeros(max_len, dtype=np.int8)
    outs = []

    for i in range(len(bits)):
        register[1:] = register[:-1]
        register[0] = bits[i]

        for pos in ones_pos:
            out = 0
            for j in pos:
                out ^= register[j]

            outs.append(out)

    return list(batched(outs, len(polynomes)))


def hamm_dist(a, b):
    if len(a) != len(b):
        print("Operandes must be have same length")
        sys.exit(1)

    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1

    return counter

def viterbi_decoder(bits, polynomes):
    if len(polynomes) <= 1:
        print("Function wait two and more polynomes!") 
        sys.exit(1)

    bin_poly = [bin(x)[2:] for x in polynomes]
    max_len = max(len(x) for x in bin_poly)
    bin_poly = [x.zfill(max_len) for x in bin_poly]

    count_of_states = 2**max_len
    matrix = [['' for _ in range(len(bits) +1)] for _ in range(count_of_states)]

    # fill start states
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tmp = MatrixCell(bin(i)[2:].zfill(max_len), '', 0)
            matrix[i][j] = tmp
    
    # pprint([[cell.metric for cell in row] for row in matrix])

    # fill matrix
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            reg_out = []

            cur_state = matrix[j][i].state

            # "1" branch
            new_state = "1" + cur_state[:-1]
            
            for k in range(len(bin_poly)):
                out = 0
                for m in range(len(new_state)):
                    reg_value = int(new_state[m], 10)
                    poly_value = int(bin_poly[k][m], 10)

                    out ^= reg_value * poly_value

                reg_out.append(str(out))
                ",".join(reg_out)

            print(reg_out)
            # "0" branch

    

    # fill matrix
    # for i in range(1, len(matrix[0])):



a = conv_coder([1, 0, 1], [0b011, 0b101])

# for i in a:
#     print(*i)

b = viterbi_decoder(a, [0b011, 0b101])