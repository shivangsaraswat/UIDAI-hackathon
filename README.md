# Aadhaar Demographic Data Analysis

## UIDAI Hackathon Project

This project focuses on the programmatic extraction, cleaning, and visualization of anonymized Aadhaar demographic update data.

### Project Overview
- **Automated Pipeline:** Uses Python and Jupyter Notebooks to process ~2 million records.
- **Data Engineering:** Programmatic extraction of zip archives and merging of multiple CSV partitions.
- **Visual Analytics:** Generates high-resolution insights into demographic trends across age groups and time.

### How to Run
1. Ensure you have the `aadhaar-hackathon.zip` file in the root directory.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn notebook
   ```
3. Open the notebook:
   ```bash
   jupyter notebook aadhaar_analysis.ipynb
   ```

### Project Structure
- `aadhaar_analysis.ipynb`: The main analysis notebook.
- `generate_notebook.py`: Source generation script for the notebook structure.
- `data/`: Extracted CSV data (ignored by git).
