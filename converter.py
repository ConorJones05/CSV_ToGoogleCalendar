import pandas as pd
import json

def build_file():
    df = pd.read_csv("classes.csv", header=None)
    df.columns = ['Task', 'Course', 'Date']

    def fix_date():
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%dT00:00:00.000Z')

    def fix_name():
        new_tasks = []
        for i in range(len(df['Task'])):
            task = f"{df['Course'][i]}: {df['Task'][i]}"
            new_tasks.append(task)
        df['Task'] = new_tasks

    fix_date()
    fix_name()

    def making_json():
        all_dicts = []
        for i in range(df.shape[0]):
            dict = {
                'title': f"{df['Task'][i]}",
                'due': f"{df['Date'][i]}"
            }
            all_dicts.append(dict)

        with open("tasks.json", "w") as json_file:
            json.dump(all_dicts, json_file, indent=4)


    making_json()