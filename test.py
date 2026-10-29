from main import generate_string, ALLOWED_CHARACTERS

TARGET = "hello"
CURRENT = "hxlxo"
RUNS = 300

def test_output_promises():
    """Promises that must hold on every call whatever the randomness does."""

    for _ in range(RUNS):
        result = generate_string(TARGET, CURRENT)

        assert len(result) == len(TARGET)

        for char in result:
            assert char in ALLOWED_CHARACTERS

        for target_char, current_char, new_char in zip(TARGET, CURRENT, result):
            if current_char == target_char:
                assert new_char == target_char

def test_wrong_positions_are_rerolled():
    """A function that does nothing must fail this test."""

    results = [generate_string(TARGET, CURRENT) for _ in range(RUNS)]

    for idx, (target_char, current_char) in enumerate(zip(TARGET, CURRENT)):
        if current_char != target_char:
            assert any(result[idx] != current_char for result in results)

def test_already_correct_phrase_is_unchanged():
    """Nothing to reroll, so the output is fully predictable."""
    assert generate_string(TARGET, TARGET) == TARGET

if __name__ == "__main__":
    test_output_promises()
    test_already_correct_phrase_is_unchanged()
    test_wrong_positions_are_rerolled()
    print("All tests passed")