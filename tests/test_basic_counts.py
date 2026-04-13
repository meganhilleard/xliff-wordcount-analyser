def test_basic_counts():
  from src.xliff_parser import extract_source_segments
  from src.analysis import analyse_segments


def test_basic_counts():
    segments = extract_source_segments("tests/samples/simple.xliff")
    result = analyse_segments(segments)

    assert result["total_segments"] == 3
    assert result["unique_segments"] == 2
    assert result["repeated_segments"] == 1
    assert result["total_words"] == 5
``
