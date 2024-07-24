import random
import time

# List of random text examples
random_texts = [
    "Hello, World!",
    "This is a random message.",
    "Python is awesome!",
    "Docker makes deployment easy.",
    "Random text generator."
]

# Choose a random text from the list
random_text = random.choice(random_texts)

# Print the random text
print(random_text)

# Sleep indefinitely
while True:
    time.sleep(3600)  # Sleep for 1 hour (or any large number)
