import requests
import os
import zipfile
 
def create_dataset_folder() -> None:
    """Creates the folder to store the World Development Indicators Dataset."""

    parent_dir = r"C:\Users\pc\Documents\Python\W.D.I.-Analysis\Complementary datasets"
    global dataset_path
    dataset_path = os.path.join(parent_dir, "W.D.I. Dataset")

    if os.path.isdir(dataset_path) == True:
        pass
    else:
        os.mkdir(dataset_path)
        

def download_files_archive() -> None:
    """Downloads the dataset from the specified URL."""

    url = "https://storage.googleapis.com/kaggle-data-sets/2377794/4661528/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230808%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230808T070920Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=79fc18207f2aacb18b49a24a537e1d9d84bcc24af67e38c79b3f789e7018053628958c19a632e17468a1a54c6b40eeb9280a026410b9521db94f407cc8150a008ca2a9fa86ac424eda234d5944d94b35d67d806f3bfb759ab6570fd042021712c4ce96f8ea1a062948199137e4fa3fbf6973c6f620245e0d66ec3cc73aaa584db5cde2c435f560656164d67efc3ebffb296c5b5f21ae7744f395a5946b75dcaf4a340195a7ce05dc8d69c106bea3ead811b98e2882704ecdf3cd1db3908b23e4c2f8f10b02e90745d716080c73b275ec0e5f6b640fa85cb124796a2be41b04404dfcb38833f2ad115550e8fb1d8b2c6fb8d20660d99cfc1b53e398a994ab1b2a"
    response = requests.get(url, stream= True) # Download in several smaller parts

    with open(os.path.join(dataset_path, "W.D.I. Archive.zip") , "wb") as file:
        for chunk in response.iter_content(chunk_size= 10 * 1024 * 1024): # To avoid RAM issues
            file.write(chunk)

def unzip_archives()-> None:
    """Unzips archives."""
    dataset_path = r"C:\Users\pc\Documents\Python\W.D.I.-Analysis\Complementary datasets"
    file_name = "archive.zip"
    with zipfile.ZipFile(os.path.join(dataset_path, file_name), 'r') as zip_ref:
        zip_ref.extractall(dataset_path)

def main():
    create_dataset_folder()
    download_files_archive()
    unzip_archives()

if __name__ == "__main__":
    main()