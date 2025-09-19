import os
import shutil

def main():
    path = input("Enter the absolute path of the folder you want to organize: ")

    if not os.path.isdir(path):
        print(f"\n[ERROR] The path '{path}' is not a valid folder. Please try again.")
        return

    # This dictionary defines the sorting rules for file extensions.
    folder_map = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents', '.csv': 'Documents',
        '.mp3': 'Music', '.wav': 'Music',
        '.mp4': 'Videos', '.mov': 'Videos', '.avi': 'Videos',
        '.zip': 'Archives', '.rar': 'Archives'
    }

    summary = {}
    created_folders = set()

    for item_name in os.listdir(path):
        full_path = os.path.join(path, item_name)

        # Process only files, ignore any sub-folders.
        if os.path.isfile(full_path):
            extension = os.path.splitext(item_name)[1]
            dest_folder_name = folder_map.get(extension.lower(), 'Others')
            dest_folder_path = os.path.join(path, dest_folder_name)
            
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)
                created_folders.add(dest_folder_name)
            
            shutil.move(full_path, os.path.join(dest_folder_path, item_name))
            
            summary[dest_folder_name] = summary.get(dest_folder_name, 0) + 1

    print("\n----------------------------------------")
    print("      ORGANIZATION COMPLETE!      ")
    print("----------------------------------------")
    
    if created_folders:
        print(f"Folders created: {', '.join(sorted(list(created_folders)))}")
    
    for folder, count in summary.items():
        print(f"- Moved {count} file(s) to the '{folder}' folder.")


if __name__ == "__main__":
    main()