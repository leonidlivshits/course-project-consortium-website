import pytest
from unittest.mock import MagicMock, patch
from app.translator import translate_to_english

def test_translate_to_english_empty_or_non_string():
    assert translate_to_english("") == ""
    assert translate_to_english(None) is None
    assert translate_to_english(123) == 123


def test_translate_to_english_successful_translation():
    mock_translator = MagicMock()
    mock_translator.translate.return_value = "Translated text"

    result = translate_to_english("Текст", mock_translator)
    assert result == "Translated text"
    mock_translator.translate.assert_called_once_with("Текст")


def test_translate_to_english_error():
    mock_translator = MagicMock()
    mock_translator.translate.side_effect = Exception("Error")

    result = translate_to_english("Ошибка", mock_translator)
    assert result == "Ошибка"
    mock_translator.translate.assert_called_once_with("Ошибка")

def test_translate_to_english_mymemory_warning():
    mock_translator = MagicMock()
    mock_translator.translate.return_value = "MYMEMORY WARNING"

    result = translate_to_english("Текст", mock_translator)
    assert result == "Текст"
    mock_translator.translate.assert_called_once_with("Текст") 
