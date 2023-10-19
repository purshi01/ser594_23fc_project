# Introduction

This repository contains files for the individual course project in SER594 : Data Science for Software Engineers (2023) created by Purushothama Shanthappa for partial fulfillment of the course requirements.

At this time, this project has not been cleared by the course staff (R. Acuna) for public release, and must be kept within a private repository.

Welcome to the SER594_23FC_PROJECT-1 repository! This project focuses on analyzing and exploring housing market data, taking into account various macroeconomic and property-specific factors.

## Repository Structure

- **data_original**: Contains the original data files used in the project.

  - `data_original.csv`: Primary dataset of housing market information.
  - `inflation_rates.csv`: Dataset containing inflation rates over time.
  - `mortgage_interest.csv`: Data on mortgage interest rates.

- **data_processed**: Folder for processed and cleaned data.

  - `correlations.txt`: Text file with correlation values between different features.
  - `data_description.txt`: Descriptions of the columns and data features.
  - `out.csv`: Processed and transformed dataset ready for analysis.
  - `summary.txt`: Summary statistics of the data.

- **visuals**: Contains visual representations and plots generated from the data.

- **project_exploration.md**: Detailed exploration and analysis of the project.

- **project_proposal_initial.md**: Initial project proposal and scope.

- **requirements.txt**: List of Python packages required to run the project.

- **wf_core.py**: Core script with primary functions and logic.

- **wf_datagen.py**: Script to generate additional data or simulate data.

- **wf_dataprocessing.py**: Data processing and cleaning script.

- **wf_visualization.py**: Script for generating data visualizations.

## How to Execute the Project

1. **Setup & Installation**:

   ```bash
   git clone [https://github.com/purshi01/ser594_23fc_project.git]
   cd SER594_23FC_PROJECT-1
   pip3 install -r requirements.txt
   ```

2. **Data Processing && Data Visualization**:
   Run the data processing script to clean and transform the raw data.

   ```bash
    python3 wf_core.py
   ```

3. **Analysis & Results**:
   Dive deep into the project's analysis by exploring `project_exploration.md`.

## Additional Resources

- Explore `project_proposal_initial.md` for the initial project ideas and scope.
- Refer to `data_description.txt` in the `data_processed` directory for a deeper understanding of the dataset columns and features.
