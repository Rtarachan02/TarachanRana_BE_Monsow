# JSON Data Handling and Processing (INTERMEDIATE TASK)

This project demonstrates how to handle and process JSON data using Python. It includes functionalities to read data from a JSON file, filter questions based on difficulty level and tags, and save the filtered questions to a new JSON file.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Set up a virtual environment and activate it:

    ```bash
    python -m venv env          # Create virtual environment
    .\env\Scripts\activate      # Activate virtual environment (on Windows)
    source env/bin/activate     # Activate virtual environment (on macOS/Linux)
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that your input JSON file (`input_questions.json`) is located in the `data/` directory. If not, provide your own JSON file with the same structure.

2. Run the `main.py` script to execute the application:

    ```bash
    python main.py
    ```

3. After execution, check the `data/` directory for the `filtered_questions.json` file. This file contains the filtered questions based on the specified criteria.

## Project Structure (INTERMEDIATE TASK)

```
project/
│
├── data/
│   ├── input_questions.json     # Input JSON file containing mock interview questions
│   └── filtered_questions.json  # Output JSON file with filtered questions
│
├── logs/
│   └── app.log                  # Log file containing application logs
│
└── src/
    ├── __init__.py
    ├── data_handler.py          # Module for reading JSON data
    ├── filter_questions.py      # Module for filtering questions
    ├── save_json.py             # Module for saving JSON data
    └── main.py                  # Main script orchestrating the processing of JSON data
```
## Dependencies
- Python (>= 3.6)
- Flask