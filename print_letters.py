"""
Project: Print letters in alphabet.
Description: This project showcases examples of printing alphabet letters using the asterisk (*) character in Python.
GitHub: Baypython
instagram: baypython
This project aims to provide examples of generating alphabet letters using the '*' character in the Python programming language. Each letter has its corresponding function (e.g., write_A) demonstrating how to print the respective letter pattern.

Feel free to use, modify, and distribute the code as needed. If you have any questions or suggestions, please reach out via email or GitHub.

Happy coding!
"""

"""
-EN-
Note: Some letters may already appear cropped!
For instance, the letter 'D' may look like the letter 'O' if it isn't cropped. Similarly, the letter 'B' may resemble the number '8' if its corners aren't cropped.

If there are no corners in the letter, the functions produce output in two different methods:

First Method: In this method, blank values are based on the empty spaces in rows and columns.
Second Method: In this method, filled values are based on the filled positions in rows and columns.
"""

"""
-TR-
Not: Bazı harfler zaten kırpılmış gibi görünebilir!
Örneğin,'D' harfi, kırpılmazsa 'O' harfi gibi görünebilir. Benzer şekilde, 'B' harfi, köşeleri kırpılmazsa '8' sayısına benzeyebilir.

Eğer harfte herhangi bir köşe bulunmuyorsa, fonksiyonlar iki ayrı yöntemle çıktı üretir:

Birinci Yöntem: Bu yöntemde, boşluk değerleri, satır ve sütunlardaki boşlukları temel alır.
İkinci Yöntem: Bu yöntemde, dolu değerleri, satır ve sütunlardaki dolu konumları temel alır.
"""


