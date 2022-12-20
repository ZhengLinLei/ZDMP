# Build Folder

## Index

- [Data.png](#data)
- [Model.pkl](#model)

## Data.png
If you don't find any `data.png` file, run the following command before using the `data.py` script:
```bash
python3 src/data.py
```

Here is located the `data.png` to visualize the data.

What we can see on the graph:
- The points are the every product with their realibility
- In most of the cases the realibility is between 0.5 and 0.9


## Model.pkl
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
