from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import json
from converter import build_file

# Define the scope for accessing Google Tasks
SCOPES = ['https://www.googleapis.com/auth/tasks']

# Path to your OAuth 2.0 credentials.json file (downloaded from Google Cloud Console)
CREDENTIALS_FILE = 'path/to/your/credentials.json'

# Token file to store access and refresh tokens
TOKEN_FILE = 'token.json'

# Function to get the Google Tasks service
def get_google_tasks_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('tasks', 'v1', credentials=creds)
    return service

service = get_google_tasks_service()

# Load the JSON data containing tasks


build_file()
with open('tasks.json') as f:
    data = json.load(f)

# Function to create task lists and populate task_ids
task_ids = {}

def pick_list():
    tasklists = service.tasklists().list(maxResults=100).execute()
    
    # Fetch existing task lists and store them in task_ids
    for tasklist in tasklists.get('items', []):
        task_ids[tasklist['title'].split(':')[0]] = tasklist['id']

    # Create new task lists if they don’t already exist
    for course in data:
        course_title = course['title'].split(':')[0]
        if course_title not in task_ids:
            new_tasklist = service.tasklists().insert(body={"title": course_title}).execute()
            task_ids[course_title] = new_tasklist['id']

pick_list()

# Function to add tasks to the created task lists
def making_tasks():
    for task in data:
        course_title = task['title'].split(':')[0]
        if course_title in task_ids:
            tasklist_id = task_ids[course_title]
            task_result = service.tasks().insert(tasklist=tasklist_id, body={
                'title': task['title'],
                'notes': task.get('notes', ''),
                'due': task.get('due', '')
            }).execute()
            print(f"Task created: {task_result.get('title')}")

making_tasks()
