import argparse
from src.selection import selection

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-path', '--file_path', type=str, required=True)
    parser.add_argument('--low', nargs='?', default=0.001, type=float)
    parser.add_argument('--high', nargs='?', default=0.002, type=float)
    parser.add_argument('-S', '--subset-size', '--subset_size', type=int, required=True)
    parser.add_argument('-N', '--num-solutions', '--num_solutions', nargs='?', const=10, type=int)
    parser.add_argument('--verbose', action="store_true")
    args = parser.parse_args()

    selection(
        filepath=args.file_path,
        low=args.low,
        high=args.high,
        subset_size=args.subset_size,
        num_solutions=args.num_solutions,
        verbose=args.verbose)
