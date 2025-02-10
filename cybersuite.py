import os
import ctypes

class CyberSuite:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def hide_folder(self):
        """Hide the specified folder."""
        try:
            if os.path.exists(self.folder_path):
                ctypes.windll.kernel32.SetFileAttributesW(self.folder_path, 2)
                print(f"Folder '{self.folder_path}' is now hidden.")
            else:
                print(f"Folder '{self.folder_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def unhide_folder(self):
        """Unhide the specified folder."""
        try:
            if os.path.exists(self.folder_path):
                ctypes.windll.kernel32.SetFileAttributesW(self.folder_path, 0)
                print(f"Folder '{self.folder_path}' is now visible.")
            else:
                print(f"Folder '{self.folder_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_to_hide = input("Enter the full path of the folder you want to hide/unhide: ")
    action = input("Enter 'hide' to hide the folder or 'unhide' to make it visible: ").strip().lower()

    cybersuite = CyberSuite(folder_to_hide)

    if action == 'hide':
        cybersuite.hide_folder()
    elif action == 'unhide':
        cybersuite.unhide_folder()
    else:
        print("Invalid action specified. Use 'hide' or 'unhide'.")