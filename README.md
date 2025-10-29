# Simple ML Project

This is a beginner-friendly Machine Learning project that demonstrates best practices in project organization and code structure.

## Project Structure

```
ML-Project/
├── data/               # Store datasets here
│   ├── raw/           # Original, immutable data
│   └── processed/     # Cleaned and processed data
├── notebooks/         # Jupyter notebooks for exploration and analysis
├── src/              # Source code for the project
│   ├── data/         # Scripts for data processing
│   ├── models/       # Model training and prediction code
│   └── utils/        # Utility functions and helpers
└── tests/            # Unit tests for the project
```

## Project Components

1. `data/`: Contains all data files
   - `raw/`: Store original, unmodified datasets
   - `processed/`: Store cleaned and transformed datasets

2. `notebooks/`: Contains Jupyter notebooks for:
   - Data exploration
   - Feature analysis
   - Model experimentation

3. `src/`: Main source code
   - `data/`: Scripts for data loading and processing
   - `models/`: Model-related code (training, evaluation)
   - `utils/`: Helper functions and utilities

4. `tests/`: Unit tests to ensure code reliability

## Setup and Installation

1. Create a virtual environment (already done):
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# On Linux/Mac
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
```

3. Install required packages (already done):
```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage

1. Place your dataset in the `data/raw/` directory
2. Use notebooks in `notebooks/` for exploration
3. Run the training script:
```bash
python src/train.py
```

4. Make predictions:
```bash
python src/predict.py
```