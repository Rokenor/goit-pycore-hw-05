import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    parsed_str = line.split(' ', 3)
    if len(parsed_str) < 4:
        return None
    
    return {
        "date": parsed_str[0],
        "time": parsed_str[1],
        "level": parsed_str[2],
        "message": parsed_str[3]
    }

def load_logs(file_path: str) -> list[dict]:
    normalized_logs = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    log_dict = parse_log_line(cleaned_line)
                    if log_dict:
                        normalized_logs.append(log_dict)
                    else:
                        print(f'Warning: Unexpected format line was skipped: {cleaned_line}')
    except FileNotFoundError:
        print(f'Error: File {file_path} not found')
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
    
    return normalized_logs
        

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list(filter(lambda log: log['level'] == level, logs))
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    levels = (log['level'] for log in logs)
    level_counts = Counter(levels)
    return level_counts

def display_log_counts(counts: dict, log_level_filter: str, filtered_logs: list[dict]):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        print(f'{level:<16} | {count}')
    if log_level_filter is not None:
        print(f'\nДеталі логів для рівня {log_level_filter}:')
        if filtered_logs: 
            for log in filtered_logs:
                print(f'{log['date']} {log['time']} - {log['message']}')
        else:
            print(f'Немає логів для рівня {log_level_filter}.')

def main():
    # Перевірка коректності введеної команди
    if len(sys.argv) < 2:
        print('Usage: python main.py <file_path> [filtration_level]')
        sys.exit(1)

    # Визначення введеного шляху до файлу 
    log_file_path = sys.argv[1]

    # Визначення значення введеного фільтру
    log_level_filter = None
    if len(sys.argv) > 2:
        log_level_filter = sys.argv[2].upper()

    # Завантаження та нормалізація логів з файлу
    loaded_logs = load_logs(log_file_path)

    # Підрахунок записів за рівнем логування
    logs_count = count_logs_by_level(loaded_logs)

    # Фільтрація отриманих логів по введеному користувачем фільтру
    filtered_logs = []
    if log_level_filter != None:
        # Перевірка чи є введений користувачем фільтр як один з level параметрів в логах
        if log_level_filter not in logs_count:
            print(f"Error: Log level '{log_level_filter}' not found in file.")
            sys.exit(1)

        filtered_logs = filter_logs_by_level(loaded_logs, log_level_filter)

    # Вивід результатів в консоль
    display_log_counts(logs_count, log_level_filter, filtered_logs)

if __name__ == "__main__":
    main()