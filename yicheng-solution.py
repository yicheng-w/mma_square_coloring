import itertools as i

def inflate(s):
    [a0, a1, a2, b0, b1, b2, c0, c1, c2] = list(s)
    return [ [a0, a1, a2], \
             [b0, b1, b2], \
             [c0, c1, c2] ]

def deflate(square):
    [ [a0, a1, a2], \
      [b0, b1, b2], \
      [c0, c1, c2] ] = square
    return "".join([a0, a1, a2, b0, b1, b2, c0, c1, c2])

def rotate_cw(s):
    [ [a0, a1, a2], \
      [b0, b1, b2], \
      [c0, c1, c2] ] = inflate(s)
    return deflate([ [c0, b0, a0], \
                     [c1, b1, a1], \
                     [c2, b2, a2]])

def flip_in_place(square):
    return list(map(
        lambda row: list(map(
            lambda x : 'W' if x == 'G' else 'G', row)), square))

def flip_horizontal(s):
    [ [a0, a1, a2], \
      [b0, b1, b2], \
      [c0, c1, c2] ] = inflate(s) 
    return deflate(
            flip_in_place([ [a2, a1, a0], \
                            [b2, b1, b0], \
                            [c2, c1, c0] ]))
 
def flip_diagonal(s):
    [ [a0, a1, a2], \
      [b0, b1, b2], \
      [c0, c1, c2] ] = inflate(s) 
    return deflate(
            flip_in_place([ [c0, c1, c2], \
                            [b0, b1, b2], \
                            [a0, a1, a2] ]))
  
def all_squares():
    return i.product('GW', repeat=9)

if __name__ == '__main__':
    unique = set([])

    for s in all_squares():
        is_new = True
        # for each of the four rotations, check all possible flipping positions
        # unflipped, flipped-h, flipped-d
        for _ in range(4):
            if not is_new:
                continue

            if s in unique:
                is_new = False
            if flip_horizontal(s) in unique:
                is_new = False
            if flip_diagonal(s) in unique:
                is_new = False

            s = rotate_cw(s)

        if is_new:
            unique.add(s)

    print(len(unique))