def write_A(character="*", l_size=9, end_space=1, crop_corners=True):
    """
        Generates and prints an uppercase letter 'A' with specified parameters.

        Parameters:
        - character (str): The character used to draw the 'A'.
        - l_size (int): The size of the letter 'A', representing both height and width.
        - end_space (int): The number of spaces between characters.
        - crop_corners (bool): If True, the corners of the 'A' will be cropped; if False, the full 'A' will be displayed.

        Returns:
        None
        """
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter A with cropping corners
                if i != 0 and i != l_size // 2 and j != 0 and j != l_size - 1 or (
                        i == 0 and (j == 0 or j == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter A without not cropping corners
                if i == 0 or i == l_size // 2 or j == 0 or j == l_size - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_B(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter B with cropping corners
                if i != 0 and i != l_size - 1 and i != l_size // 2 and j != 0 and j != l_size - 1 or (
                        j == l_size - 1 and (i == 0 or i == l_size - 1 or i == l_size // 2)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter B without not cropping corners
                if j == 0 or ((j < l_size - 1 and (i == 0 or i == l_size // 2 or i == l_size - 1)) or
                              ((0 < i < l_size // 2 or l_size // 2 < i < l_size - 1) and j == l_size - 1)):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_C(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter C with cropping corners
                if i != 0 and i != l_size - 1 and j != 0 or (j == 0 and (i == 0 or i == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter C without not cropping corners
                if i == 0 or i == l_size - 1 or j == 0:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_D(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter D, method one
                if i != 0 and i != l_size - 1 and j != 0 and j != l_size - 1 or (
                        j == l_size - 1 and (i == 0 or i == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter D, method two
                if j == 0 or (
                        (j < l_size - 1 and (i == 0 or i == l_size - 1)) or (0 < i < l_size - 1 and j == l_size - 1)):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_E(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter E with cropping corners
                if i != 0 and i != l_size // 2 and i != l_size - 1 and j != 0 or (
                        j == 0 and (i == 0 or i == l_size // 2 or i == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter E without not cropping corners
                if i == 0 or i == l_size // 2 or i == l_size - 1 or j == 0:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_F(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter F with cropping corners
                if i != 0 and i != l_size // 2 and j != 0 or (j == 0 and (i == 0 or i == l_size // 2)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter F without not cropping corners
                if i == 0 or i == l_size // 2 or j == 0:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_G(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter G with cropping corners
                if (
                        ((i == 0 or i == l_size - 1) and j == 0) or (
                        (i == l_size // 2 or i == l_size - 1) and j == l_size - 1) or
                        (i != 0 and i != l_size - 1 and j != 0 and
                         ((i < l_size // 2 and 0 < j < l_size - 1) or
                          (i == l_size // 2 and 0 < j < l_size // 2) or
                          (i > l_size // 2 and 0 < j < l_size - 1) or
                          (j == l_size - 1 and 0 < i < l_size // 2))
                        )
                ):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter G without not cropping corners
                if i == 0 or (i == l_size // 2 and j >= l_size // 2) or i == l_size - 1 or j == 0 or (
                        (l_size // 2 <= i < l_size - 1) and j == l_size - 1):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_H(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter H with method one
                if (
                        j == 0 or
                        j == l_size - 1 or
                        (i == l_size // 2 and 0 < j < l_size - 1)
                ):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)
            else:
                # Print letter H with method two
                if j == 0 or j == l_size - 1 or i == l_size // 2:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_I(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter I with method one
                if i != 0 and i != l_size - 1 and j != l_size // 2:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter I with method two
                if j == l_size // 2:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_J(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter J with cropping corners
                if ((j != l_size // 2 and 0 < i < l_size - 1) or (i == l_size - 1 and j > l_size // 2 - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter J without not cropping corners
                if i == 0 or j == l_size // 2 or (i == l_size - 1 and 0 < j <= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_K(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter K with method one
                if j != 0 and j != l_size // 2 + 1 - i and i != l_size // 2 - 1 + j:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter K with method two
                if j == 0 or (i + j == l_size // 2 + 1) or i - j == l_size // 2 - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_L(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter L with cropping corners
                if ((j != l_size // 2 and 0 <= i < l_size - 1) or (i == l_size - 1 and j < l_size // 2 + 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter L without not cropping corners
                if j == l_size // 2 or (i == l_size - 1 and j >= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_M(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter M with method one
                if j != 0 and (i != j and j <= l_size // 2) or (
                        (i != l_size - j - 1 and l_size // 2 <= j < l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter M with method two
                if j == 0 or j == l_size - 1 or (i == j and j <= l_size // 2) or (
                        i + j == l_size - 1 and j >= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_N(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter N with method one
                if j != 0 and j != l_size - 1 and i != j:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter N with method two
                if j == 0 or j == l_size - 1 or i == j:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_O(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter O, with cropping corners
                if i != 0 and i != l_size - 1 and j != 0 and j != l_size - 1 or (
                        j == l_size - 1 and (i == 0 or i == l_size - 1)) or (j == 0 and (i == 0 or i == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter O, without cropping corners
                if i == 0 or i == l_size - 1 or j == 0 or j == l_size - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_P(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter P with cropping corners
                if i != 0 and i != l_size // 2 and j != 0 and j != l_size - 1 or (
                        j == l_size - 1 and (i == 0 or i >= l_size // 2)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter P without not cropping corners
                if i == 0 or i == l_size // 2 or j == 0 or (j == l_size - 1 and i < l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_Q(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter O, with cropping corners
                if i != 0 and i != l_size - l_size // 2 + 1 and j != 0 and j != l_size - l_size // 2 + 1 and i != j or (
                        i == j and i <= l_size // 2) or (
                        (i == 0) and j >= l_size - l_size // 2 + 1) or ((j == 0) and i >= l_size - l_size // 2 + 1) or (
                        (
                                j > l_size - l_size // 2 + 2 or j == l_size - l_size // 2 + 1) and i > l_size - l_size // 2 + 1) or (
                        i == l_size - l_size // 2 + 1 and j > l_size - l_size // 2 + 1):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter O, without cropping corners
                if ((i == 0 or i == l_size - l_size // 2 + 1) and j <= l_size - l_size // 2 + 1) or (
                        (j == 0 or j == l_size - l_size // 2 + 1) and i <= l_size - l_size // 2 + 1) or (
                        l_size - 1 >= i >= l_size // 2 and l_size // 2 + 3 >= j > l_size // 2 and i == j):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


"""
Version_2 Letter R with cropped corners:

if (i != 0 and i != l_size // 2 and j != 0 and j != l_size - 1) or 
(j == l_size - 1 and (i == 0 or i == l_size // 2)) or 
(i > l_size // 2 and i != j - 1 and 0 < j < l_size - 1)"""


def write_R(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter R with cropping corners
                if i != 0 and j != 0 and (i > l_size // 2 and j != -l_size // 2 + i + 1 and j > 0) or (
                        0 < i < l_size // 2 and 0 < j < l_size - 1) or (
                        (i == 0 or i == l_size // 2) and j == l_size - 1):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter R without not cropping corners
                if i == 0 or i == l_size // 2 or j == 0 or (j == l_size - 1 and i < l_size // 2) or (
                        i > l_size // 2 and j == -l_size // 2 + i + 1):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_S(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter S with cropping corners
                if i != 0 and i != l_size - 1 and i != l_size // 2 and j != 0 and j != l_size - 1 or (
                        (j == l_size - 1) and (i == l_size - 1 or 0 < i <= l_size // 2)) or (
                        j == 0 and (l_size // 2 <= i < l_size - 1 or i == 0)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter S without not cropping corners
                if i == 0 or i == l_size // 2 or i == l_size - 1 or (j == 0 and i <= l_size // 2) or (
                        j == l_size - 1 and i >= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_T(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter T with method one
                if i != 0 and j != l_size // 2:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter T with method two
                if i == 0 or j == l_size // 2:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_U(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter U with cropping corners
                if i != l_size - 1 and j != 0 and j != l_size - 1 or (i == l_size - 1 and (j == 0 or j == l_size - 1)):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter U without cropping corners
                if i == l_size - 1 or j == 0 or j == l_size - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_V(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter V with method one
                if j != 0 and j == l_size - 1 and (j == l_size - 1 and i > l_size // 2) or (
                        i < l_size // 2 and 0 < j < l_size - 1) or (
                        i >= l_size // 2 and j >= l_size // 2 and j != -i + l_size + l_size // 2 - 1) or (
                        i >= l_size // 2 and j <= l_size // 2 and j - i != -l_size // 2 + 1
                ):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter V with method two
                if (j == 0 and i <= l_size // 2) or \
                        (j == l_size - 1 and i <= l_size // 2) or \
                        ((i >= l_size // 2 and j <= l_size // 2) or (i >= l_size // 2 and j >= l_size // 2)) and \
                        (j - i == -l_size // 2 + 1 or j == -i + l_size + l_size // 2 - 1):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_W(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter W with method one
                if j != 0 and j != l_size - 1 and ((i != j and i >= l_size // 2)) and (
                        j + i != l_size - 1 and i >= l_size // 2) or (0 < j < l_size - 1 and i < l_size // 2):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter W with method two
                if j == 0 or j == l_size - 1 or (i == j and i >= l_size // 2) or (
                        j + i == l_size - 1 and i >= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_X(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter Y with method one
                if i != j and j + i != l_size - 1:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter Y with method two
                if i == j or j + i == l_size - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_Y(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter Y with method one
                if ((i != j and j + i != l_size - 1) or i >= l_size // 2) and (j != l_size // 2) or (
                        j == l_size // 2 and i < l_size // 2):
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter Y with method two
                if ((i == j or j + i == l_size - 1) and i < l_size // 2) or (j == l_size // 2 and i >= l_size // 2):
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def write_Z(character="*", l_size=9, end_space=1, crop_corners=True):
    for i in range(l_size):
        for j in range(l_size):
            if crop_corners:
                # Print letter Z with method one
                if i != 0 and i != l_size - 1 and j + i != l_size - 1:
                    print(" ", end=" " * end_space)
                else:
                    print(character, end=" " * end_space)
            else:
                # Print letter Z with method two
                if i == 0 or i == l_size - 1 or j + i == l_size - 1:
                    print(character, end=" " * end_space)
                else:
                    print(" ", end=" " * end_space)

        # Move to the next line after completing each row
        print("")


def show_two_methods(l_function, crop_corners):
    for i in range(2):
        l_function(character, l_size, end_space, crop_corners)
        print("\n")
        crop_corners = not crop_corners


def show_all(character, l_size, end_space, crop_corners, letter_functions):
    for i in letter_functions.keys():
        l_function = letter_functions.get(i)
        l_function(character, l_size, end_space, crop_corners)
        print("\n" + "-" * l_size * 2)


letter_functions = {
    'A': write_A,
    'B': write_B,
    'C': write_C,
    'D': write_D,
    'E': write_E,
    'F': write_F,
    'G': write_G,
    'H': write_H,
    'I': write_I,
    'J': write_J,
    'K': write_K,
    'L': write_L,
    'M': write_M,
    'N': write_N,
    'O': write_O,
    'P': write_P,
    'Q': write_Q,
    'R': write_R,
    'S': write_S,
    'T': write_T,
    'U': write_U,
    'V': write_V,
    'W': write_W,
    'X': write_X,
    'Y': write_Y,
    'Z': write_Z,
}

l_size = 9  # Default size, only odd numbers
character = "*"  # Default character
end_space = 1  # default space 1 or 0
crop_corners = True  # Default cropped

if __name__ == "__main__":
    # Show the all letters
    # show_all(character, l_size, end_space, crop_corners, letter_functions)
    while True:
        selection = input("Enter a letter to print : ").upper()
        if selection.lower() == "exit":
            break
        if selection in letter_functions.keys():
            w_function = letter_functions.get(selection)
            w_function(character, l_size, end_space, crop_corners)
            # Show the letter as with cropped and not cropped (or with two methods)
            # show_two_methods(w_function,crop_corners)
            continue
        print("This letter not found in dictionary. Please try again")
