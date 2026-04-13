
"""
XLIFF parsing utilities.
"""

def extract_source_segments(xliff_path):
    """
    Extracts source segments from an XLIFF file.
    """
    pass

import xml.etree.ElementTree as ET


def extract_source_segments(xliff_path):
    """
    Extract all <source> text nodes from an XLIFF file.
    This intentionally starts simple (namespace-agnostic).
    """
    tree = ET.parse(xliff_path)
    root = tree.getroot()

    segments = []
    for elem in root.iter():
        if elem.tag.endswith("source") and elem.text:
            text = elem.text.strip()
            if text:
                segments.append(text)

    return segments
