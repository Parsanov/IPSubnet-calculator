from subnetcalc.core import ipToBinarySystem, validIp4v



def main():

    userIp = input("Enter your ip: ")

    if validIp4v(userIp):
        print("The ip is valid")

        binaryArr = ipToBinarySystem(userIp) 
        
        print(binaryArr)

    elif validIp4v(userIp):
        print("The ip is invalid")


 

if __name__ == '__main__':
    main()

