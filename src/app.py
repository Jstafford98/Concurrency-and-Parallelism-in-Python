''' Concurrency is about dealing with many things at once, but Parallelism is about doing many things at once '''

from utils import timer
from monte_carlo_demonstration.cli import CLI
from monte_carlo_demonstration import sequential, parallel

if __name__ == '__main__' :

    # domain, max_batch_size = CLI().parse()
    domain = 5000
    max_batch_size = 50_000

    print('----- Monte Carlo Estimation of PI [Sequential] -----')
    timer(sequential.pi_monte_carlo)(domain)
    print()

    print('-----  Monte Carlo Estimation of PI [Parallel]  -----')
    timer(parallel.pi_monte_carlo_fast)(domain, max_batch_size)