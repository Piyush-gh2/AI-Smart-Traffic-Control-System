def optimize_signal(vehicles):
    if vehicles > 100:
        return "Increase green time significantly"
    elif vehicles > 70:
        return "Increase green time"
    elif vehicles < 30:
        return "Reduce green time"
    else:
        return "Normal signal timing"