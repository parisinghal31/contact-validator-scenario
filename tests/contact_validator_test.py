import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone

def test_is_valid_email_true():
    email = "student@lpu.in"
    assert is_valid_email(email) == True

def test_is_valid_email_type_error():
    with pytest.raises(TypeError):
        is_valid_email(12345)

def test_is_valid_phone_true():
    phone = "555-123-4567"
    assert is_valid_phone(phone) == True

def test_mask_email_basic():
    email = "priya@example.com"
    assert mask_email(email) == "pr***@example.com"

def test_mask_email_invalid():
    with pytest.raises(ValueError):
        mask_email("invalid-email")

def test_normalize_phone_valid():
    assert normalize_phone("555-123-4567") == "5551234567"

def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("invalid-phone")