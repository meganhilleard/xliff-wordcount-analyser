def test_repetitions_are_detected():
  from src.analysis import analyse_segments


def test_repetition_rate():
    segments = ["Hello", "Hello", "World"]
    result = analyse_segments(segments)

    assert result["repeated_segments"] == 1
``
