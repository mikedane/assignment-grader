import os


class Screen(object):

    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def print_title(cls):
        title = ".--------------. .--------------. .--------------. .--------------. .--------------.\n" \
                "|  _________   | |  _________   | |    _______   | |  _________   | |  _______     |\n" \
                "| |  _   _  |  | | |_   ___  |  | |   /  ___  |  | | |  _   _  |  | | |_   __ \    |\n" \
                "| |_/ | | \_|  | |   | |_  \_|  | |  |  (__ \_|  | | |_/ | | \_|  | |   | |__) |   |\n" \
                "|     | |      | |   |  _|  _   | |   '.___`-.   | |     | |      | |   |  __ /    |\n" \
                "|    _| |_     | |  _| |___/ |  | |  |`\____) |  | |    _| |_     | |  _| |  \ \_  |\n" \
                "|   |_____|    | | |_________|  | |  |_______.'  | |   |_____|    | | |____| |___| |\n" \
                "|              | |              | |              | |              | |              |\n" \
                "'--------------' '--------------' '--------------' '--------------' '--------------'\n\n" \


        print(title)

    @classmethod
    def reset_screen(cls):
        cls.clear_screen()
        cls.print_title()

    class PrintInColor:
        _RED = '\033[91m'
        _BLUE = '\033[94m'
        _GREEN = '\033[92m'
        _YELLOW = '\033[93m'
        _LIGHT_PURPLE = '\033[94m'
        _PURPLE = '\033[95m'
        _DEFAULT = '\033[0m'

        @classmethod
        def red(cls, message="red"):
            print(cls._RED + message + cls._DEFAULT)

        @classmethod
        def blue(cls, message="blue"):
            print(cls._RED + message + cls._DEFAULT)

        @classmethod
        def green(cls, message="green"):
            print(cls._GREEN + message + cls._DEFAULT)

        @classmethod
        def yellow(cls, message="yellow"):
            print(cls._YELLOW + message + cls._DEFAULT)

        @classmethod
        def lightPurple(cls, message="light purple"):
            print(cls._LIGHT_PURPLE + message + cls._DEFAULT)

        @classmethod
        def purple(cls, message="purple"):
            print(cls._PURPLE + message + cls._DEFAULT)
