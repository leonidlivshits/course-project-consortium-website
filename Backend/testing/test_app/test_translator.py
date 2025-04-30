import pytest
from unittest.mock import MagicMock, patch
from app.translator import translate_to_english, translate_to_russian

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



def test_translate_to_russian_empty_or_non_string():
    assert translate_to_russian("") == ""
    assert translate_to_russian(None) is None
    assert translate_to_russian(123) == 123

def test_translate_to_russian_successful_translation():
    mock_translator = MagicMock()
    mock_translator.translate.return_value = "Переведенный текст"

    result = translate_to_russian("Text", mock_translator)
    assert result == "Переведенный текст"
    mock_translator.translate.assert_called_once_with("Text")

def test_translate_to_russian_error():
    mock_translator = MagicMock()
    mock_translator.translate.side_effect = Exception("Error")

    result = translate_to_russian("Error", mock_translator)
    assert result == "Error"
    mock_translator.translate.assert_called_once_with("Error")

def test_translate_to_russian_mymemory_warning():
    mock_translator = MagicMock()
    mock_translator.translate.return_value = "MYMEMORY WARNING"

    result = translate_to_russian("Text", mock_translator)
    assert result == "Text"
    mock_translator.translate.assert_called_once_with("Text")