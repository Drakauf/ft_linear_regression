import sys
import csv
from numbers import Number

def estimate(str):
    print("=== This is the estimator ===")
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
        sys.exit("File not accessible")
    while True:
        mileage = 0
        estimate = 0
        try:
           mil = input("Car's mileage: ")
        except EOFError:
            sys.exit(0)
        except:
            sys.exit(0)
        if mil == "quit":
            sys.exit("Quitting the beautiful estimator")
        try:
            mileage = int(mil)
            if mileage > 0:
                estimate = float(teta0) + (float(teta1) * mileage / 10000)
                if estimate >= 0:
                    print('Estimated price: %d\n' %(int(estimate)))
                else:
                    print("It no longer has any value\n")
            else:
                print("Enter valide mileage\n")
        except ValueError as e:
            print("Not a valid number(enter an int): %s\n" %(mil))

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        estimate(None)
    else:
        estimate(sys.argv[1])
