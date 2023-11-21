from huggingface_hub import HfFileSystem, login, HfApi
import pandas as pd
from io import StringIO
import os


"""
READ THIS
https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions
https://huggingface.co/docs/huggingface_hub/v0.18.0.rc0/guides/hf_file_system

"""


class Pipeline:
    def __init__(self, token=None, revision="main"):
        try:
            self.token = os.getenv("HF_TOKEN")
            self.fs = HfFileSystem(token=token)
            self.api = HfApi(token=token)

        except:
            self.token = None

        self.root = (
            f"PromptSystematicReview/Prompt_Systematic_Review_Dataset@{revision}/"
        )
        self.repo_name = f"PromptSystematicReview/Prompt_Systematic_Review_Dataset"
        self.revision = revision

    def is_logged_in(self):
        print(self.token)
        return self.token is not None

    def get_revision(self):
        return self.revision

    def set_revision(self, revision):
        try:
            assert revision.isalnum()
            self.revision = revision
            self.root = f"hf://datasets/PromptSystematicReview/Prompt_Systematic_Review_Dataset@{revision}/"
        except:
            raise ValueError("Revision must be alphanumeric")

    def login(self, token):
        if self.token is not None:
            raise ValueError("Already Logged In")
        else:
            self.fs = HfFileSystem(token=self.token)
            login(token=token)
            self.token = token

    def get_all_files(self):
        return self.fs.ls(self.root, detail=False, revision=self.revision)

    def get_all_data_files(self):
        return self.fs.glob(self.root + "**.csv", revision=self.revision)

    def read_from_file(self, fileName):
        return pd.read_csv(os.path.join(self.root, fileName))

    def write_to_file(self, fileName, dataFrame):
        if not self.is_logged_in():
            raise ValueError("Not Logged In")
        path = os.path.join(self.root, fileName)
        dataFrame.to_csv(path, index=False)

    def upload_file(self, fileName):
        if not self.is_logged_in():
            raise ValueError("Not Logged In")
        path = os.path.join(self.repo_name, fileName)
        self.api.upload_file(
            repo_id=self.repo_name,
            path_in_repo=fileName,
            path_or_fileobj=fileName,
            commit_message=f"Add {fileName}",
            repo_type="dataset",
        )

    def upload_folder(self, folderName):
        if not self.is_logged_in():
            raise ValueError("Not Logged In")
        path = os.path.join(self.repo_name, folderName)
        self.api.upload_folder(
            repo_id=self.repo_name,
            folder_path=folderName,
            commit_message=f"Add {folderName}",
            repo_type="dataset",
        )

    def delete_file(self, fileName):
        if not self.is_logged_in():
            raise ValueError("Not Logged In")
        path = os.path.join(self.repo_name, fileName)
        self.api.delete_file(
            fileName,
            self.repo_name,
            token=self.token,
            commit_message=f"Delete {fileName}",
            repo_type="dataset",
        )

    def delete_folder(self, folderName):
        if not self.is_logged_in():
            raise ValueError("Not Logged In")
        self.api.delete_folder(
            folderName,
            self.repo_name,
            token=self.token,
            commit_message=f"Delete {folderName}",
            repo_type="dataset",
        )
