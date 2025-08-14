# DECISION TREE
## This is Project 2 for the Introductory Foundations of Artificial Intelligence course - a subject within the Faculty of Information Technology at the University of Science (HCMUS).

## Description about Project:

This repository contains the source code and datasets for a Decision Tree classification project, developed as part of the Introductory Foundations of Artificial Intelligence course at the University of Science (HCMUS). The project demonstrates the application of Decision Tree algorithms on multiple real-world datasets, including heart disease, rice classification, and penguin species identification.

Key features:
- Data preprocessing and visualization for each dataset.
- Implementation and evaluation of Decision Tree classifiers using scikit-learn.
- Performance metrics and visualizations for model assessment.
- Jupyter Notebooks for interactive exploration and reproducibility.

The project aims to provide a comprehensive, hands-on introduction to Decision Tree learning and its practical applications.

## Repository Overview

This course project showcases decision tree classification on three real‑world datasets. All code resides in Jupyter notebooks; there is no Python package or module structure.

### Repository Layout

```
DecisionTree/
├── README.md                – setup and run instructions
├── requirements.txt         – dependencies (matplotlib, scikit‑learn, seaborn, graphviz, ucimlrepo)
├── heart_disease_dataset/
│   ├── heart_disease.csv
│   ├── heart_disease.ipynb  – data prep, training, evaluation
│   └── output/              – confusion matrix, tree images, accuracy vs. depth plots
├── Rice_Dataset/
│   ├── Rice_Cammeo_Osmancik.csv
│   ├── rice_source.ipynb
│   └── output/
└── penguins_dataset/
    ├── penguins.csv
    ├── PalmerPenguins.ipynb
    ├── output/
    └── tree_depth_None      – exported Graphviz tree
```

### Important Concepts

- **Notebook‑centric workflow** – each dataset has its own `.ipynb` notebook combining data loading, preprocessing, model training and evaluation.
- **scikit‑learn `DecisionTreeClassifier`** – notebooks train decision trees (entropy or Gini criteria) with `train_test_split`, pipelines, and optional scaling.
- **Visualization** – Graphviz, Matplotlib, and Seaborn create tree diagrams, accuracy curves, and confusion matrices.
- **Outputs saved to disk** – model artifacts and charts are written to the `output/` subfolders for later inspection.

### Next Steps for a Newcomer

1. **Read the notebooks** – walk through each cell to understand data cleaning, feature engineering, model training, and evaluation.
2. **Experiment with parameters** – try different `max_depth`, `criterion`, or preprocessing options and observe their impact.
3. **Learn scikit‑learn tooling** – explore `Pipeline`, `ColumnTransformer`, and evaluation utilities such as `classification_report`.
4. **Extend the project** – add cross‑validation, hyper‑parameter tuning, reusable modules, or alternative tree algorithms like Random Forests.

## Team Members
1. Trần Xuân Minh Hiển - 22120102
2. Bùi Khánh Hưng - 22120119
3. Nguyễn Minh Hưng - 22120124
4. Hoàng Tiến Huy - 22120134

## Prerequisites
- Python 3 or higher
- pip (Python package manager)
- Graphviz
  
## How to run

### 1. **Clone the repository**  
   Open your terminal or command prompt and run:
   ```sh
   git clone https://github.com/simpleHuy/DecisionTree.git
   ```

### 2. **Navigate to the project directory**  
   ```sh
   cd DecisionTree
   ```

### 3. **Install the required dependencies**  
   Make sure you have Python 3 and pip installed. Then run:
   ```sh
   pip install -r requirements.txt
   ```

### 4. **Install Jupyter Notebook (if not already installed)**  
   If you do not have Jupyter installed, run:
   ```sh
   pip install notebook
   ```

### 5. **Execute each `.ipynb` file in the dataset subdirectories**  
#### a. Launch Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

#### b. In the Jupyter interface, open the corresponding `.ipynb` file (e.g., `heart_disease.ipynb`).

#### c. Run all cells in the notebook (from the menu: `Cell` > `Run All`).

### 6. **(Optional) To run notebooks with `Visual Studio Code` without opening `Jupyter Notebook`:**  
#### a. Install `Visual Studio Code` [here](https://code.visualstudio.com/download)
#### b. Install `Jupyter Notebook` extension in VSCode
#### c. Run Dataset with options in VSCode Jupyter interface

