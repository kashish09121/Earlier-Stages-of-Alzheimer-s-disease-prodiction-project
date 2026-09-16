# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - Modernization Update

### Added
- **`train.py`**: A dedicated training script to programmatically load the dataset, scale features, train the `LinearSVC` and `LogisticRegression` models, and save them to a `models/` directory for robust reproducibility.
- **`.gitignore`**: Standard Python gitignore rules to prevent accidentally committing temporary files, caches, and virtual environments.
- **`models/` directory**: A dedicated folder to store serialized `.pkl` machine learning models.
- **Medical Disclaimer**: Added clear disclaimers to the UI and README indicating this is an educational prototype, not a medical diagnostic tool.
- **License**: Added the MIT License.
- **Ownership Attribution**: Added clear attribution for Kashish as the author and maintainer.

### Changed
- **Repository Restructuring**: Flattened the directory structure by removing the redundant nested folder.
- **UI Refresh**: Completely rewrote `templates/index.html` to utilize modern Bootstrap 5 styling, resulting in a cleaner, professional, responsive, and accessible interface.
- **`app.py` Refactor**: Updated the Flask backend to load models robustly using context managers, improved error handling on bad user input, and updated `.bin` references to the new `.pkl` format.
- **Dependencies (`requirements.txt`)**: Cleaned up the requirements file, removing unused libraries (e.g., `xgboost`, `matplotlib`) and pinning modern versions of `scikit-learn`, `Flask`, `numpy`, and `pandas`.
- **Documentation**: Completely rewrote `README.md` to accurately reflect the modern architecture, including clear instructions on environment setup, model training, and application execution.

### Removed
- **Unused CSS**: Deleted the `templates/css/` directory as it was entirely unused and filled with legacy libraries.
- **Opaque Models**: Removed old hardcoded `LinearSVM.bin`, `LogisticRegression.bin`, and `scaler.bin` files in favor of reproducible model generation.
