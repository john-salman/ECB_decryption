import sys

def main():
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    
    flags = []
    outputs = []
    for line in lines:
        i = 5
        end = len(line)
        flag = ""
        output = ""
        while(line[i] != ":"):
            i += 1
        flags.append(line[0:i])
            
        i += 1
        outputs.append(line[i:end])
    

    
#    print flags
    print outputs


    end = len(flags)
    i = 0
    while(i < end):
        
main()
