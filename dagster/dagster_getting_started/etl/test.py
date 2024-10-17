from dotenv import load_dotenv
import os
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

# Lấy giá trị của các biến môi trường
database_url = os.getenv('DUCKDB_DATABASE')
print(database_url)