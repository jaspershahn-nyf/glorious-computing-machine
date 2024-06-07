from datetime import datetime

datestring = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

print(f"Hello, today's date is really {datestring}")