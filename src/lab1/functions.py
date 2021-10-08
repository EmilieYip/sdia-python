<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
benco2000 = 1


>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
def is_unique(x):
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


def triangle_shape(n, fillchar="x", spacechar=" "):
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
