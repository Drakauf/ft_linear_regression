import sys
import helper as h

def checkArg(argv):
    nbArg = len(argv);
    print(nbArg)
    if (nbArg) > 1:
        if (argv[1] == "-e"):
            return([1, argv[2]])
        if (argv[1] == "-t" and nbArg == 4):
            return([2, argv[2], argv[3]])
    h.help()

if __name__ == "__main__":
    launch = checkArg(sys.argv);
    print("launch")
    print(launch[1])
    #verify Args and route to estimater

    #verify Args and route to trainer

    #verify Args and route to helper
    #Sys exit in helper
    print("main");
