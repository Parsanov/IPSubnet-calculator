from ipaddress import ip_address, IPv4Address

def ipToBinarySystem(ip):

    binaryArr = []

    octectsArr = ip.split(".")

    ipNumber = [int(x) for x in octectsArr] 


    for octets in ipNumber:
        binaryArr.append(octetsToBinary(octets))        

    return binaryArr
        

def octetsToBinary(octets) -> str:
    tempStr = ""
    tempNumber = octets
    for power in [128, 64, 32, 16, 8, 4, 2, 1]:
    
        if tempNumber >= power:
            tempStr += "1"
            tempNumber -= power
        else:
            tempStr += "0"
    return tempStr



            
def validIp4v(IP: str):
    try:
        return True if type(ip_address(IP)) is IPv4Address else False
    except ValueError:
        return False
