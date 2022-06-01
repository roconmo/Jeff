import os
import dotenv
dotenv.load_dotenv()

KEY = {
        'host':os.getenv('host'),
        'database':os.getenv('Cordis'),
        'user':os.getenv('user'),
        'password':os.getenv('password')
      }


