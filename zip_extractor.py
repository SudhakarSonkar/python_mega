import zipfile

def extract_archive(archive_path, dest_dir):
    """
    Extracts the contents of a zip archive to the specified destination directory.
    
    :param archive_path: Path to the zip archive file.
    :param dest_dir: Directory where the contents should be extracted.
    """
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
        print(f"Extraction complete: {archive_path} to {dest_dir}")
    except zipfile.BadZipFile:
        print(f"Error: The file {archive_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python zip_extractor.py <archive_path> <dest_dir>")
    else:
        archive_path = sys.argv[1]
        dest_dir = sys.argv[2]
        extract_archive(archive_path, dest_dir)