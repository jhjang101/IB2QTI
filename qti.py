import os
import subprocess
import shutil
import time
import txt

# prompt filename and make folder
def file_in():
    """
    prompt and returns docx file name.
    """
    # ask file name
    print("type filename without docx extension. (Ex. test)")
    file = input()

    # make a folder
    os.makedirs(file,exist_ok=True)

    return(file)


def pandoc(file):
    '''
    convert docx to github-flavored markdown txt file.
    :param filein: docx file name
    :return: no return but create a txt file in the same folder
    '''
    filein = file + '.docx'
    fileout = file +'gfm.txt'
    filepath = os.path.join(f'{file}/',fileout)
    subprocess.run(['pandoc', f'--extract-media=.', filein, '-t', 'gfm', '-o', filepath], shell=True)
    time.sleep(0.1)
    shutil.move('media', file)

def reformat_txt(file):
    filein = file + 'gfm.txt'
    fileout = file +'.txt'
    fileinpath = os.path.join(f'{file}/',filein)
    fileoutpath = os.path.join(f'{file}/',fileout)

    questions = txt.read_questions(fileinpath)

    for question in questions:
        question = txt.remove_emptyline(question)
        question = txt.fix_equation(question)
        question = txt.fix_image(question)
        question = txt.fix_answers(question)
        question = txt.add_answer(question)
        num, key, stem, answers = txt.slice(question)

        with open(fileoutpath, 'a', encoding='utf-8') as fo:
            fo.writelines(num)
            fo.writelines(stem)
            fo.writelines(answers)
            fo.writelines(['\n'])


def txt2qti(file):
    '''
    convert github-flavored markdown txt file to qti.
    :param file: txt file name
    :return: no return but create a zip file in the same folder
    '''
    filein = file + '.txt'
    fileinpath = os.path.join(f'{file}/',filein)
    subprocess.run(['text2qti', fileinpath], shell=True)


if __name__ == "__main__":

    file = file_in()
    pandoc(file)
    reformat_txt(file)
    txt2qti(file)