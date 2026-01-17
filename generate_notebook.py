import json

# Define the structure of the Jupyter Notebook as a dictionary (JSON)
notebook_structure = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Aadhaar Demographic Data Analysis\n",
                "## UIDAI Hackathon - Source Generation Script\n",
                "---"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["### Step 1: Import Libraries"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import zipfile\n",
                "import os\n",
                "\n",
                "plt.style.use('seaborn-v0_8-whitegrid')\n",
                "sns.set_palette('husl')\n",
                "\n",
                "print('✅ Libraries imported successfully!')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["### Step 2: Extract the Dataset"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "zip_path = \"aadhaar-hackathon.zip\"\n",
                "extract_path = \"data\"\n",
                "\n",
                "with zipfile.ZipFile(zip_path, 'r') as zip_ref:\n",
                "    zip_ref.extractall(extract_path)\n",
                "\n",
                "print(f'✅ Dataset extracted to: {extract_path}')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["### Step 3: Load Data"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "files = []\n",
                "for root, dirs, filenames in os.walk(\"data\"):\n",
                "    for f in filenames:\n",
                "        if f.endswith(\".csv\"): files.append(os.path.join(root, f))\n",
                "\n",
                "df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)\n",
                "print(f'✅ Loaded {len(df)} rows')"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the dictionary to a physical .ipynb file
filename = "reconstructed_notebook.ipynb"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(notebook_structure, f, indent=1)

print(f"Successfully generated {filename} from programmatic building blocks.")
