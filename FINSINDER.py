import os

print("выберите язык для программы введите 1 для русского и 2 для англиского")
print("choose a language for the program 1 for russian 2 for english")
lang = input()
if lang == "1":
    result = "результат.txt"
    wordses = "Введите слова для поиска (через пробел): "
    resultIN = "|          путь                                          | номер строки | найденная строка |              |\n"
    searchEND = "Поиск завершен. Результат записан в файл 'результат.txt'"
    exit = "Нажмите Enter, чтобы выйти..."
    luassa = "введите расширение файлов для поиска, пример: .txt :"
if lang == "2":
    result = "result.txt"
    wordses = "Enter search words (space separated): "
    resultIN = "|          path                                          | line number | found string |                   |\n"
    searchEND = "Search completed. The result is written to the file 'result.txt'"
    exit = "Press Enter to exit..."
    luassa = "enter the file extension to search for, example: .txt :"
lua = input(luassa)




def search_files(directory, words):
    result = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(lua):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='cp1251', errors='ignore') as f:
                    lines = f.readlines()
                    for line_num, line in enumerate(lines, 1):
                        for word in words:
                            if word in line:
                                result.append(f"| {filepath} | {line_num} | {line.strip()} |\n")

    return result

if __name__ == "__main__":
    directory = os.getcwd()

    search_words = input(wordses).split()

    results = search_files(directory, search_words)

    with open(result, 'w', encoding='cp1251') as f:
        f.write("|-FINSENDER-1.1----------------------------------------------------------------------------made by 2E2E3W-|\n")
        f.write(resultIN)
        f.write("|---------------------------------------------------------------------------------------------------------|\n")
        f.writelines(results)

    print(searchEND)
    input(exit)
