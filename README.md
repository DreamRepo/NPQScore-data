# NPQ Score dataset

The goal of the NPQ Score dataset is to provide a dataset containing the experiments results of the fluorescence of algae in different conditions.

To access the dataset, unzip `dataset.zip`

## Explanation of the dataset

#### The experiments are following this pattern :

| EXPERIMENT GROUP A |
|-- |
| run 1 - pattern group 0 - pattern number 0 |
| run 2 - pattern group 0 - pattern number 1 |
| run 3 - pattern group 0 - pattern number 2 |
| run 4 - pattern group 0 - pattern number 3 |
|activation |
|relaxation|
|run 5 - pattern group 1 - pattern number 0|
|run 6 - pattern group 1 - pattern number 1|
|run 7 - pattern group 1 - pattern number 2|
|run 8 - pattern group 1 - pattern number 3|
|...|

| EXPERIMENT GROUP B |
|-- |
| run 17 - pattern group 0 - pattern number 0 |
| run 18 - pattern group 0 - pattern number 1 |
| run 19 - pattern group 0 - pattern number 2 |
| run 20 - pattern group 0 - pattern number 3 |
|activation |
|relaxation|
|run 21 - pattern group 1 - pattern number 0|
|run 22 - pattern group 1 - pattern number 1|
|run 23 - pattern group 1 - pattern number 2|
|run 24 - pattern group 1 - pattern number 3|
|...|

#### The dataset is composed of 3 CSV files containing the NPQ score data :

### params_npq_score.csv

This file contains, for each algae of each experiment, all the parameters and configuration.


x_coords|y_coords|surface|algae|strain_state|monoclonal|activation_time|limit_blue|camera_heat_delay|period_SP|label|synchronized|strain|relaxation_time|gain|pattern_group|HL_time|variant|length_SP|exposure|experiment|limit_blue_high|actinic_filter|number_algae|pattern_number|limit_blue_low|run_id
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
61.58426966292135|510.0674157303371|89|1.0|Pop-qE|no|243.72|40.0|250.0|20000.0|3.0|yes|stt7-1|48.94|70.0|1.0|15.0|A6|200.0|170.0|b|450.0|1.0|114.0|3.0|0.0|20
80.84|485.84|75|2.0|Pop-qE|no|243.72|40.0|250.0|20000.0|3.0|yes|stt7-1|48.94|70.0|1.0|15.0|A6|200.0|170.0|b|450.0|1.0|114.0|3.0|0.0|20
107.12820512820512|493.87179487179486|39|3.0|Pop-qE|no|243.72|40.0|250.0|20000.0|3.0|yes|stt7-1|48.94|70.0|1.0|15.0|A6|200.0|170.0|b|450.0|1.0|114.0|3.0|0.0|20
113.64102564102564|331.2564102564103|39|4.0|Pop-qE|no|243.72|40.0|250.0|20000.0|3.0|yes|stt7-1|48.94|70.0|1.0|15.0|A6|200.0|170.0|b|450.0|1.0|114.0|3.0|0.0|20
... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

Description of columns :
- **x_coords** : average x coordinate of the algae on the video (in pixels)
- **y_coords** : average y coordinate of the algae on the video (in pixels)
- **surface** : surface size of the algae (in pixels)
- **algae** : number of the specific algae in the experiment 
- **strain** : strain used
- **pattern_group** : see pattern group in the table describing experiment pattern above
- **length_SP** : duration of the saturating pulse (ms)
- **monoclonal** : whether the population is isogenic or not
- **exposure** : exposure time of the camera
- **HL_time** : duration of the HL exposure (min)
- **relaxation_time** : time of relaxation after activation (in minutes)
- **actinic_filter** : density filter placed in front of the actinic LED on the set-up
- **limit_blue_high** : light intensity during the HL (µE/m²/s)
- **limit_blue_low** : light intensity in the dark  (µE/m²/s)
- **period_SP** : periodicity of Saturating pulses (ms)
- **synchronized** : whether the cell population is synchronised (12h/12h)
- **camera_heat_delay** : the experiment starts in the dark to allow the camera to heat-up and stabilise (s)
- **variant** : population variant
- **pattern_number** : see pattern number in the table describing experiment pattern above
- **number_algae** : number of the algae in the experiment
- **strain_state** : 'Pop-0', 'Pop-qE','Pop-qI', 'Pop-qT', 'wt4', 'cc124'
- **gain** : gain of the camera
- **activation_time** : time of activation, exposition to light (in minutes)
- **run_id** : number of the run/experiment, see run in the table describing experiment pattern above.
- **experiment**: Letter corresponding to an experiment group (algae on the same pad exposed to several consecutive patterns). Experiments run from a to n. 

