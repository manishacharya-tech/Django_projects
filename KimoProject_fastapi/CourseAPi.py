from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to the local instance of MongoDB
client = MongoClient()
db = client['courses_db']
courses_col = db['courses']

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

@app.get('/courses')
async def get_courses(sort: str = 'alphabetical', domain: str = None):
    # Set up the sort order
    sort_order = [('name', 1)]
    if sort == 'date':
        sort_order = [('date', -1)]
    elif sort == 'rating':
        sort_order = [('rating', -1)]

    # Set up the filter for the domain
    filter = {}
    if domain:
        filter = {'domain': domain}
    # Retrieve the courses
    courses = courses_col.find(filter).sort(sort_order)
    return list(courses)



@app.get('/courses/{course_name}')
async def get_course(course_name: str):
    # Retrieve the course with the specified course name
    course = courses_col.find_one({'name': course_name})
    if not course:
        return ErrorResponseModel(
            "An error occurred", 404, "{0} doesn't exist".format(course_name)
        )
    return course


@app.get('/courses/{course_name}/chapters')
async def get_chapters(course_name: str):
    # Retrieve the chapters for the course with the course name
    course = courses_col.find_one({'name': course_name})
    chapters = course.get('chapters', [])
    if not chapters:
        return ErrorResponseModel(
            "An error occurred", 404, "{0} doesn't exist".format(course_name)
        )
    return chapters


@app.post('/courses/{course_name}/chapters/rate')
async def rate_chapter(course_name: int,  rating: int):
    # Update the rating for the specified chapter in the specified course
    courses_col.update_one({'name': course_name}, {'$set': {'chapters.$.rating': rating}})
    # Recalculate the overall rating for the course
    course = courses_col.find_one({'name': course_name})
    chapters = course.get('chapters', [])
    ratings = [chapter.get('rating', 0) for chapter in chapters]
    overall_rating = sum(ratings) / len(ratings)
    update_rating = courses_col.update_one({'name': course_name}, {'$set': {'rating': overall_rating}})
    if update_rating:
        return ResponseModel(
            "Rating added",
            "Rating updated successfully",
        )

