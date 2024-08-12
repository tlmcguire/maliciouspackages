# Malicious Python Package Classification

### Summary

This repository contains Python scripts to preprocess data and train machine learning models to classify Python packages as malicious or benign. Included are scripts to process a dataset of Python packages, train classification models, and evaluate their performance using various metrics.

### Requirements

To run these scripts, you will need the following Python packages:

- `scipy`
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `lxml`

Additionally, the Backstabber's Knife Collection is required. You can find it [here](https://dasfreak.github.io/Backstabbers-Knife-Collection/).

### Instructions

1. **Prepare the Dataset**:  
   Ensure you have the CSV file named `merged.csv` in the root directory of the repository. This file should contain the features and labels extracted from the malicious and benign packages.

2. **Setup Test**:  
   If you want to exclude specific columns from the dataset, modify the `columns_to_exclude` list in the script. The test split and the ratio of malicious packages in the test set are also adjustable.

3. **Run the Notebook**:  
   Run each cell in `rfTest.ipynb`.

### Acknowledgments

- **Backstabbers' Knife Collection**: [https://dasfreak.github.io/Backstabbers-Knife-Collection/] for providing labeled malicious Python packages.
- **Scikit-learn**: For machine learning functionalities that support model training and evaluation.
- **pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **SciPy**: For scientific computing capabilities.
- **lxml**: For XML processing.
- **NumPy**: For numerical computing and array manipulation.