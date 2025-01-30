def log_message(sender, text):
    """Log received messages (can be extended for DB storage)"""
    print(f"Received from {sender}: {text}")
