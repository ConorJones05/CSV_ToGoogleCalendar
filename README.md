# Google Tasks Automation with Python

This project automates the process of creating and managing tasks in Google Tasks using data from a CSV file. The code handles the Google OAuth 2.0 flow, creates task lists, and populates them with tasks according to the data provided.

## Features

- Authenticates using Google OAuth 2.0.
- Automatically creates task lists and tasks in Google Tasks based on data from a CSV file.
- Handles existing task lists and prevents duplicates.
- Converts CSV data into a structured JSON format for task creation.

## Prerequisites

Before running the code, ensure you have the following:

1. **Python 3.6+** installed on your system.
2. Necessary Python packages installed:

   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
   ```

3. A Google Cloud project with the Google Tasks API enabled.
4. OAuth 2.0 credentials (downloaded as `credentials.json`) from your Google Cloud Console.

## Setup

1. Place your `credentials.json` file in the project directory.
2. Prepare your CSV file (e.g., `classes.csv`) with the following format:

   | Task       | Course | Date       |
   |------------|--------|------------|
   | Task Name  | Course Name | mm/dd/yyyy |

3. The project will automatically convert the CSV data into a structured JSON file (`tasks.json`) used to create tasks in Google Tasks.

## Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

   The script will:
   - Authenticate your Google account.
   - Create task lists based on course names.
   - Add tasks under the relevant lists according to the data in your CSV file.

## Code Explanation

- `get_google_tasks_service()`: Authenticates and returns the Google Tasks API service.
- `build_file()`: Converts the CSV data into a structured JSON format (`tasks.json`).
- `pick_list()`: Fetches existing task lists and creates new ones if needed.
- `making_tasks()`: Adds tasks to the appropriate task lists based on the JSON data.

## Customization

You can customize the CSV file structure and add more fields as needed. The code is flexible and can be extended to include additional task properties like notes, priority, etc.

## Important Notes

- The first time you run the script, it will open a browser window for Google account authentication.
- The script will store your OAuth tokens in a `token.json` file for future use.
- Ensure that the titles in the CSV file follow the correct format (`Course: Task Name`) for consistent task list creation.

## License

This project is licensed under the MIT License.

---

This README should help you get started with your Google Tasks automation project.