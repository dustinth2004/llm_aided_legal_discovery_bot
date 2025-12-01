import pytest
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm_aided_legal_discovery_bot import (
    generate_completion,
    is_gpu_available,
    calculate_safe_max_tokens
)


class TestLLMIntegration:
    """Tests for LLM integration functions (with mocking)."""

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_generate_completion_openai_mock(self, mock_llm_response):
        """Test OpenAI completion generation with mock."""
        with patch('llm_aided_legal_discovery_bot.USE_LOCAL_LLM', False), \
             patch('llm_aided_legal_discovery_bot.API_PROVIDER', 'OPENAI'), \
             patch('llm_aided_legal_discovery_bot.generate_completion_from_openai',
                   new_callable=AsyncMock) as mock_openai:

            mock_openai.return_value = mock_llm_response

            result = await generate_completion(
                "Test prompt",
                model="gpt-4o-mini",
                max_tokens=100
            )

            assert result == mock_llm_response
            mock_openai.assert_called_once()

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_generate_completion_claude_mock(self, mock_llm_response):
        """Test Claude completion generation with mock."""
        with patch('llm_aided_legal_discovery_bot.USE_LOCAL_LLM', False), \
             patch('llm_aided_legal_discovery_bot.API_PROVIDER', 'CLAUDE'), \
             patch('llm_aided_legal_discovery_bot.generate_completion_from_claude',
                   new_callable=AsyncMock) as mock_claude:

            mock_claude.return_value = mock_llm_response

            result = await generate_completion(
                "Test prompt",
                model="claude-3-haiku-20240307",
                max_tokens=100
            )

            assert result == mock_llm_response
            mock_claude.assert_called_once()

    @pytest.mark.unit
    def test_is_gpu_available(self):
        """Test GPU availability check."""
        result = is_gpu_available()
        assert isinstance(result, bool)

    @pytest.mark.unit
    def test_calculate_safe_max_tokens(self):
        """Test safe max tokens calculation."""
        result = calculate_safe_max_tokens(
            context_length=4096,
            prompt_tokens=100,
            buffer=50
        )
        assert result > 0
        assert result <= 4096 - 100 - 50


class TestLLMErrorHandling:
    """Tests for LLM error handling."""

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_generate_completion_empty_prompt(self):
        """Test completion generation with empty prompt."""
        with patch('llm_aided_legal_discovery_bot.USE_LOCAL_LLM', False), \
             patch('llm_aided_legal_discovery_bot.API_PROVIDER', 'OPENAI'), \
             patch('llm_aided_legal_discovery_bot.generate_completion_from_openai',
                   new_callable=AsyncMock) as mock_openai:

            mock_openai.return_value = ""

            result = await generate_completion(
                "",
                model="gpt-4o-mini",
                max_tokens=100
            )

            # Should still call the function even with empty prompt
            mock_openai.assert_called_once()
