#       
#   Apache License 2.0
#   Repository: https://github.com/ZhengLinLei/ZDMP
#
#

# ------------------------- #

import pandas as pd
import pickle
import json
from datetime import datetime

def predict(json_data, s_model):
    # Computes predictions for new data

    # Parameters
    # ----------
    # json_data : str
    #     A JSON with data to predict.

    # s_model: str
    #     The path where the model is stored.
    
        
    # Returns
    # ----------
    #     A JSON with the following information:
    #         "id": data identifier (index) 
    #         "timestamp": time in which the prediction is done
    #         "payload": contains the following information:
    #             "name": name of the response variable
    #             "value": predicted value for the response variable
    #         "raw_data": the data used for the prediction
        
    # 
    
    # Load model
    with open(s_model, 'rb') as file:
        model = pickle.load(file)
    # Load data
    df = pd.DataFrame(json_data, index=[0])
    # We will assume that the first column is the index (timestamp, serial  number, ...)
    df.set_index(df.columns.values[0], inplace=True)
    
    
    # Preprocessing
    X_pred = model.scaler.transform(df[model.predictors])
    
    # Make predictions
    y_pred = model.predict(X_pred)
    
    # There should be just one observation at a time
    y_pred = float(y_pred[0]) # prediction should be passed as a float
    

    
    
    
    # export results as JSON
    data = {
        "id": str(df.index[0]),
        "timestamp": datetime.now().isoformat(timespec='milliseconds')+'Z',
        "payload": [
                    {
                        "name": model.response,
                        "value": y_pred
                    },
                ],
        "raw_data": json_data
    }

    json_results = json.dumps(data, indent=4)
    return json_results
