import datetime

if __name__ == "__main__":
    with open("log.txt", "w") as f:
        now = datetime.datetime.now()
        f.write(f"Updated {str(now)}\n".encode())
