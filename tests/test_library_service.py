import pytest
from unittest.mock import Mock
from app.services.library_service import get_books, create_book, update_book, delete_book

@pytest.fixture
def mock_db():
    db_mock = Mock()
    return db_mock

def test_get_books(mock_db):
    mock_db.get_all_books.return_value = [
        {"isbn": "1234567890123", "title": "Test Book", "copies_available": 5}
    ]
    
    result = get_books()
    
    assert result == [{"isbn": "1234567890123", "title": "Test Book", "copies_available": 5}]
    mock_db.get_all_books.assert_called_once()

def test_create_book_success(mock_db):
    create_book("1234567890123", "Test Book", 5)
    
    mock_db.add_book.assert_called_once_with("1234567890123", "Test Book", 5)

def test_create_book_missing_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN and title are required"):
        create_book("", "Test Book", 5)

def test_create_book_missing_title(mock_db):
    with pytest.raises(ValueError, match="ISBN and title are required"):
        create_book("1234567890123", "", 5)

def test_create_book_title_too_long(mock_db):
    with pytest.raises(ValueError, match="Title must be 30 characters or less"):
        create_book("1234567890123", "This Title Is Way Too Long To Be Valid", 5)

def test_create_book_negative_copies(mock_db):
    with pytest.raises(ValueError, match="Copies available cannot be negative"):
        create_book("1234567890123", "Test Book", -1)

def test_create_book_invalid_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN must be 13 digits"):
        create_book("12345", "Test Book", 5)

def test_update_book_success(mock_db):
    update_book("1234567890123", "Updated Book", 3)
    
    mock_db.update_book.assert_called_once_with("1234567890123", "Updated Book", 3)

def test_update_book_missing_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN and title are required"):
        update_book("", "Updated Book", 3)

def test_update_book_missing_title(mock_db):
    with pytest.raises(ValueError, match="ISBN and title are required"):
        update_book("1234567890123", "", 3)

def test_update_book_title_too_long(mock_db):
    with pytest.raises(ValueError, match="Title must be 30 chars or less"):
        update_book("1234567890123", "This Title Is Way Too Long To Be Valid", 3)

def test_update_book_negative_copies(mock_db):
    with pytest.raises(ValueError, match="Copies cannot be negative"):
        update_book("1234567890123", "Updated Book", -1)

def test_update_book_invalid_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN must be 13 digits"):
        update_book("12345", "Updated Book", 3)

def test_delete_book_success(mock_db):
    delete_book("1234567890123")
    
    mock_db.delete_book.assert_called_once_with("1234567890123")

def test_delete_book_missing_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN is required"):
        delete_book("")

def test_delete_book_invalid_isbn(mock_db):
    with pytest.raises(ValueError, match="ISBN must be 13 digits"):
        delete_book("12345")