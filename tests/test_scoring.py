import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm_aided_legal_discovery_bot import calculate_importance_score


class TestImportanceScoring:
    """Tests for importance scoring calculation."""

    @pytest.mark.unit
    def test_calculate_importance_score_all_max(self):
        """Test importance score with all maximum values."""
        scores = {
            'relevance': 10,
            'keyword_density': 10,
            'entity_mentions': 10,
            'temporal_relevance': 10,
            'credibility': 10,
            'uniqueness': 10
        }
        result = calculate_importance_score(scores)
        assert result == 10.0

    @pytest.mark.unit
    def test_calculate_importance_score_all_min(self):
        """Test importance score with all minimum values."""
        scores = {
            'relevance': 0,
            'keyword_density': 0,
            'entity_mentions': 0,
            'temporal_relevance': 0,
            'credibility': 0,
            'uniqueness': 0
        }
        result = calculate_importance_score(scores)
        assert result == 0.0

    @pytest.mark.unit
    def test_calculate_importance_score_weighted(self):
        """Test importance score weighting is correct."""
        # Relevance has 40% weight, should dominate
        scores = {
            'relevance': 10,  # 40% weight
            'keyword_density': 0,  # 20% weight
            'entity_mentions': 0,  # 15% weight
            'temporal_relevance': 0,  # 10% weight
            'credibility': 0,  # 10% weight
            'uniqueness': 0  # 5% weight
        }
        result = calculate_importance_score(scores)
        assert result == 4.0  # 10 * 0.4 = 4.0

    @pytest.mark.unit
    def test_calculate_importance_score_range(self):
        """Test importance score is within valid range."""
        scores = {
            'relevance': 7,
            'keyword_density': 5,
            'entity_mentions': 6,
            'temporal_relevance': 4,
            'credibility': 8,
            'uniqueness': 3
        }
        result = calculate_importance_score(scores)
        assert 0.0 <= result <= 10.0

    @pytest.mark.unit
    def test_calculate_importance_score_missing_keys(self):
        """Test handling of missing score keys."""
        scores = {
            'relevance': 5,
            'keyword_density': 5
            # Missing other keys
        }
        with pytest.raises(KeyError):
            calculate_importance_score(scores)
