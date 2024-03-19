def solution(items):
    data = []
    for item in items:
        result = (
            (item["hamburgers"] * 3)
            + (item["chickenwings"] * 5)
            + (item["hotdogs"] * 2)
        )
        name = item["name"]
        output ={"name": name, "score": result}
        data.append(output)
    scoreboard_result = sorted(data,key=lambda data: data["score"],reverse=True)
    # print(scoreboard_result)
    #print the results line by line
    for score in scoreboard_result:
        print(score)

scoreboard = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Allen shams", "chickenwings": 12, "hamburgers": 6, "hotdogs": 22},
    {"name": "Anne Shiko", "chickenwings": 9, "hamburgers": 20, "hotdogs": 1},
    {"name": "Brian Kip", "chickenwings": 8, "hamburgers": 14, "hotdogs": 5},
    {"name": "Mariam Senzia", "chickenwings": 3, "hamburgers": 7, "hotdogs": 8},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 3},
]

solution(scoreboard)
