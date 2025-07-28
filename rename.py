import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if not (filename.endswith('.xls') or filename.endswith('.xlsx')):
            continue

        _, ext = os.path.splitext(filename)
        year = filename[-9:-5]
        new_name = f"{year}{ext}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)    

        if filename != new_name:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)
