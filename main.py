import datetime

if __name__ == "__main__":
    with open("log.txt", "w") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        f.write(f"Updated {now}\n".encode())
