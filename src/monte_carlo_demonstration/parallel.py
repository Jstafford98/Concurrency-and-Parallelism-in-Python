import math
import random
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

__all__ = ['pi_monte_carlo_slow', 'pi_monte_carlo_fast']

def calculate_point() -> int :

    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    origin_dist = rand_x**2 + rand_y**2

    if origin_dist <= 1:
        return 1

    return 0

def calculate_multiple_points(total_points : int) -> tuple[int, int] :
    
    total_circles = 0
    total_squares = 0

    for _ in range(total_points):
        total_circles += calculate_point()
        total_squares += 1

    return total_circles, total_squares

def pi_monte_carlo_slow(domain : int) -> float :
    '''
        This implementation is intentionally bad with the intent of showing how Parallelization can
        actually make a program slower if implemented in a bad way (or in an inappropriate scenario)
    '''

    def _pi(total_circle : int, total_square : int) -> float :
        return 4 * total_circle / total_square

    total_points = domain ** 2

    circle_points = 0
    square_points = 0

    scheduled_bar = tqdm(total=total_points, position=0, leave=False, desc='Scheduled')
    completed_bar = tqdm(total=total_points, position=1, leave=False, desc='Completed')
    
    executor = ProcessPoolExecutor()

    with executor, scheduled_bar, completed_bar :

        futures = []

        for i in range(total_points):
            futures.append(
                executor.submit(calculate_point)
            )
            scheduled_bar.update()

        for future in as_completed(futures):
            circle_points += future.result()
            square_points += 1
            completed_bar.update()

    pi = _pi(circle_points, square_points)

    # print(f'Pi [Estimated]: {pi:.5f}')
    # print(f'Pi [Actual] : {math.pi:.5f}')

    return pi

def pi_monte_carlo_fast(domain : int, batch_size : int) -> float :

    def _pi(total_circle : int, total_square : int) -> float :
        return 4 * total_circle / total_square

    total_points = domain ** 2

    circle_points = 0
    square_points = 0

    total_full_batches = total_points // batch_size
    last_batch_remainder = total_points - (total_full_batches * batch_size)

    batches = [*[batch_size]*total_full_batches, last_batch_remainder]
    total_batches = len(batches)

    batch_completed_bar = tqdm(total=total_batches, position=0, leave=False, desc='Batch Completed')

    executor = ProcessPoolExecutor()

    with executor, batch_completed_bar:

        futures = []
        
        for batch in batches:

            futures.append(
                executor.submit(calculate_multiple_points, batch)
            )

        for future in as_completed(futures):

            n_circles, n_square = future.result()
            circle_points += n_circles
            square_points += n_square

            batch_completed_bar.update()
    
    pi = _pi(circle_points, square_points)

    # print(f'Pi [Estimated]: {pi:.5f}')
    # print(f'Pi [Actual] : {math.pi:.5f}')

    return pi

