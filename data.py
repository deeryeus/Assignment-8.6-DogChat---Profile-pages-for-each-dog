# first datetime is the module, second datetime is the class
from datetime import datetime

comment1 = {
    "UserID": 2,
    "Text": "What time are you going?",
    "Name": "Inu",
    "Username": "Shiba",
    "DateTime": datetime(2021, 7, 1, 18, 0, 0),
    "Picture": "inu.jpg"
}

comment2 = {
    "UserID": 1,
    "Text": "I'm going to go at 7 tonight!",
    "Name": "Collie",
    "Username": "collie",
    "DateTime": datetime(2021, 7, 1, 19, 0, 0),
    "Picture": "collie.jpg"
}

comment3 = {
    "UserID": 1,
    "Text": "I love me a good nap!",
    "Name": "Collie",
    "Username": "collie",
    "DateTime": datetime(2021, 6, 29, 10, 0, 0),
    "Picture": "collie.jpg"
}

post1 = {
    "UserID": 1,
    "PostId": 1,
    "Text": "I can't wait to go to the park today",
    "Name": "Collie",
    "Username": "collie",
    "Likes": ["Inu"],
    "Comments": [comment1, comment2],
    # biggest unit to smallest, make sure to import datetime
    "DateTime": datetime(2021, 7, 1, 17, 0, 0),
    "Picture": "collie.jpg"
}

post2 = {
    "UserID": 1,
    "PostId": 2,
    "Text": "I could really use a treat right now",
    "Name": "Collie",
    "Username": "collie",
    "Likes": [],
    "Comments": [],
    # biggest unit to smallest, make sure to import datetime
    "DateTime": datetime(2021, 6, 30, 12, 30, 0),
    "Picture": "collie.jpg"
}

post3 = {
    "UserID": 2,
    "PostId": 3,
    "Text": "Aren't naps the best?",
    "Name": "Inu",
    "Username": "shiba",
    "Likes": ["Collie"],
    "Comments": [comment3],
    # biggest unit to smallest, make sure to import datetime
    "DateTime": datetime(2021, 6, 29, 9, 0, 0),
    "Picture": "inu.jpg"
}

#postID : post
test_posts = {
    1 : post1,
    2 : post2,
    3 : post3
}

# returns the date in Month/DD/YYYY format (e.g. March 16, 2022) 
def birthday(y, m, d):

    date = datetime(y, m, d)

    month = date.strftime("%B") # full name of the month (January, February, etc.)
    day = date.strftime("%d") # day as DD
    year = date.strftime("%Y") # full year as YYYY

    full_date = f"{month} {day}, {year}"

    return full_date

user1 = {
    "Name": "Collie",
    "Username": "collie",
    "Intro": "My name is Collie and I'm a border collie. I love treats and walks!",
    "Friends": "Inu",
    "Birthday": birthday(2012, 3, 16),
    "Picture": "collie.jpg"
}

user2 = {
    "Name": "Inu",
    "Username": "shiba",
    "Intro": "I'm Inu the shiba inu. I love naps!",
    "Friends": "Collie",
    "Birthday": birthday(2014, 12, 5),
    "Picture": "inu.jpg"
}

# profile ID : user profile
users = {
    1 : user1,
    2 : user2
}