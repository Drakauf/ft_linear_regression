import sys
import csv
from numbers import Number

def estimate(str):
    print("\n=== This is the estimator ===")
    teta0 = 0
    teta1 = 0
    filename = "estimateData.csv"

    if str != None:
        filename = str

    try:
        with open(filename, 'r') as f:
            fcsv = csv.reader(f, delimiter=',')
            try:
                for line in fcsv:
                    try:
                        teta0 = int(line[0])
                        teta1 = int(line[1])
                    except ValueError:
                        try:
                            teta0 = float(line[0])
                            teta1 = float(line[1])
                        except ValueError as e:
                            sys.exit('Not a valid number %s' % e)
            except csv.Error as err:
                sys.exit("An error occured when reading file: %s" % err)
    except IOError:
        print("File not accessible")
    while True:
        mileage = 0
        estimate = 0
        try:
           mil = input("Car's mileage: ")
        except EOFError:
            sys.exit(0)
        except:
            sys.exit(0)
        try:
            mileage = int(mil)
            estimate = float(teta0) + (float(teta1) * mileage / 10000)
            print('Estimated price: %d' %(int(estimate)))
        except ValueError as e:
            print("Not a valid number(enter an int): %s" %(mil))

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        estimate(None)
    else:
        estimate(sys.argv[1])
