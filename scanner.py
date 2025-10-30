import os, json, re

class Scanner:
    """
    scanner class that scans directories for secrets and passwords

    Public Methods:
        change_directory:
            changes working directory to be scanned
        scan:
            scans directory for secrets and passwords
    """

    def __init__(self, customRules="rules/rules.json"):
        """
        constructor method for Scanner class

        sets _directoryToScan as the current working directory by default
        """
        self._directoryToScan = os.getcwd()
        self._rulesData = {}

        # load rules
        rules_data = json.load(open(customRules))
        for rule in rules_data['rules']:
            regex = re.compile(rule['name'])
            self._rulesData[rule['regex']] = regex

    def get_current_rules(self) -> dict:
        """
        returns a dict of the current rule set and regex pattern
        """
        return self._rulesData

    def change_custome_rules(self, rulesPath: str) -> None:
        """
        change the custom rule set used for scanning

        Precondition:
            rulesPath must be of the correct type
            rulesPath must be a json file
            rulesPath must be a valid path to a directory

        Postcondition:
            updates self._rulesData to use the rules in rulesPath

        Raises:
            TypeError if rulesPath not of the correct type
            Invalid Path if rulesPath not a correct path
            FileError?? if rulesPath not a json file
        """
        if not isinstance(rulesPath, str):
            raise TypeError("rulesPath must be a str but is a "
                            f"{type(rulesPath)}")

        if not self._check_path(rulesPath): # check this is correct later
            raise Exception("rulesPath must be a valid path to a file")

        # TODO add a check to json

        # update ._rulesData
        self._rulesData = {}
        rules_data = json.load(open(rulesPath))
        for rule in rules_data['rules']:
            regex = re.compile(rule['name'])
            self._rulesData[rule['regex']] = regex


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

    def scan(self):
        """
        Scans self.__directoryToScan for secrets and passwords

        Returns:
            ?

        Precondition:
            self._directoryToScan must be a valid path to the directory


        Raises:
            ValueError:
                if self._directoryToScan is not a valid path to a directory
        """
        if not os.path.exists(self._directoryToScan):
            raise ValueError(f"self._directoryToScan: {self._directoryToScan} "
                             " is not a valid path to a directory")

        fileList = self._get_file_list()

        for fileName in fileList:
            fileContents = self._get_file_contents(fileName)
            # need method to scan file contents


    def _scan_for_secrets(self, fileContents: str):
        """
        internal method that scans a string for possible passwords and secrets

        Parameters:
            fileContents:
                a str from a file to scan

        Returns:
            unsure yet

        Precondition:
            fileContents must be of the correct type

        Raises:
            TypeError:
                if fileContents not of the correct type
        """

        if not isinstance(fileContents, str):
            raise TypeError("fileContents must be a str but is: "
                            f"{type(fileContents)}")

        # rules_data = json.load(open("rules.json"))

        # for rule in rules_data['rules']:
        #     regex = re.compile(rule['name'])
        #     print(regex)


s = Scanner()
s._scan_for_secrets('test')
# s.change_directory()
