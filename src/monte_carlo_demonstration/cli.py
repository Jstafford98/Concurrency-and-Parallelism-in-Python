import argparse

__all__ = ['CLI']

class CLI(argparse.ArgumentParser):

    def __init__(self) -> None :

        super().__init__()

        self.add_argument('--domain', required=True, type=int)
        self.add_argument('--batch_size', required=True, type=int)

    def parse(self) -> tuple[int, int] :
        args = self.parse_args()
        return args.domain, args.batch_size

if __name__ == '__main__':
    print(CLI().parse())