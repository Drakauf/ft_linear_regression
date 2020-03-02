import sys

def help():
    print ("\n\t---------- Usage ---------- \n\n python3 main.py -[e|t] [filename] [filename?]\n\t\t-e => estimate, takes a csv file with 2 values in first row to estimate price\n\t\t-t => train, takes a csv files with data for estimations")
    sys.exit()
