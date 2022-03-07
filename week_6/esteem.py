
def main():
    total_score = 0
    choice = ''
    positive_statements = ['I feel that I am a person of worth, at least on an equal plane with others.', 'I feel that I have a number of good qualities.','I am able to do things as well as most other people.','I take a positive attitude toward myself.','On the whole, I am satisfied with myself.']
    negative_statements = ['All in all, I am inclined to feel that I am a failure.','I feel I do not have much to be proud of.','I wish I could have more respect for myself.','I certainly feel useless at times.','At times I think I am no good at all.']
    
    print ('This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters: \n')
    print ('D means you strongly disagree with the statement. \
\nd means you disagree with the statement.\
\na means you agree with the statement.\
\nA means you strongly agree with the statement.\n')
    
    total_score += ask_positive_statements(positive_statements)
    total_score += ask_negative_statements(negative_statements)
    give_score (total_score)



def ask_positive_statements(statements):
    score = 0
    for question in statements:
        print(question)
        answer = input ('')
        score += positive_answers(answer)
    return score

def ask_negative_statements(statements):
    score = 0
    for question in statements:
        print(question)
        answer = input ('')
        score += negative_answers(answer)
    return score

def positive_answers(choice):
    if choice == 'D':
        return 0
    elif choice == 'd':
        return 1
    elif choice == 'a':
        return 2
    elif choice == 'A':
        return 3
    else:
        print('invalid input')

def negative_answers(choice):
    if choice == 'D':
        return 3
    elif choice == 'd':
        return 2
    elif choice == 'a':
        return 1
    elif choice == 'A':
        return 0
    else:
        print('incorrect input')

def give_score(score):
    print (f'\nYour total score was: {score}/30')
    if score >= 15 :
        print ('Way to go! Keep it up!')
    elif score <= 15 :
        print ('You may have low self-esteem. Talk with a friend')
main()
