from app.database.database import Base, engine

# Import ALL models so SQLAlchemy knows about them
from app.database.models import Investigation
from app.database.alert_models import Alert

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")