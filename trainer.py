import sys
import csv

mileage = []
price = []
theta0 = 0.0
theta1 = 0.0
m = 0
iterations  = 100000
learningRate = 0.01

def readData(str):
    global m
    try:
        with open(str, 'r') as f:
            fcsv = csv.reader(f, delimiter=',')
            try:
                for line in fcsv:
                    if fcsv.line_num != 1:
                        try:
                            mil= float(line[0])
                            pri = float(line[1])
                        except ValueError as e:
                            sys.exit('Not a valid number %s' % e)
                        mileage.append(mil)
                        price.append(pri)
            except csv.Error as err:
                sys.exit("An error occured when reading file: %s" % err)
    except IOError:
        sys.exit("File not accessible")
    mileage.pop(0)
    price.pop(0)
    m = len(price) 


def derive(t0, t1):
    d0 = 0.0
    d1 = 0.0
    for j in range(0, m):
        d0 += t0 + (t1 * mileage[j] / 10000) - price[j]
        d1 += (t0 + (t1 * mileage[j] / 10000) - price[j]) * mileage[j] / 10000
    return([d0, d1])

def linearRegression():
    tmp0 = theta0
    tmp1 = theta1 
    for i in range(0, iterations):
        derives = derive(tmp0, tmp1)
        tmp0 = tmp0 - (learningRate * (derives[0]/m))
        tmp1 = tmp1 - (learningRate * (derives[1]/m))  
    return [tmp0, tmp1]

def train(str):
    print("\n=== This is the trainer ===")
    filename = "data.csv"
    if str != None:
        filename = str
    readData(filename)
    print(m)
    theta = linearRegression()
    print("teta")
    print(theta)

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        train(None)
    else:
        train(sys.argv[1])
