import json
from pymongo import MongoClient

# Load the courses from courses.json
with open('courses.json') as f:
    courses = json.load(f)

# Connect to the local instance of MongoDB
client = MongoClient()

# Create the appropriate databases and collections
db = client['courses_db']
courses_col = db['courses']

# Create the appropriate indices for efficient retrieval
courses_col.create_index([('title', 1)])
courses_col.create_index([('date', -1)])
courses_col.create_index([('domain', 1)])
courses_col.create_index([('rating', -1)])

# Add the course data to the collection
for course in courses:
    courses_col.insert_one(course)
