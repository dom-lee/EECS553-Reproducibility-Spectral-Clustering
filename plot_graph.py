import argparse
import matplotlib.pyplot as plt
import pysc.datasets

def parse_args():
    parser = argparse.ArgumentParser(description='Run the experiments.')
    parser.add_argument('experiment', type=str,
                        choices=['cycle', 'grid', 'cycle_unequal', 'grid_unequal',
                                 'complete', 'mnist', 'usps', 'bsds'],
                        help="which experiment to perform")
    parser.add_argument('bsds_image', type=str, nargs='?',
                        help="(optional) the BSDS ID of a single " \
                             "BSDS image file to segment")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.experiment == 'cycle':
        dataset = pysc.datasets.SbmCycleDataset(k=10, n=1000, p=0.01, q=0.001)
    elif args.experiment == 'grid':
        dataset = pysc.datasets.SBMGridDataset(d=4, n=1000, p=0.01, q=0.001)
    elif args.experiment == 'complete':
        dataset = pysc.datasets.SbmCompleteDataset(k=5, n=100, p=0.2, q=0.01)
    elif args.experiment == 'mnist':
        dataset = pysc.datasets.MnistDataset(k=3, downsample=None)
    elif args.experiment == 'usps':
        dataset = pysc.datasets.UspsDataset(k=3, downsample=None)

    # Draw
    dataset.graph.draw()
    plt.show()


if __name__ == "__main__":
    main()
