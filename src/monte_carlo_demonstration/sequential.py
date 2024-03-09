''' Sequential implementation of the Monte Carlo Pi estimation algorithm '''

import math
import random
from tqdm import tqdm

__all__ = ['pi_monte_carlo']

def calculate_point() -> int :
    ''' 
        Creates a random point in a 2x2 area. If the distance from the origin (0,0) is <= 1,
        we return a value of 1. Otherwise, return 0.
    '''
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    origin_dist = rand_x**2 + rand_y**2

    if origin_dist <= 1:
        return 1

    return 0

def pi_monte_carlo(domain : int) -> float :
    ''' Estimation of PI using the Monte Carlo algorithm '''

    def _pi(total_circle : int, total_square : int) -> float :
        return 4 * total_circle / total_square

    total_points = domain ** 2

    circle_points = 0
    square_points = 0

    with tqdm(total=total_points, position=0, leave=False, desc='Points Created') as bar:

        for _ in range(total_points):

            circle_points += calculate_point()
            square_points += 1

            bar.update()
    
    pi = _pi(circle_points, square_points)

    # print(f'Pi [Estimated]: {pi:.5f}')
    # print(f'Pi [Actual] : {math.pi:.5f}')

    return pi

if __name__ == '__main__' :
    pi_monte_carlo(domain=100)

