import csv
from app import create_app, db
from models import Episode, Guest  # Import your models here

app = create_app()

def seed_database():
    with open('data/seed.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            episode = Episode(year=row['Year'], number=row['number'])
            db.session.add(episode)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        seed_database()  # Call the seed function

