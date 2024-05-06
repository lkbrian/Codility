def solution(S, C):
    names = S.split(", ")
    emails = []
    for name in names:
        parts = name.split()
        first = parts[0][0].lower()
        middle = ""
        last = "".join(parts[1:]).replace("-", "").lower()[:8]
        if len(parts) > 2:
            middle = parts[1][0].lower()
        email = f"{first}{middle}{last}@{C.lower()}.com"
        count = 1
        while email in [e.split("@")[0] for e in emails]:
            email = f"{first}{middle}{last}{count}@{C.lower()}.com"
            count += 1
        emails.append(email)
    return ", ".join([f"{name} <{email}>" for name, email in zip(names, emails)])
