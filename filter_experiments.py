from utils import FilterExp as getexp
import argparse
import os

if __name__ == '__main__':

    query = None
    export_name = None

    if not os.path.exists('filtered'):
        os.mkdir('filtered')

    parser = argparse.ArgumentParser(description="Export full database to csv")
    parser.add_argument('query', type=str)
    parser.add_argument('-n', '--export_name', type=str)
    args = parser.parse_args()

    query_file = 'queries/' + args.query

    if args.export_name:
        export_name = args.export_name

    if os.path.exists("dataset/dataset"):
        source_folder = 'dataset/dataset'
    else:
        source_folder = 'dataset'

    getexp.get_experiment_from_csv(query_file, 'npq_score', source_folder=source_folder, export_name=export_name, export_folder='filtered')
