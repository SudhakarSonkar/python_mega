import zipfile
import pathlib
import os

def make_archive(filepaths, dest_dir):
    """
    Creates a zip archive named 'compressed.zip' in the specified destination directory,
    containing the provided file paths (relative to this script's location).
    """
    # Path to the current script
    base_path = pathlib.Path(__file__).parent

    # Ensure destination directory exists
    dest_path = base_path / dest_dir
    dest_path.mkdir(parents=True, exist_ok=True)

    # Create zip archive path
    archive_path = dest_path / "compressed.zip"

    with zipfile.ZipFile(archive_path, 'w') as archive:
        for filepath in filepaths:
            full_path = base_path / filepath  # ensure full path
            archive.write(full_path, arcname=filepath)  # arcname ensures clean names inside zip

if __name__ == "__main__":
    try:
        make_archive(
            filepaths=['functions.py', 'gui.py', 'compress.py'],
            dest_dir='dest'
        )
        print("Zip archive created successfully.")
    except Exception as e:
        print(f"Error: {e}")
