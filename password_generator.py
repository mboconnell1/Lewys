import string
from random import randint, shuffle
from secrets import choice


class PasswordGenerator:
    """
    Generates customisable passwords.
        Properties:
            min_len           (int):    minimum password length (default = 8)
            max_len           (int):    maximum password length (default = 16)
            min_upper_chars   (int):    minimum uppercase characters (default = 1)
            min_lower_chars   (int):    minimum lowercase characters (default = 1)
            min_special_chars (int):    minimum special characters (default = 1)
            min_nums          (int):    minimum numbers (default = 1)
    """
    def __init__(self) -> None:
        self.min_len           = 8
        self.max_len           = 16
        self.min_upper_chars   = 1
        self.min_lower_chars   = 1
        self.min_special_chars = 1
        self.min_nums          = 1

        self.upper_chars = string.ascii_lowercase
        self.lower_chars = string.ascii_lowercase
        self.numbers     = string.digits

        self.special_chars = [
            '!',
            '$',
            '(',
            ')',
            '^',
            '%',
            '&',
            '*',
            '?'
            '=',
            '+',
            '-',
            '/',
            '*',
            '>',
            '<',
            ',',
            '.',
            '_',
            '#'
        ]
        self.all_chars = (
            list(self.lower_chars)
            + list(self.upper_chars)
            + list(self.numbers)
            + self.special_chars
        )

    def generate(self) -> str:
        """
        Returns a password conforming to class properties.
            Returns:
                password (str): Character string representing generated password.
        """
        if (
            self.min_len < 0
            or self.max_len < 0
            or self.min_upper_chars < 0
            or self.min_lower_chars < 0
            or self.min_special_chars < 0
            or self.min_nums < 0
        ):
            raise ValueError("Character length cannot be negative.")
        
        if self.min_len > self.max_len:
            raise ValueError(
                "Minimum length cannot exceed maximum length. \
                    The default maximum length is 16."
            )
        
        collective_min_length = (
            self.min_upper_chars + self.min_lower_chars
            + self.min_special_chars + self.min_nums
        )

        if collective_min_length > self.min_len:
            self.min_len = collective_min_length

        password = [
            choice(list(set(self.lower_chars)))
            for i in range(self.min_lower_chars)
        ]
        password += [
            choice(list(set(self.upper_chars)))
            for i in range(self.min_upper_chars)
        ]
        password += [
            choice(list(set(self.numbers)))
            for i in range(self.min_nums)
        ]
        password += [
            choice(list(set(self.special_chars)))
            for i in range(self.min_special_chars)
        ]

        current_len = len(password)
        if current_len < self.max_len:
            rand_len = randint(self.min_len, self.max_len)
            password += [
                choice(self.all_chars) for i in range(rand_len - current_len)
            ]
        
        shuffle(password)
        return "".join(password)
    

if __name__ == '__main__':
    # Example usage.
    gen = PasswordGenerator()
    gen.min_len = 12
    gen.min_special_chars = 3
    gen.min_nums = 4
    print(gen.generate())