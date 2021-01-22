import joblib

class modelM:
    """
    feed data into ML model and return prediction
    """
    def __init__(self,iData):
        """
        constructor
        """
        self.data = iData

    def useModel(self):
        """
        feed Model with data
        """
        model = joblib.load('IRIS_KNN.sav')
        predict = model.predict(self.data)
        return(predict)

    