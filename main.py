import sys
import helper as h
import estimator as e

def checkArg(argv):
    nbArg = len(argv);
#    print(nbArg)
    if nbArg > 1:
        if argv[1] == "-e":
            if nbArg == 3:
                e.estimate(argv[2])
            else:
                e.estimate(None)
        if (argv[1] == "-t" and nbArg == 4):
            return([2, argv[2], argv[3]])
    h.help()

if __name__ == "__main__":
    launch = checkArg(sys.argv);
    #verify Args and route to estimater

    #verify Args and route to trainer
