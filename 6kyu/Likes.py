def likes(names):
    likes = len(names)
    print(likes)
    
    if likes == 0:
        return f"no one likes this"
    elif likes == 1:
        return f"{names[0]} likes this"
    elif likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif likes >= 4:
        return f"{names[0]}, {names[1]} and {likes - 2} others like this"
