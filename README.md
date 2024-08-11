# Malicious Python Package Classification

### Summary

This repository contains a Python script that implements a machine learning workflow to classify Python packages as either malicious or benign. The script processes a dataset of Python packages, trains a classification model, and evaluates its performance using various metrics. Additionally, it visualizes the model's performance through a Receiver Operating Characteristic (ROC) curve.
Features

    Data preprocessing to handle malicious and benign Python packages.
    Classification model training (using Random Forest or other algorithms).
    Evaluation metrics including accuracy, classification report, and confusion matrix.
    Visualization of model performance with ROC curve.

### Requirements

To run this script, you will need the following Python packages:

    pandas
    scikit-learn
    matplotlib

You can install the required packages using pip:

bash

pip install pandas scikit-learn matplotlib

### Instructions

    Clone the Repository:
    Clone this repository to your local machine using the following command:

bash

git clone https://github.com/yourusername/repository-name.git

Prepare the Dataset:
Ensure you have a CSV file named merged.csv in the root directory of the repository. This file should contain the features and labels for the classification task.

Modify the Script (if necessary):
If you want to exclude specific columns from the dataset, modify the columns_to_exclude list in the script.

Run the Script:
Execute the script using Python:

bash

    python your_script_name.py

    View Results:
    After running the script, you will see the model's accuracy, classification report, confusion matrix, and a plot of the ROC curve displayed in the console.

### Acknowledgments

    Scikit-learn for machine learning functionalities.
    pandas for data manipulation and analysis.
    Matplotlib for data visualization.
