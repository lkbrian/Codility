def solution(data):
    items = sorted(data ,key=lambda data: data["name"])
    for item in items:
        result = item["hamburgers"] + item["chickenwings"] + item["hotdogs"]
        name = item["name"]
        print(f"name: {name}, score: {result}")


scoreboard = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11},
]

solution(scoreboard)
