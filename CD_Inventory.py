#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# FMitsiopoulos, 2022-Mar-20, completed TODOs
#------------------------------------------#


lstofCDObjects = []
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    # -- Fields -- #
    cd_id = 0
    cd_title = ''
    cd_artist = ''
    
    # -- Constructors -- #
    def __init__(self, cd_id, cd_title, cd_artist):   # __init__ is a method, self is first parameter
        # -- Atributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # setter and getter for cd_id 
        
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if value == int:
            self.__cd_id = value
        else:
            Exception('ID must be an integer!')
        
    # setter and getter for cd_title
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self,value):
        if str(value).isnumeric():
            raise Exception('Title must be a string!')
        else:
            self.__cd_title = value
            
    # setter and getter for cd_artist
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self,value):
        if str(value).isnumeric():
            raise Exception('Artist must be a string!')
        else:
            self.__cd_artist = value    

    # -- Methods -- #
    
    def cdList(self):
        return '{},{},{}'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def __str__(self):
        return self.cdList()

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries
        
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        Args:
        file_name (string): name of file used to read the data from
        table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
        None.
        """
        lstofCDObjects.clear()  # this clears existing data and allows to load data from file
                
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': (data[0]), 'Title': data[1], 'Artist': data[2]}
                lstofCDObjects.append(dicRow)
            objFile.close()
        except FileNotFoundError as e:
            print(e)
            print('Sorry, that file does not exist!')

    # TODone Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """ Save inventory in memory into text file
    
        Args:
            objFile: file that data is saved into
            cdList: List of CDs 
            rowLst: individual CDs from list
        
        Return: None
        """
        
        try:
            objFile = open(file_name, 'w')
            for row in table:
                rowLst = row.cdList()
                objFile.write(rowLst)
            objFile.close()
            print('CD Inventory has been saved.')
        except:
            print('Your CD Inventory has not been saved! Please try again')


# -- PRESENTATION (Input/Output) -- #
class IO:
    
    # TODone  add docstring
    """Handling Input / Output"""
    
    # TODone add code to get CD data from user
    @staticmethod
    def user_CDInput():
        """Function to create new dictionary
    
        Args:
            intID: gets ID number from user
            strTitle: gets CD title from user
            strArtist: gets CD artist from user
        
        Returns: None
        """
        
        while True:
            strID = input('Enter ID: ').strip()
            try:  # Handling a non integer response from user for ID
                intID = int(strID)
                break
            except ValueError as e:
                print(e)
                print('Please enter an integer!')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, strArtist

    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

# -- Main Body of Script -- #
# TOD Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects)

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstofCDObjects)
            IO.show_inventory(lstofCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstofCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        cdID, cdArtist, cdTitle = IO.user_CDInput()
        cdList = CD(cdID, cdArtist, cdTitle)
        lstofCDObjects.append(cdList)
        print('CD has been created. Please remember to save all new data!')
        continue  # start loop back at top.
    # show user current inventory    
    elif strChoice == 'i':
        IO.show_inventory(lstofCDObjects)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstofCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstofCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
