def make_readable(seconds):
    hours, minutes = 0, 0
    for unit in minutes, hour:
    if seconds >= 60:
        minutes = (seconds // 60)
        seconds = seconds - (minutes*60)
    if minutes >= 60:
        hours = (minutes // 60)
        minutes = minutes - (hours*60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
