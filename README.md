# SMA
Social Media Analyser

# Facebook Page Information Fetcher

This Python script fetches information about a Facebook Page using the Graph API and outputs the result to `output1.json`.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Python 3.x**: [Download and Install Python](https://www.python.org/downloads/)
- **pip** (Python package manager): It comes pre-installed with Python.
- **Facebook App**: You need to create a Facebook App to obtain the access token.

## Installation

1. Clone or download this repository.
2. Navigate to the project directory.

### Required Packages

Install the required Python packages:

```bash
pip install python-dotenv requests


Usage

Create .env file 
PAGE_ACCESS_TOKEN=your_page_access_token
PAGE_ID=your_page_id


# How to Run the Script
Make sure you've installed python-dotenv.
Fill in your actual access token and page ID in the .env file.
Run the script with Python:
bash
python facebook_page_info.py

# Troubleshooting
Missing Variables:
Ensure the .env file is in the same directory as the script or the project root.
Check that the variables are correctly named and spelled.
Dotenv Not Installed:
Ensure that python-dotenv is installed by running:
bash
pip show python-dotenv
