import os

class Scanner:
    """
    scanner class that scans directories for secrets and passwords

    Public Methods:
        change_directory
    """

    def __init__(self):
        """
        constructor method for Scanner class

        sets _directoryToScan as the current working directory by default
        """
        self._directoryToScan = os.getcwd()


    def get_directory_to_scan(self) -> str:
        """
        returns a string of the path to the directory to be scanned
        """
        return self._directoryToScan


    def change_directory(self, directoryPath:str=None):
        """
        Changes the directory to be scanned.
        User can pass the directory as an argument or input it through the
        terminal input request


        Parameters:
            directoryPath:
                str:
                    default None
                    A path to a directory can be passed with the method call
                    User must use absolute path to directory.
                    Example for Mac or Linux:
                        "/Users/ratman/Documents/"
        """
        if directoryPath is None:
            directoryPath = input("path to directory to scan "
                                "(example: /Users/{username}/Documents/) or "
                                "leave empty for current directory: ")

        # error check directory
        while not self._check_path(directoryPath):
            print("Invalid path, please enter a valid path to a directory")
            directoryPath = input("path to directory to scan "
                                "(example: /Users/{username}/Documents/) or "
                                "leave empty for current directory: ")
        self._directoryToScan = directoryPath

    def _check_path(self, directoryPath) -> bool:
        """
        error checking method to verify that a path is valid
        """
        try:
            if os.path.exists(directoryPath):
                return True
            return False
        except NameError:
            return False
        except SyntaxError:
            return False
        except TypeError:
            return False

# print_directory()
# try:
#     if directoryToScan:
#         print(os.listdir(directoryToScan))
#     else:
#         print(os.listdir())
# except FileNotFoundError:

s = Scanner()
# s.change_directory()
