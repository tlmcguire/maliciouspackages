# maliciouspackages

# Classification with Random Forest

## Summary

This repository contains a Python script that implements a machine learning workflow to classify data as either malicious or benign using a Random Forest classifier. The script reads a dataset from a CSV file, processes the data to maintain a specified ratio of malicious and benign samples, trains a Random Forest model, and evaluates its performance through various metrics. Additionally, it visualizes the model's performance using a Receiver Operating Characteristic (ROC) curve.

## Features

- Data preprocessing to handle malicious and benign samples.
- Random Forest classifier for model training.
- Evaluation metrics including accuracy, classification report, and confusion matrix.
- Visualization of model performance with ROC curve.

## Requirements

To run this script, you will need the following Python packages:

- pandas
- scikit-learn
- matplotlib

You can install the required packages using pip:

```bash
pip install pandas scikit-learn matplotlib
```

## Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   ```

2. **Prepare the Dataset**:
   Ensure you have a CSV file named `merged.csv` in the root directory of the repository. This file should contain the features and labels for the classification task.

3. **Modify the Script (if necessary)**:
   If you want to exclude specific columns from the dataset, modify the `columns_to_exclude` list in the script.

4. **Run the Script**:
   Execute the script using Python:
   ```bash
   python your_script_name.py
   ```

5. **View Results**:
   After running the script, you will see the model's accuracy, classification report, confusion matrix, and a plot of the ROC curve displayed in the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scikit-learn](https://scikit-learn.org/stable/) for machine learning functionalities.
- [Matplotlib](https://matplotlib.org/) for data visualization.
