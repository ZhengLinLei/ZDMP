If you don't find any `model.pkl` file, run the following command before using the `predict.py` script:
```bash
python3 src/train.py
```

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
