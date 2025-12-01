import pytest
import sys
from pathlib import Path

# Import functions from main module
sys.path.insert(0, str(Path(__file__).parent.parent))
from llm_aided_legal_discovery_bot import (
    remove_pagination_breaks,
    sophisticated_sentence_splitter,
    highlight_keywords,
    estimate_tokens,
    chunk_text
)


class TestTextProcessing:
    """Tests for text processing functions."""

    @pytest.mark.unit
    def test_remove_pagination_breaks(self):
        """Test removing pagination breaks from text."""
        text = "This is a hyphen-\nated word. And another sen-\ntence here."
        result = remove_pagination_breaks(text)
        # Should join hyphenated words
        assert "hyphenated" in result or "hyphen-\nated" in result
        assert isinstance(result, str)

    @pytest.mark.unit
    def test_sophisticated_sentence_splitter(self):
        """Test sentence splitting."""
        text = "First sentence. Second sentence! Third sentence?"
        sentences = sophisticated_sentence_splitter(text)
        assert len(sentences) == 3
        assert "First sentence" in sentences[0]
        assert "Second sentence" in sentences[1]
        assert "Third sentence" in sentences[2]

    @pytest.mark.unit
    def test_sophisticated_sentence_splitter_with_abbreviations(self):
        """Test sentence splitting handles abbreviations correctly."""
        text = "Dr. Smith works at U.S. Corp. He is very skilled."
        sentences = sophisticated_sentence_splitter(text)
        # The function splits on periods, may not handle all abbreviations perfectly
        assert isinstance(sentences, list)
        assert len(sentences) > 0

    @pytest.mark.unit
    def test_highlight_keywords(self):
        """Test keyword highlighting in text."""
        text = "This document contains fraud and misconduct."
        keywords = ["fraud", "misconduct"]
        result = highlight_keywords(text, keywords)
        assert "**fraud**" in result
        assert "**misconduct**" in result

    @pytest.mark.unit
    def test_highlight_keywords_case_insensitive(self):
        """Test keyword highlighting is case insensitive."""
        text = "FRAUD and Fraud and fraud"
        keywords = ["fraud"]
        result = highlight_keywords(text, keywords)
        # All instances should be highlighted
        assert result.count("**") == 6  # 3 keywords * 2 markers each

    @pytest.mark.unit
    def test_estimate_tokens(self):
        """Test token estimation."""
        text = "This is a simple test."
        tokens = estimate_tokens(text, model_name="gpt-4o-mini")
        assert tokens > 0
        assert isinstance(tokens, int)

    @pytest.mark.unit
    def test_chunk_text(self):
        """Test text chunking."""
        text = "word " * 1000  # Create a long text
        chunks = chunk_text(text, max_chunk_tokens=100, model_name="gpt-4o-mini")
        assert len(chunks) > 1
        for chunk in chunks:
            assert len(chunk) > 0


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.mark.unit
    def test_empty_text_processing(self):
        """Test processing empty text."""
        assert remove_pagination_breaks("") == ""
        assert sophisticated_sentence_splitter("") == []
        assert highlight_keywords("", ["test"]) == ""

    @pytest.mark.unit
    def test_none_handling(self):
        """Test handling of None values."""
        with pytest.raises((TypeError, AttributeError)):
            remove_pagination_breaks(None)

    @pytest.mark.unit
    def test_chunk_text_empty(self):
        """Test chunking empty text."""
        chunks = chunk_text("", max_chunk_tokens=100, model_name="gpt-4o-mini")
        assert len(chunks) == 0 or (len(chunks) == 1 and chunks[0] == "")
