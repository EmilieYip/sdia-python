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
