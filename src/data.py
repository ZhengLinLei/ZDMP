#       
#   Apache License 2.0
#   Repository: https://github.com/ZhengLinLei/ZDMP
#
#   This file is used to visualizate the data saved in the datasets folder
#   The data is visualizated in the ./build folder
#

# ------------------------- #

# Import modules
import json, os, pickle, time
from libs.loadData import load_data
from libs.preparateData import prepare_data
from matplotlib import pyplot as plt


# Get execution time()
start_time = time.time()

# Load training configuration ./config.ini
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)) # ./src
CONFIG = json.load(open(os.path.join(CURRENT_PATH, 'config.ini'))) # ./config.ini
DATASET_PATH = os.path.join(CURRENT_PATH, CONFIG['dataset']['path']) # ./datasets/batch_data.csv

# Load the data
df = load_data(DATASET_PATH)

# Prepare the data
Y, X  = prepare_data(df)


plt.figure(figsize=(100,30))
# Visualizate the data
plt.scatter(x=range(0, len(Y)), y=Y, c="#7CAE00" ,alpha=0.3)
plt.ylabel('Reliability')
plt.xlabel('Product ID')

# Save the data in ./build folder
plt.savefig(os.path.join(CURRENT_PATH, CONFIG['build']['path'], CONFIG['build']['data']))



# Print execution time()
print("--- %s seconds ---" % (time.time() - start_time))


# ------------------------- #
# Output:

# --- 2.3485071659088135 seconds ---
# Image data in ./build/data.png