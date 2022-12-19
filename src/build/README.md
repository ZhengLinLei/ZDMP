Here is located the `model.pkl` to predict the future data.

To execute the script, run the following command:
```bash
python3 src/predict.py
```

To get the model in python, run this code:
```python
import pickle
with open('src/build/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Predict
Y = model.predict(...)
```
