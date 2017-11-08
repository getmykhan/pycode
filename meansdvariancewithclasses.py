class MSV:
    
    def __init__(self, listt):
        self.list = listt
    
    def Mean(self):
        """ Calculate the Average """
        return (sum(self.list) / len(self.list))
    
    def sd(self):
        """ Calculate the Standard Deviation """
        self.sd = 0
        for i in self.list:
            self.sd = self.sd + (i - (sum(self.list) / len(self.list))) **2
        self.val = math.sqrt(self.sd / len(self.list))
        return(math.sqrt(self.sd / len(self.list)))
    
    def vr(self):
        """ Calculate the Variance """
        self.vr = self.val**2
        return(self.vr)