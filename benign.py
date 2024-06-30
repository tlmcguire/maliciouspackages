import requests
import subprocess
import sys
import os
import tarfile
import time
import json

def get_top_pypi_packages(url='https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'):
    response = requests.get(url)
    response.raise_for_status() 
    
    data = response.json()
    packages = [package['project'] for package in data['rows'][:1000]]

    return packages

top_packages = get_top_pypi_packages()
print(top_packages)

def dl_packages(packages, target_directory):
    count = 0
    for package in packages:
        package_dir = os.path.join(target_directory, package)
        os.makedirs(package_dir, exist_ok=True)
        retries = 2
        delay = 1
        while retries > 0:
            try:
                r = requests.get(f"https://pypi.org/pypi/{package}/json").content
                d = json.loads(r)
                for url in d["urls"]:
                    if url["packagetype"] == "sdist":
                        download_url = url["url"]
                        print(f"Downloading {package} from {download_url}")
                        response = requests.get(download_url)
                        file_name = os.path.basename(download_url)
                        with open(os.path.join(package_dir, file_name), 'wb') as file:
                            file.write(response.content)
                        print(f"Downloaded {package} into {package_dir}/{file_name}")
                        count += 1
                        print(f"Progress: {count}/{len(packages)}")
                        break

                break  # Break out of the retry loop if download is successful
            except Exception as e:
                print(f"Failed to download {package}: {e}")
                retries -= 1
                if retries == 0:
                    print(f"Max retries reached for {package}. Skipping.")
                else:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                    continue

download_directory = '/mnt/volume_nyc1_01/benignPyPI/'

dl_packages(top_packages, download_directory)

repo_dir = "/mnt/volume_nyc1_01/benignPyPI/"
#Find all tar.gz files in the repository
tar_files = []
for root, dirs, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(".tar.gz") or file.endswith(".tar.bz2") or file.endswith(".tar.xz"):
            tar_files.append(os.path.join(root, file))

#Unzip the files with different compression methods
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
    except (tarfile.ReadError, tarfile.CompressionError) as e:
        print(f"Failed to extract {tar_file}: {e}")

print("Extraction process completed.")