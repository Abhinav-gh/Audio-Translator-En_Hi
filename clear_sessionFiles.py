# This program will clear the session files in the sessionFiles directory

import os

# Define the directory containing the session files
session_dir = "./sessionAudiofiles/"
print("\n\n Critical\n\n")
print("Clearing session files in the directory: ", session_dir, ". Please confirm the directory path", sep="")
print("Press 'y' to confirm or any other key to cancel")
confirmation = input()
if confirmation.lower() != 'y':
    print("Operation Cancelled")
    exit()
# List all files in the session directory
session_files = os.listdir(session_dir)
print("This will clear all the below listed files")
print(session_files)
if(session_files==[]):
    print("Session Files directory is already empty")
# Remove all files in the session directory
for file in session_files:
    try:
        print(f"Removing file: {file} from session directory ...")
        os.remove(os.path.join(session_dir, file))
    except:
        print(f"Error removing file: {file}")
print("Clear Operation Completed")
