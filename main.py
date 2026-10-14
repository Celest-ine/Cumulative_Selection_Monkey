"""The infinite monkey theorem states that a monkey hitting keys at random on a
typewriter keyboard for an infinite amount of time will almost surely type any
given text, such as the complete works of William Shakespeare.

This is a cumulative selection algorithm that keeps the correct characters and generates new random characters for the incorect ones.
This is a more effective approach than generating a completly random string each time, as it allows the algorithm to converge towards the target phrase more quickly.
"""

import random
import string
import time

ALLOWED_CHARACTERS = (
    string.ascii_letters
    + string.digits
    + string.punctuation
    + " "
)

def get_targeted_string():
    """Get a string from the user."""
    
    print(
        "*" * 5
        + " This program will tell you how long it would take to type some words until they match the phrase you entered while keeping the correct characters and generating new random characters for the incorrect ones."
        + "*" * 5
    )

    while True:
        try:
            phrase = (input("What phrase/word do you want the monkey to generate? ").strip())

            if not phrase:
                raise ValueError("The phrase cannot be empty. Please enter a valid phrase.")
        
            for char in phrase:
                if char not in ALLOWED_CHARACTERS:
                    raise ValueError(
                        f"The phrase contains invalid character '{char}'. Please use only letters, digits, punctuation, and spaces."
                        )

        except ValueError as e:
            print(e)
            continue

        return phrase


def generate_string(the_phrase, current_phrase):
    """Generate a new phrase while keeping characters that are already correct."""

    characters = ALLOWED_CHARACTERS
    new_phrase = []

    for target_char, current_char in zip(the_phrase, current_phrase):

        if target_char == current_char:
            # Keep characters that are already correct.
            new_phrase.append(current_char)
        else:
            # Generate a new random character for incorrect positions.
            new_phrase.append(random.choice(characters))

    return "".join(new_phrase)


def score_generated_strings(the_phrase):
    """Generate strings until every character matches the target."""

    attempts = 0
    start_time = time.time()

    # Start with a completely random phrase.
    characters = ALLOWED_CHARACTERS
    current_phrase = "".join(
        random.choice(characters) for _ in range(len(the_phrase))
    )

    while True:
        attempts += 1

        current_phrase = generate_string(the_phrase, current_phrase)

        matches = sum(1 for char1, char2 in zip(current_phrase, the_phrase) if char1 == char2)
        score = (matches / len(the_phrase)) * 100

        if score == 100:
            end_time = time.time()

            print(f"\nSuccess after {attempts} generations.")
            print(f"The generated phrase is: {current_phrase}")
            print(f"Time taken is: {end_time - start_time:.4f} seconds.")
            break

        elif attempts % 100 == 0:
            print(f"\nAttempts: {attempts}, Score: {score:.2f}%")
            print(f"The best generated phrase is: {current_phrase}")


the_phrase = get_targeted_string()
score_generated_strings(the_phrase)