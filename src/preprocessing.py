"""Text preprocessing for the Sephora moisturizer review project.

Two versions:
- preprocess_for_extraction: full cleanup for keyword and frequency analysis
- preprocess_for_sentiment: light cleanup for VADER, which relies on capitalization,
  punctuation, and emojis to judge intensity, so those are left in place
"""
import html
import re
import contractions


def contraction_handling(text):
    """Expand contractions ("didn't" -> "did not") so negations stay intact."""
    return contractions.fix(text)


def basic_clean(text):
    """Cleanup shared by both versions: HTML, quote styles, and spacing."""
    # Strip HTML tags, then decode entities (&amp; -> &) so they don't become words like "amp"
    text = re.sub(r"<.*?>", " ", text)
    text = html.unescape(text)
    # Normalize curly apostrophes so contractions like don't are recognized
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    # Add a missing space after sentence punctuation ("great.Love it" -> "great. Love it")
    text = re.sub(r"([.!?])([A-Za-z])", r"\1 \2", text)
    return text


def preprocess_for_extraction(text):
    """Full cleanup for keyword analysis: lowercase, expand contractions, remove
    possessives, numbers, and punctuation."""
    text = basic_clean(text).lower()
    # Expand contractions ("didn't" -> "did not") so negations stay intact
    text = contraction_handling(text)
    # Remove possessives ("tatcha's" -> "tatcha")
    text = re.sub(r"'s\b", "", text)
    # Remove numbers and ordinal suffixes (1st, 2nd, 30)
    text = re.sub(r"\d+(st|nd|rd|th)?", " ", text)
    # Remove punctuation, special characters, and emojis
    text = re.sub(r"[^\w\s]|_", " ", text)
    # Collapse extra whitespace
    return re.sub(r"\s+", " ", text).strip()


def preprocess_for_sentiment(text):
    """Light cleanup for VADER: keeps capitalization, punctuation, and emojis."""
    text = basic_clean(text)
    return re.sub(r"\s+", " ", text).strip()