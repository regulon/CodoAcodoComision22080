from app import app
from utils.db import db




with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=500, debug=False)
