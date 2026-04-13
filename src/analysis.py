
"""
Analysis logic for localisation metrics.
"""

def analyse_segments(segments):
    """
    Performs basic analysis on a list of segments.
    """
    pass


from collections import Counter

def analyse_segments(segments):
    """
    Basic metrics:
    - total word count (naive whitespace split)
    - repetition rate (exact segment matches)
    - unique segment count
    """
    total_segments = len(segments)
    unique_segments = len(set(segments))
    repeated_segments = total_segments - unique_segments

    repetition_rate = (repeated_segments / total_segments * 100) if total_segments else 0

    total_words = sum(len(s.split()) for s in segments)
    unique_words = len(set(word for s in segments for word in s.split()))

    # Optional: top repeated segments (to help explain repeats)
    counts = Counter(segments)
    top_repeats = [(seg, c) for seg, c in counts.most_common(5) if c > 1]

    return {
        "total_segments": total_segments,
        "unique_segments": unique_segments,
        "repeated_segments": repeated_segments,
        "repetition_rate_percent": round(repetition_rate, 2),
        "total_words": total_words,
        "unique_words": unique_words,
        "top_repeats": top_repeats,  # list of tuples
    }
