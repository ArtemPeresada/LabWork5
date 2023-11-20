def read_paragraphs_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        paragraphs = content.split('\n\n')  # Розділення абзаців за порожніми рядками
        return paragraphs

def find_paragraphs_with_tag(tag, paragraphs):
    matching_paragraphs = [(i+1, paragraph) for i, paragraph in enumerate(paragraphs) if f'#{tag} ' in paragraph]
    return matching_paragraphs

if __name__ == "__main__":
    while True:
        file_path = input("Введіть шлях до текстового файлу: ")

        try:
            paragraphs = read_paragraphs_from_file(file_path)
            break  # Вийти з циклу, якщо файл був успішно зчитаний
        except FileNotFoundError:
            print(f"Файл {file_path} не знайдено. Спробуйте ще раз.")

    while True:
        tag_to_find = input("Введіть тег для пошуку: ")
        matching_paragraphs = find_paragraphs_with_tag(tag_to_find, paragraphs)

        if matching_paragraphs:
            print("\nАбзаци, що містять тег:")
            for paragraph_number, (original_number, paragraph) in enumerate(matching_paragraphs, 1):
                print(f"\nАбзац {original_number}:\n{paragraph}")
            break  # Вийти з циклу, якщо теги були успішно знайдені
        else:
            print(f"\nТег '#{tag_to_find}' не знайдено в жодному абзаці. Спробуйте ще раз.")
