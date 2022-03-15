import sys
import os.path
from subprocess import Popen

if sys.platform == 'linux':
    LIBRE_OFFICE = '/usr/bin/soffice'
elif sys.platform == 'darwin':
    LIBRE_OFFICE = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
else:
    raise Exception("Not supported platform")


def convert_to_pdf(input_docx):
    out_dir = f'{os.path.dirname(input_docx)}/PDF'
    check_create_dir(out_dir)
    print('Converting "%s" to "%s"' % (input_docx, out_dir))
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir', out_dir, input_docx])
    p.communicate()


def is_doc(fn_: str):
    return fn_.endswith('.doc') or fn_.endswith('.docx')


def check_create_dir(dir_: str):
    if os.path.exists(dir_) is False:
        os.mkdir(dir_)
    return True


if __name__ == '__main__':
    input_dir = sys.argv[1]
    if os.path.exists(input_dir) is False:
        print('Input directory %s is not existed' % input_dir)
        exit(1)
    for root, _dirs, files in os.walk(input_dir):
        for file in files:
            filename = f'{root}/{file}'
            if os.path.isfile(filename) and is_doc(file):
                convert_to_pdf(filename)
