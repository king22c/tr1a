import sys
import os.path
from subprocess import Popen

if sys.platform == 'linux':
    LIBRE_OFFICE = '/usr/bin/soffice'
elif sys.platform == 'darwin':
    LIBRE_OFFICE = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
else:
    raise Exception("Not supported platform")


def convert_to_pdf(input_docx, out_dir):
    print('Converting "%s" to PDF' % input_docx)
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir', out_dir, input_docx])
    p.communicate()


def is_doc(filename: str):
    return filename.endswith('.doc') or filename.endswith('.docx')


if __name__ == '__main__':
    input_dir = sys.argv[1]
    if os.path.exists(input_dir) is False:
        print('Input directory %s is not existed' % input_dir)
        exit(1)
    output_dir = f'{input_dir}/PDF'
    if os.path.exists(output_dir) is False:
        os.mkdir(output_dir)
    count = 0
    for file in os.listdir(input_dir):
        filename = f'{input_dir}/{file}'
        if os.path.isfile(filename) and is_doc(file):
            convert_to_pdf(filename, output_dir)
            count = count + 1
    print('Converted %d files to PDF' % count)
