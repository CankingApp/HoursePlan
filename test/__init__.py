_FILE_NAME_SAVE = 'day_net_signatory_pro.csv'

with open(_FILE_NAME_SAVE, 'rb+') as csv_file:
    off = -100
    while True:
        csv_file.seek(off, 2)
        lines = csv_file.readlines()
        if len(lines) >= 2:
            last_line = lines[-1]
            print(last_line)
            break
        off *= 2

