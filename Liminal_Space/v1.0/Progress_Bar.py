import sys
import color as c

def progress_bar(i, total, prefix, length=70, fill='=', print_end='\r'):
    percent = ("{0:.1f}").format(100 * (i / float(total)))
    filled_length = int(length * i // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    if i == total:
        sys.stdout.write('\r{} {} {}% '.format(c.yellow(f'{prefix}:'), c.green('[' + f'{bar}' + ']'), percent))
    else:
        sys.stdout.write('\r{} {} {}% '.format(c.yellow(f'{prefix}:'), c.red('[' + f'{bar}' + ']'), percent))
    sys.stdout.flush()
    if i == total:
        sys.stdout.write(print_end)
        sys.stdout.flush()
