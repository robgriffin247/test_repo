import datetime

if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "w") as file:
        file.write(f"{now}")