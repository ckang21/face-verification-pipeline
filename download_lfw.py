import os
import urllib.request
import tarfile

def download_lfw_dataset(dest_path='data/images'):
    url = "http://vis-www.cs.umass.edu/lfw/lfw-deepfunneled.tgz"
    tar_path = "lfw.tgz"

    if os.path.exists(dest_path) and len(os.listdir(dest_path)) > 0:
        print("LFW already downloaded.")
        return

    print("Downloading LFW dataset...")
    urllib.request.urlretrieve(url, tar_path)

    print("Extracting...")
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path="data/")
    
    # Move all images to `data/images/`
    os.rename("data/lfw-deepfunneled", dest_path)
    os.remove(tar_path)
    print("Done.")

if __name__ == "__main__":
    download_lfw_dataset()
