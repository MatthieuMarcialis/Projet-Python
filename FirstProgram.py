class demmarage:
    def __init__(self):
        """

        """
        RobotName = "Unknown"
        RobotAddress = "Unknown"
        AcqStatus = False
        RobotStatus = False
    
    def Linkup (self):
        """
        Permet la connexion avec le robot
        """
        RobotAddress_test = input()

        if RobotAddress_test == False:
            RobotAddress_test
        if RobotAddress_test == True:
            self.RobotAddress = RobotAddress_test
            self.RobotName = RobotAddress_test[-1,-3]

    

    def Acquisition(self):
        """
        Permet l'enregistrement des données du robot
        """

    def Status(self):
        """
        Permet la mise en marche ou l'arrêt du robot
        """