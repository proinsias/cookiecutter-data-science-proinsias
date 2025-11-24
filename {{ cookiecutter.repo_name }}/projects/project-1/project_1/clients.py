from ploomber.clients import LocalStorageClient, S3Client


def get_local():
    """Returns local client."""
    return LocalStorageClient('backup')


def get_s3():
    """Returns S3 client."""
    return S3Client(
        bucket_name='bucket',
        parent='folder1/folder2',
        # # Pass the json_credentials_path if env not configured with credentials.
        # json_credentials_path='credentials.json'
    )
