benco2000 = "b"

def is_unique(L):
    """ takes a list of integers as input and returns True if the there is no duplicate items otherwise return False

    Args:
        L ([integer])

    Returns:
        [boolean]
    """
    for i in range(len(L)):
        for j in range(len(L)):
            if (i!=j)and (L[i]==L[j]):
                return False
    return True


def triangle_shape(height):
    """
    Define a function triangle_shape(height), that returns a string that forms a triangle with height prescribed by height

    Args:
        height ([integer])

    Returns:
        [string]
    """
    mot = str()
    if height == 0:
        return str()
    else :
        for i in range (height):
            esp = height-1-i
            mot = mot+ esp*" " + (2*i+1)*"x" +esp*" "
            if i!=height-1:
                mot = mot+ "\n"
        return(mot)
