#from lab2.utils import get_random_number_generator


class BoxWindow:
    """[summary]"""

    def __init__(self, args):
        """initialize the BoxWindow with the bounding points

        Args:
            args (np.array([integer])): array of the bounding points of the box
        """
        self.bounds = args

    def __str__(self): #manière de print l'objet
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        return ("BoxWindow: " + str(self.bounds))

    def __len__(self): #dimension, faire dependre la fonction dimension et len
        return

    def __contains__(self, args): #si x est ds la boite/utiliser  dans indicator_function?
        return True or False

    def dimension(self):
        """[summary]"""
        return

    def volume(self):
        """[summary]"""
        return

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)


c = BoxWindow(np.array([[2.5, 2.5]]))
c.bounds
