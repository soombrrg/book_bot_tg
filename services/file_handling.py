import os
import sys

BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Делит книгу на страницы указанного размера и
# возвращает строку с текстом страницы и ее размер.
# Размер может отличаться так как концом страницы будет один из специальных символов
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    max_size = start + size
    counter = 0
    if len(text) < max_size:
        size = len(text) - start
        text = text[start:max_size]
    else:
        if text[max_size] == '.' and text[max_size - 1] in end_signs:
            text = text[start:max_size - 2]
            size -= 2
        else:
            text = text[start:max_size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


# Формирует словарь книги
# Ключ - номер страницы.
# Значение - текст страницы.
def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Подготовка книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))