import os
import shutil

# Define a function to organize files from one directory to another
def organize_files(source_dir, target_dir):
    # Check if the target directory exists, if not, create it
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the current item is a file
        if os.path.isfile(os.path.join(source_dir, filename)):
            # Extract the file extension and convert it to uppercase
            file_extension = filename.split(".")[-1].upper()

            # Proceed if file_extension is not empty
            if file_extension:
                # Determine the target folder path for this file type
                target_folder = os.path.join(target_dir, file_extension)
                # Create the target folder if it doesn't exist
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)

                # Build the full source and target paths for the file
                source_path = os.path.join(source_dir, filename)
                target_path = os.path.join(target_folder, filename)

                # Move the file from the source to the target path
                shutil.move(source_path, target_path)
                # Print a message indicating the file has been moved
                print(f"Moved {filename} to {target_folder}")

# Entry point of the script
if __name__ == "__main__":
    # Specify the source and target directories
    source_directory = r"C:\Users\Dev\Desktop\Projects\File Organizer\Random"
    target_directory = r"C:\Users\Dev\Desktop\Projects\File Organizer\Organized"

    # Call the function to start organizing files
    organize_files(source_directory, target_directory)
