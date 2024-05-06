users = []


def solution(name, company):
    split_string = name.split()
    firstname_initial = split_string[0][0]
    split_string.pop(0)
    split_string.insert(0, firstname_initial)
    names = "".join(split_string).replace("-", "")
    users.append(names)

    count = 1
    for user in users:
        if user == names:
            count += 1
            email = f"{names}{count}@{company}.com"
            break
        else:
            email = f"{names}@{company}.com"

    return email


name = input("Enter your name: ")
company = input("Enter company name=> ")
email = solution(name, company)
print(email)
print(users)
