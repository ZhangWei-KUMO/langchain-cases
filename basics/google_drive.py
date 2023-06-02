from langchain.document_loaders import GoogleDriveLoader
loader = GoogleDriveLoader(document_id='',credentials_path='credentials.json')
loader.load()