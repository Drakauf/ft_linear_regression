import sys
import csv
import matplotlib.pyplot as plt

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
                        mileage.append(mil / 10000)
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
        d0 += t0 + (t1 * mileage[j]) - price[j]
        d1 += (t0 + (t1 * mileage[j]) - price[j]) * mileage[j]
    return([d0, d1])

def linearRegression():
    tmp0 = theta0
    tmp1 = theta1 
    for i in range(0, iterations):
        derives = derive(tmp0, tmp1)
        tmp0 = tmp0 - (learningRate * (derives[0]/m))
        tmp1 = tmp1 - (learningRate * (derives[1]/m))  
    return [tmp0, tmp1]

def write(destname, theta):
    try:
        with open(destname, 'w') as f:
            fcsv = csv.writer(f, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fcsv.writerow(theta)
    except IOError:
        sys.exit("File not accessible")

def train(src, dest ,g):
    print("\033[1;35m=== This is the trainer ===\033[m")
    filename = "data.csv"
    destname = "estimateData.csv"
    if src != None:
        filename = src
    if dest != None:
        destName = dest
    print("trainig with data in \033[1;31m%s\033[0m" %filename)
    readData(filename)
    print("-> Initial Theta0 = \033[1;31m%f\033[0m" %theta0)
    print("-> Initial Theta1 = \033[1;31m%f\033[0m" %theta1)
    print("-> m:Total values = \033[1;31m%d\033[0m" %m)
    print("-> Iterations = \033[1;31m%d\033[0m" %iterations)
    print("-> learningRate= \033[1;31m%f\033[0m" %learningRate)
    theta = linearRegression()
    print("-> Final Theta0 = \033[1;31m%f\033[0m" %theta[0])
    print("-> Final Theta1 = \033[1;31m%f\033[0m" %theta[1])
    print("output file: \033[1;31m%s\033[0m" %destName)
    write(destName, theta);
    if g:
        plt.plot(mileage, price, 'ro')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.plot([min(mileage), max(mileage)],[theta[0] + (theta[1] * min(mileage)), theta[0] + (theta[1] * max(mileage))])
        plt.show()

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        train(None, None, False)
    elif len(sys.argv) == 2:
        train(sys.argv[1], None, False)
    elif len(sys.argv) == 3 and sys.argv[2] == "-g":
        train(sys.argv[1], None, True)
    elif len(sys.argv) == 3 and sys.argv[2] != "-g":
        train(sys.argv[1], sys.argv[2], False)
    elif len(sys.argv) == 4 and sys.argv[3] == "-g":
        train(sys.argv[1], sys.argv[2], True)
