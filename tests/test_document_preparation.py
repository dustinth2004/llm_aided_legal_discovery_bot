import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm_aided_legal_discovery_bot import (
    parse_email_async,
    parse_enron_email_async,
    beautify_and_format_as_markdown
)


class TestEmailParsing:
    """Tests for email parsing functions."""

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_parse_email_basic(self, sample_email):
        """Test basic email parsing."""
        result = await parse_email_async(sample_email)
        assert "From:" in result
        assert "john.doe@enron.com" in result
        assert "Important Meeting" in result

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_parse_enron_email(self, sample_email):
        """Test Enron-specific email parsing."""
        result = await parse_enron_email_async(sample_email)
        assert "From:" in result
        assert "john.doe@enron.com" in result


class TestMarkdownFormatting:
    """Tests for markdown formatting."""

    @pytest.mark.unit
    def test_beautify_and_format_as_markdown(self):
        """Test markdown beautification."""
        text = "# Title\n\nThis is content."
        result = beautify_and_format_as_markdown(text)
        assert "# Title" in result
        assert "This is content" in result

    @pytest.mark.unit
    def test_beautify_empty_text(self):
        """Test markdown formatting with empty text."""
        result = beautify_and_format_as_markdown("")
        assert isinstance(result, str)
