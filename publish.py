import neocities
import glob
import os
from dotenv import load_dotenv
import hashlib

def path_normalize(fname):
    normPath = filename.replace("\\","/")
    splitPath = normPath.split("/")
    splitPath.pop(0)
    newPath = "/".join(splitPath)

    return newPath

def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

def should_upload(fname, files):
    for file in files:
        if file['is_directory']:
            continue

        normal_path = path_normalize(fname)

        if normal_path == file['path']:
            file_sum = sha1(fname)
            if file_sum == file['sha1_hash']:
                return False
            else:
                return True
    return True;

load_dotenv()

root_dir = "build"
file_tuples = []

nc = neocities.NeoCities(os.getenv('NC_USER'), os.getenv('NC_PASS'))
response = nc.listitems()
files_onsite = response['files']

for filename in glob.iglob(root_dir + '/**/**.*', recursive=True):
    s_u = should_upload(filename, files_onsite)
    
    if s_u:
        print("Will upload " + filename)
        newPath = path_normalize(filename)
        file_tuples.append((filename, os.getenv('TARGET') + "/" + newPath))

if len(file_tuples) > 0:
    print("Uploading...")
    nc.upload(*file_tuples)
else:
    print("Nothing to upload")