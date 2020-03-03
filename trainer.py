import sys
import csv

mileage = []
price = []
theta0 = 0.0
theta1 = 0.0
m = 0
iterations  = 2000
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

def linearRegression():
    tmp0 = theta0
    tmp1 = theta1
    
    for i in range(0, iterations):
    
        d0 = 0.0
        d1 = 0.0
        
        for j in range(0, m):
            d0 += tmp0 + (tmp1 * mileage[j] / 10000) - price[j]
            d1 += (tmp0 + (tmp1 * mileage[j] / 10000) - price[j]) * mileage[j] / 10000
        d1 = d1/m
        d0 = d0/m
        new0 = tmp0 - (learningRate * d0)
        new1 = tmp1 - (learningRate * d1)  
        
        tmp0 = new0
        tmp1 = new1
    
    return [tmp0, tmp1]

def train(str):
    print("\n=== This is the trainer ===")
    filename = "data.csv"
    if str != None:
        filename = str
    readData(filename)
    print(m)
    teta = linearRegression()
    print("teta")
    print(teta)

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        train(None)
    else:
        train(sys.argv[1])
