def example_method(point_x, point_y):
    """Example of a method's documentation.

    Parameters
    ----------
    point_x : float
        Description of the first param
    point_y : float
        Description of the second param
    """
    print(point_x + point_y)

    # After you verified this method works, please delete it ;)
    print('Yay! It works!')


def new_method():
    """test

    """

    for i in range(3):
        print(i)


class myClass():

    def __init__(self, x):
        self.variable = x

    def my_print(self):
        print(self.variable)

    def MYTEST(self):
        print("you didn't correct me")
