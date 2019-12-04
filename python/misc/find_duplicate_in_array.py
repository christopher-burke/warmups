#!/usr/bin/env python3

"""Find duplicate in array.

In an array with integers between 1 and 1,000,000 one value
is in the array twice. How do you determine which one?
"""


from random import randint


def duplicate(A):
    """Find the duplicate in the array."""
    n = len(A)
    total = (n)*(n+1)//2
    sum_A = sum(set(A))
    missing_value = total - sum_A
    return A[missing_value-1]


def generate_array(random_duplicate):
    """Create an array with a random duplicate."""
    random_position = randint(1, 1000000)
    array = list(range(1, 1000001))

    if array[random_position] == random_duplicate:
        array[random_position+1] = random_duplicate
    else:
        array[random_position] = random_duplicate
    return (array, random_duplicate,)


def main():
    """Run sample duplicate functions. Do not import."""
    A, random_duplicate = generate_array(random_duplicate=36586)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=271266)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=383902)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=776320)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=702362)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=515717)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=748044)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=930975)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=342361)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=334401)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=717640)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=451307)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=238467)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=345717)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=178833)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=180919)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=593789)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=403092)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=825917)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=348832)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=672774)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=305029)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=476786)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=836183)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=829863)
    assert duplicate(A) == random_duplicate
    A, random_duplicate = generate_array(random_duplicate=74054)
    assert duplicate(A) == random_duplicate
    print('Passed.')


if __name__ == "__main__":
    main()
