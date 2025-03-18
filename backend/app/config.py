from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATION = os.getenv('SQLALCHEMY_TRACK_MODIFICATION')
    UPLOAD_FOLDER = f"{os.getcwd()}/{os.getenv('UPLOAD_FOLDER')}"
