# PrismBenchmarkAnalyzer
Used to analyze internal prism benchmarks

## Before you run this:
You need to install openpyxl by running `pip install openpyxl datetime pandas` or something similar based on your installation of python.

## Steps:
For people who can run jupyter notebooks locally:
* Enter the path to the log file in the first line of the second cell.
* "Run all" the cells of the notebook 
* After analysis, it will print out the mean and median of latency, mining time and confirmation depth
For people who can't run the jupyter notebook locally:
* cd into the directory where this program is stored
* Run `python analyzer.py`
* Enter the path to the log file when prompted.
* Analysis will begin. Once complete, it will output a file called analyzed_data.xlsx in the directory where analyzer.py is stored. That can now be used to calculate the median latencies.
