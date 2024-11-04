import requests
import os
import tarfile
import time
import json
import ast

test_packages = ['ospyata']
print(test_packages)

def dl_packages(packages, target_directory):
    successful_downloads = 0
    failed_packages = []
    
    total_packages = len(packages)
    
    for index, package in enumerate(packages, start=1):
        package_dir = os.path.join(target_directory, package)
        os.makedirs(package_dir, exist_ok=True)
        retries = 3
        delay = 1
        success = False
        
        while retries > 0 and not success:
            try:
                r = requests.get(f"https://pypi.org/pypi/{package}/json")
                r.raise_for_status()
                d = r.json()
                for url in d["urls"]:
                    if url["packagetype"] == "sdist":
                        download_url = url["url"]
                        print(f"Downloading {package} from {download_url}")
                        response = requests.get(download_url)
                        response.raise_for_status()
                        file_name = os.path.basename(download_url)
                        with open(os.path.join(package_dir, file_name), 'wb') as file:
                            file.write(response.content)
                        print(f"Downloaded {package} into {package_dir}/{file_name}")
                        successful_downloads += 1
                        success = True
                        break
                if not success:
                    raise Exception("No sdist found in package metadata")
            except requests.exceptions.RequestException as req_e:
                print(f"Failed to download {package}: HTTP request error - {req_e}")
                retries -= 1
            except json.JSONDecodeError as json_e:
                print(f"Failed to download {package}: JSON decoding error - {json_e}")
                retries -= 1
            except Exception as e:
                print(f"Failed to download {package}: {e}")
                retries -= 1

            if retries > 0 and not success:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            elif retries == 0:
                print(f"Max retries reached for {package}. Skipping.")
                failed_packages.append(package)
        
        # Print progress
        print(f"Progress: {index}/{total_packages} packages processed")
    
    print(f"\nDownload complete. {successful_downloads} packages downloaded successfully.")
    if failed_packages:
        print(f"{len(failed_packages)} packages failed to download: {failed_packages}")

def parse_imports(directory):
    imports = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        # Collect imports
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                imports.extend(alias.name for alias in node.names)
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:  # Check if module is not None
                                    imports.append(node.module)
                    except SyntaxError as e:
                        print(f"Syntax error in {file_path}: {e}")
    
    return imports  # Return the list of all imports

download_directory = './packages/'
dl_packages(test_packages, download_directory)

# Find all tar.gz files in the repository
tar_files = []
for root, dirs, files in os.walk(download_directory):
    for file in files:
        if file.endswith(".tar.gz") or file.endswith(".tar.bz2") or file.endswith(".tar.xz"):
            tar_files.append(os.path.join(root, file))

# Unzip the files with different compression methods
for tar_file in tar_files:
    if tar_file.endswith(".tar.gz"):
        mode = 'r:gz'
    elif tar_file.endswith(".tar.bz2"):
        mode = 'r:bz2'
    elif tar_file.endswith(".tar.xz"):
        mode = 'r:xz'
    else:
        mode = 'r'
    
    try:
        with tarfile.open(tar_file, mode) as tar_ref:
            extract_dir = os.path.splitext(os.path.splitext(tar_file)[0])[0]
            tar_ref.extractall(extract_dir)
            print(f"Extracted {tar_file} to {extract_dir}")
            print(parse_imports(extract_dir))
        
        # Remove the tar file after extraction
        # os.remove(tar_file)
        # print(f"Deleted {tar_file}")
    except (tarfile.ReadError, tarfile.CompressionError) as e:
        print(f"Failed to extract {tar_file}: {e}")

print("Extraction process completed.")