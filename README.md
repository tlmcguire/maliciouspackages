# Malicious Python Package Classification

### Summary

This repository contains Python scripts to preprocess data and train machine learning models to classify Python packages as malcious/benign. Included are scripts to process a dataset of Python packages, train classification models, and evaluate their performance using various metrics. 

Features

    Data preprocessing to handle malicious and benign Python packages.
    Classification model training (using Random Forest).
    Evaluation metrics including accuracy, classification report, and confusion matrix.
    Visualization of model performance with ROC curve.

### Requirements

To run these scripts, you will need the following Python packages:

    pandas
    scikit-learn
    matplotlib

Additionally, the Backstabber's Knife Collection (https://dasfreak.github.io/Backstabbers-Knife-Collection/) is required.

### Instructions

Prepare the Dataset:
Ensure you have the CSV file named merged.csv in the root directory of the repository. This file should contain the features and labels extracted from the malicious and benign packages.

Setup test:
Run each cell in rfTest.ipynb.
If you want to exclude specific columns from the dataset, modify the columns_to_exclude list in the script.

Run the Script

### Acknowledgments
- **Backstabbers' Knife Collection**: [https://dasfreak.github.io/Backstabbers-Knife-Collection/] for providing labeled malicious Python packages.
- **Scikit-learn**: For machine learning functionalities that support model training and evaluation.
- **pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **SciPy**: For scientific computing capabilities.
- **lxml**: For efficient XML and HTML processing.
- **NumPy**: For numerical computing and array manipulation.