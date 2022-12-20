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

    # Get json string and parse it to predict in K-NN model
    json_data = json.loads(json_data)
    X_pred = pd.DataFrame(json_data, index=[0])
    Y_pred = model.predict(X_pred).tolist()

    RELIABILITY = Y_pred[0]
        
    # export results as JSON
    data = {
        "id": str(X_pred.index[0]),
        "timestamp": datetime.now().isoformat(timespec='milliseconds')+'Z',
        "payload": [
            {
                "name": "reliability",
                "value": RELIABILITY,
                "max": 0.9,
                "min": 0.7
            },
        ],
        "results": {
            "anomaly": 1 if RELIABILITY < 0.7 else 0,
            "label": "Anomaly" if RELIABILITY < 0.7 else ("Normal" if RELIABILITY < 0.9 else "Quality")
        },
        "raw_data": json_data
    }

    json_results = json.dumps(data, indent=4)
    return json_results