### metrics_npq_score.csv

This csv contains, for each algae of each experiment, the time value series of the measured fluorescence (91 measures).

run_id | algae | 1 | 2 | 3 | 4 | 5 | 6 | ... | 91
| ------   | ------ | ------   | ------   | ------ | ------ | ------   | ------   | ------   | ------   
1 | 2 | 79.63636363636364 | 95.8181818181818 | 94.72727272727272 | 91.27272727272728 | 90.27272727272728 | 89.0909090909091 | ... | 81.36363636363636
1 | 3 | 92.5 | 108.91666666666669 | 107.44444444444444 | 105.13888888888889 | 103.38888888888889 | 101.83333333333331 | ... | 92.72222222222224
1 | 4 | 140.046875 | 133.484375 | 134.234375 | 129.59375 | 127.5625 | 125.984375 | ... | 112.96875
... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

- **run_id** : number of the run/experiment, see run in the table describing experiment pattern above.
- **algae** : number of the specific algae in the experiment 
- **1 to 91** : measured fluorescence value at the corresponding timestamp - values in the tables were taken every 20 seconds starting from 250 after the begining of the recording. Exact timestamps for each run can be found in the file timestamps_npq_score.csv.

The columns in `metrics_npq_score.csv` can be matched with the colums in `params_npq_score.csv` on columns `run_id` and `algae`


### timestamps_npq_score.csv

This csv contains, for each experiment the exact timestamps corresponding to measures 1 to 91, starting from approximatively 250 seconds and then every 20 seconds.

| run_id | 1 | 2 | 3 | 4 | ... | 91 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
1 | 249.6871410000604 | 269.66409500001464 | 289.6404140000232 | 309.6174030000111 | ... | 2047.6062559999991
2 | 249.6866150000133 | 269.66305999993347 | 289.640478999936 | 309.6170550000388 | ... | 2047.6020749999443
3 | 249.6891949999845 | 269.6659950000467 | 289.6430020000553 | 309.61994700005744 | ... | 2047.6034960000543
... | ... | ... | ... | ... | ... | ... | ... | ... | ... |





- **run_id** : number of the run/experiment, see run in the table describing experiment pattern above.
- **1 to 91** : corresponding exact timestamp at the given point.

## Prerequisites for the following parts
To be able to execute the scripts in the following parts, you will need to have a working Python environment (Python 11 or later) - local or virtual.

Then install the needed packages in `requirements.txt` with the following command : `pip install -r requirements.txt`



## Filter data

If you want you can also use the provided tool (`filter_experiments.py`) to filter the data on certain parameters, they just need to be in the columns of `params_npq_score.csv`

To do so, you will need to have a working python environment - or venv and install requirements.txt : `pip install -r requirements.txt`

### 1. Write a query file
- Create a CSV file with 4 columns : param, param_type, operator, value.
- Very important, the values have to be delimited by comma `,` otherwise it will not work.
- You can follow the example of `queries/query.csv`

- Explanation of the columns :
  - `param` : name of the param on which you want to set a filter
  - `param_type` : type of variable of the param (`text`, `number`, `bool`)
  - `operator` : `==`, `>`, `>=`, `<`, `<=`, `!=`, `between`
  - `value` : value to compare to, for operator `between` separate min and max value with `;`
- Save it in the folder `queries`.


### 2. Run the filtering script
- You can use a query file to filter CSV files containing experiments (metrics and params) using the command `python filter_experiments.py query.csv`
- First argument is the query file, specify the query file name including '.csv' (which has to be located in the `queries` folder)
- You can add arguments to the command line :

  - `-n` or `--export_name`, how you want to name your exported files, they will be named : `metrics_[export_name].csv` and `params_[export_name].csv` if not specified export_name will be equal to query filename (`metrics_[query].csv` and `params_[query].csv`)

- The filtered files (`metrics` & `params`) will be exported to the `filtered` folder.





## Test the dimension reduction

First, create a new python environment and activate it. If you have never done it, you can follow these [instructions](https://github.com/Alienor134/Teaching/blob/master/Python/Installing_Anaconda_creating_environment.md). You should install **Python 3.10** in the environment.

```conda create -n npq python=3.10```

```conda activate npq```


Install the required packages with the command line: 

```pip install -r requirements.txt```

Ensure you have unzipped **Dataset.zip**

Open Jupyter Lab. You can use the command line by simply typing: 

```jupyter lab```

=======