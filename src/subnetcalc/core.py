
def ipToBinarySystem(ip):

    binaryArr = [] 

    ipNumber = transform_ip(ip)

    for octets in ipNumber:
        binaryArr.append(octetsToBinary(octets))        

    return binaryArr
        

def octetsToBinary(octet) -> str:
    tempStr = ""
    tempNumber = octet
    for power in [128, 64, 32, 16, 8, 4, 2, 1]:
    
        if tempNumber >= power:
            tempStr += "1"
            tempNumber -= power
        else:
            tempStr += "0"
    return tempStr


def transform_ip(ip: str):
     
     octetArr = ip.split(".")
    
     return [int(x) for x in octetArr] 


def validIp4v(ip: str):
    try:
        ipArr = ip.split(".")
        all_valid = all(p.strip().isdigit() for p in ipArr)

        if all_valid:
            numbers = transform_ip(ip)

            for num in numbers:
                if num <= 255 or num >= 0:
                    continue
                else:
                    return False

            return True
    
    except ValueError:
        return False
