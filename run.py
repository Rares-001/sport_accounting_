from app import create_app, db
from config import DevelopmentConfig

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app(config_object=DevelopmentConfig)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()

