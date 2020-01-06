class Abstract_Model:
    def __init__(self, name):
        self.name = name

    def train(self):
        print('old method train')

    def predict(self):
        pass

class LSTM(Abstract_Model): ## LSTM inherits from Abstract_Model                                                                                                                              
    def train(self):
        ## whatever is done in the base train, is also done here                                                                                                                              
        super().train()
        print('new method train')
        self.train = True
