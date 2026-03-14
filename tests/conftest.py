import pytest
import os
import sys
from pathlib import Path

# Add parent directory to path so we can import the main module
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_text():
    """Sample text for testing text processing functions."""
    return """This is a sample document. It contains multiple sentences.
    Some sentences span
    multiple lines. This is useful for testing."""


@pytest.fixture
def sample_email():
    """Sample email for testing email parsing."""
    return """From: john.doe@enron.com
To: jane.smith@enron.com
Date: Mon, 14 May 2001 10:30:45 -0700 (PDT)
Subject: Important Meeting

This is the body of the email.
It contains important information about the meeting."""


@pytest.fixture
def sample_discovery_config():
    """Sample discovery configuration for testing."""
    return {
        "case_name": "Test Case",
        "discovery_goals": [
            "Identify evidence of fraud"
        ],
        "keywords": ["fraud", "misconduct", "illegal"],
        "entities_of_interest": ["John Doe", "Jane Smith"],
        "importance_threshold": 0.7
    }


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing."""
    return "This is a mock LLM response."


@pytest.fixture
def temp_test_dir(tmp_path):
    """Create a temporary directory for test files."""
    test_dir = tmp_path / "test_data"
    test_dir.mkdir()
    return test_dir


@pytest.fixture
def sample_pdf_path(temp_test_dir):
    """Create a sample text file to simulate a document."""
    pdf_file = temp_test_dir / "sample.txt"
    pdf_file.write_text("Sample document content for testing.")
    return str(pdf_file)
