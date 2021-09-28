benco2000 = "b"

def is_unique(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if (i!=j)and (L[i]==L[j]):
                return False
    return True


def triangle_shape(height):
    if height == 0:
        return str()
    else :
        for i in range (height):
            esp = height-1-i
            mot = esp*" " + (2*i+1)*"x"
            print(mot)
