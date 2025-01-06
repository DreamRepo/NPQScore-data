import os
import pandas as pd
import csv
import datetime

def get_export_name(export_name, query_file):
    """
    Takes in an export name and a query file and gives a name according to those files
    :param export_name: specified export name of the export file wanted (can be None - in this case will be named after the query file)
    :param query_file: the export name will be named after the query file (can be None - will be named full_database.csv)
    :return: export file name (str)
    """
    if export_name is not None and '.csv' not in export_name:
        return export_name + '.csv'

    elif query_file is None:
        return 'full_database.csv'

    else:
        return query_file.split('/')[1]


def get_surface_min_max(csv_file):
    """
    Takes in a csv file containing a query and search for the surface parameter which is not handle like the other ones (specific for each algae in every experiment)
    :param csv_file: query file
    :return: min and max surface values
    """
    if csv_file is not None:
        with open('queries/' + csv_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if len(row) == 4:
                    param, param_type, operator, value = row

                    if param == 'surface':
                        min_max = value.split(';')

                        if len(min_max) == 2:
                            return float(value.split(';')[0]), float(value.split(';')[1])

                        else:
                            print('Min Max value not properly specified')
                            return 0, 10000
    else:
        return 0, 10000


def get_experiment_from_csv(query_file, csv_file, source_folder, export_name, export_folder):
    """
    Same as the function above but extracts experiments from csv files instead of a database
    :param query_file: csv query file
    :param csv_file: name of the csv file containing the config/params and metrics
    :param source_folder: folder containing the params and metrics files
    :param export_name: export name
    :param export_folder: export folder
    """
    df_params = pd.read_csv(source_folder + '/params_' + csv_file + '.csv')
    df_metrics = pd.read_csv(source_folder + '/metrics_' + csv_file + '.csv')

    export_name = get_export_name(export_name, query_file)

    df_params_filtered = filter_params_on_query(query_file, df_params)
    df_metrics_filtered = filter_metrics_on_params(df_params_filtered, df_metrics)

    df_params_filtered.to_csv(export_folder + '/params_' + export_name, index=False)
    df_metrics_filtered.to_csv(export_folder + '/metrics_' + export_name, index=False)

    print(f"All the experiments have been exported to the {export_folder} folder.")


def filter_params_on_query(query_file, df_params_input):
    """
    Function that filters a dataframe containing experiments params/config according to a csv query file
    :param query_file: name of the csv query file (ex: query_example.csv) containing the query
    :param df_params_input: dataframe to filter
    :return: dataframe filtered
    """

    df_params = df_params_input.copy()
    file = open(query_file, 'r')
    reader = csv.reader(file, delimiter=',')
    count = 0

    for row in reader:
        if len(row) == 4 and count > 0:
            param, param_type, operator, value = row
            if param_type == 'number' and operator != 'between':
                value = float(value)
            if operator == "==":
                df_params = df_params[df_params[param] == value]
            elif operator == ">":
                df_params = df_params[df_params[param] > value]
            elif operator == "<":
                df_params = df_params[df_params[param] < value]
            elif operator == ">=":
                df_params = df_params[df_params[param] >= value]
            elif operator == "<=":
                df_params = df_params[df_params[param] <= value]
            elif operator == "!=":
                df_params = df_params[df_params[param] != value]
            elif operator == "between":
                # Assuming value is in the format "min,max"
                min_value, max_value = value.split(";")
                df_params = df_params[df_params[param].astype(float) >= float(min_value)]
                df_params = df_params[df_params[param].astype(float) <= float(max_value)]
            else:
                print(f"Operator not recognized for {param}: {operator}")
        count += 1
    return df_params


def filter_metrics_on_params(df_params, df_metrics):
    """
    Filter the metrics dataframe based on the filtered params dataframe
    :param df_params: filtered params dataframe
    :param df_metrics: unfiltered metrics dataframe
    :return: filtered metrics dataframe
    """
    filtered_df_metrics = df_metrics[df_metrics.apply(lambda row: (row['run_id'], row['algae']) in zip(df_params['run_id'], df_params['algae']), axis=1)]
    return filtered_df_metrics
