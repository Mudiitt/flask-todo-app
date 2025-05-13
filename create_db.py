from app import app, db

with app.app_context():
    try:
        db.create_all()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    

