# Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains name of the file and number in that file:
import random
import csv


def generate_random_number():
    return random.randint(1, 100)


def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(str(content))


def create_files_and_summary():
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    summary = ''
    for alphabet in alphabets:
        filename = alphabet + '.txt'
        random_number = generate_random_number()
        write_to_file(filename, random_number)
        summary += f'{filename}: {random_number}\n'
    return summary


def main():
    summary = create_files_and_summary()
    write_to_file('summary.txt', summary)


if __name__ == "__main__":
    main()


# Create file with some content.
some_content = """Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу"""


with open('some_file.txt', 'w', encoding='utf-8') as file:
    file.write(some_content)


# Create second file and copy content of the first file to the second file in upper case.
with open('some_file.txt', 'r', encoding='utf-8') as file1:
    content = file1.read().upper()

with open('some_second_file.txt', 'w', encoding='utf-8') as file2:
    file2.write(content)



# Write a program that will simulate user score in a game.
# Create a list with 5 player's names. After that simulate 100 games for each player.
# As a result of the game create a list with player's name and his score (0-1000 range). And save it to a CSV file.

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

with open('player_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #the header of the file
    writer.writerow(["Player name", "Score"])

    # Simulate 100 games for each player
    for _ in range(100):
        for player in players:
            #random score for the player
            score = random.randint(0, 1000)
            # Write the player's name and score to the CSV file
            writer.writerow([player, score])



# Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv
# where each row contains the player name and their highest score. Final score should sorted by descending of highest score

# to store the highest score for each player
high_scores = {}

with open('player_scores.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        player, score = row[0], int(row[1])

        if player not in high_scores or score > high_scores[player]:
            high_scores[player] = score

# Sort the players by their high scores in descending order
sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)

# Write the high scores to a new CSV file
with open('high_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Highest score"])  # the header row
    for player, score in sorted_scores:
        writer.writerow([player, score])



