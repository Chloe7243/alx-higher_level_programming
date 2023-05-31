#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int, optional): The size of a side of the square.
                Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.

        Returns:
            None.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of a side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of a side of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.

        Returns:
            None.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Compare if square is less than another by area

        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size > other.size
