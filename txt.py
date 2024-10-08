import re

def read_questions(file):
    '''
    function to read questions from github-flavered markdown text file
    :param file: file name of the text file
    :return: list of questions. Each element is also a list of line.
    '''
    questions =[]
    line_numbers = []

    # open and read the file line by line
    with open(file, 'r', encoding='utf-8') as fi:
        contents = fi.readlines()

    # find line number of each question
    for i, line in enumerate(contents):
        if bool(re.match(r'\*\*\d+\.\*\*', line)):    # find question start line
            line_numbers.append(i)
        elif bool(re.search('International Baccalaureate Organization', line)):
            line_numbers.append(i)
    
    # slice each question block and save into questions list
    for i, line_number in enumerate(line_numbers[:-1]):
        start_of_question = line_number
        end_of_question = line_numbers[i+1]-1
        question = contents[start_of_question:end_of_question]
        questions.append(question)

    return(questions)


def remove_duplicates(questions):
    '''
    function to remove duplicate questions.
    '''
    stems = []
    new_questions = []
    for question in questions:
        stem = question[2]
        if stem not in stems:
            stems.append(stem)
            new_questions.append(question)

    return new_questions


def remove_emptyline(question):
    '''
    remove a line that contains [1]
    '''
    line_to_remove = '\\[1\\]\n'
    question = [line for line in question if line != line_to_remove]      # remove point
    return(question)


def fix_equation(question):
    '''
    $$ to $
    '''
    question = [line.replace('$$', '$') for line in question]
    return(question)


def fix_image(question):
    '''
    html-taged image to markdown-taged image
    '''
    start_tag = 'src="./(.*?)"'
    end_tag = '" />'

    for i, line in enumerate(question):
        if re.search(start_tag, line):
            img = re.findall(start_tag, line)[0]    # get image address
            question[i] = f'![]({img})\n'     # replace the line with markdown formatted image line

    for i, line in enumerate(question):
        if re.search(end_tag, line):
            question.pop(i)                         # remove remaining html taged image line
    
    return(question)


def fix_answers(question):
    '''
    A.space  to a) 
    '''
    for i, line in enumerate(question):
        if bool(re.match(r'A\.\s+', line)):
            question[i] = re.sub(r'A\.\s+','a)\t', line)
        elif bool(re.match(r'B\.\s+', line)):
            question[i] = re.sub(r'B\.\s+','b)\t', line)
        elif bool(re.match(r'C\.\s+', line)):
            question[i] = re.sub(r'C\.\s+','c)\t', line)
        elif bool(re.match(r'D\.\s+', line)):
            question[i] = re.sub(r'D\.\s+','d)\t', line)
        else:
            pass
    return(question)


def add_answer(question):
    '''
    add answers if there is no answers
    '''
    is_answer = True
    answers = ['a)\tA \n', 'b)\tB \n', 'c)\tC \n', 'd)\tD \n']

    for line in question:
        if line.startswith('a)\t'):
            is_answer = False

    if is_answer:
        for i, line in enumerate(question):
            if line.startswith('Markscheme'):
                insert_pos = i

        for i in range(len(answers)):
            question.insert(insert_pos+i, answers[i])
    
    return(question)


def slice(question):                ### question number, key
    '''
    slice and reformat question into question number, key, stem, answers
    '''
    for i, line in enumerate(question):
        if line.startswith('a)\t'):
            answer_start = i
        elif line.startswith('Markscheme'):
            answer_end = i

    num = re.findall(r'\*\*(.*?)\*\*', question[0])[0]           # 13.
    key = f'{question[answer_end+2][0].lower()})'                # a)
    stem = [f'\t{line}' for line in question[2:answer_start]]    # add tap
    answers = [f'*{answer}' if answer[:2] == key else answer for answer in question[answer_start:answer_end]]    # add * for correct answer
    
    return(num, key, stem, answers)






if __name__ == "__main__":

    questions = read_questions('A.2 Forces and momentum (2025)gfm.txt')

    res = remove_duplicates(questions)
    for i in res:
        print(i[2])

    print(len(questions))
    print(len(res))

    # for question in questions:
    #     question = remove_emptyline(question)
    #     question = fix_equation(question)
    #     question = fix_image(question)
    #     question = fix_answers(question)
    #     question = add_answer(question)
    #     num, key, stem, answers = slice(question)

    #     with open('out.txt', 'a', encoding='utf-8') as fo:
    #         fo.writelines(num)
    #         fo.writelines(stem)
    #         fo.writelines(answers)
    #         fo.writelines(['\n'])


# question = questions[7]
# question = remove_emptyline(question)
# question = fix_equation(question)
# question = fix_image(question)
# question = fix_answers(question)
# question = add_answer(question)
# num, key, stem, answers = slice(question)

# print(num)
# print(key)
# print(*stem, sep = '')
# print(*answers, sep = '')

# with open('out.txt', 'a', encoding='utf-8') as fo:
#     fo.writelines(num)
#     fo.writelines(stem)
#     fo.writelines(answers)
#     fo.writelines(['\n'])

