import json

users_database_file = 'users.json'
history_database_file = 'history.json'

def get_all_users():
    try:
        users_read_file = open(users_database_file, 'r', encoding='utf-8')
        users_data = json.load(users_read_file)
        users_read_file.close()
        return users_data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_all_users(all_users_list):
    users_write_file = open(users_database_file, 'w', encoding='utf-8')
    json.dump(all_users_list, users_write_file, indent=4, ensure_ascii=False)
    users_write_file.close()

def get_all_history():
    try:
        history_file_opened = open(history_database_file, 'r', encoding='utf-8')
        history_data_list = json.load(history_file_opened)
        history_file_opened.close()
        return history_data_list
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_history_record(history_data_list):
    history_file_write = open(history_database_file, 'w', encoding='utf-8')
    json.dump(history_data_list, history_file_write, indent=4, ensure_ascii=False)
    history_file_write.close()