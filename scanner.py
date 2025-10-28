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

    def _get_file_list(self) -> list:
        """
        gets a list of all files in the directoy to be scanned
        #TODO currently ignores directories, does not scan recusively
        """
        directoryContents =  os.listdir(self._directoryToScan)
        fileList = []
        for item in directoryContents:
            if os.path.isfile(f"{self._directoryToScan}/{item}"):
                fileList.append(item)
        return fileList

    def _get_file_contents(self, fileName) -> list:
        """
        gets all the content of a file and returns it as a list
        """
        if not isinstance(fileName, str):
            raise TypeError(f"fileName is {type(fileName)}, but must be a str")

        with open(fileName) as f:
            return f.readlines()

s = Scanner()
s._get_file_list()
# s.change_directory()
