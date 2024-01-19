import sys

def progress_bar(i, total, prefix, length=70, fill='=', print_end='\r'):
    percent = ("{0:.1f}").format(100 * (i / float(total)))
    filled_length = int(length * i // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} [{bar}] {percent}% '),
    sys.stdout.flush()
    if i == total:
        sys.stdout.write(print_end)
        sys.stdout.flush()