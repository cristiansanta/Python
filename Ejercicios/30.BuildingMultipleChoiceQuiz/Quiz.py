from Question import question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) yellow\n\n",
    "What color are strawberries?\n(a) yellow\n(b) Red\n(c) Blue\n\n"
]
#Question Objects
questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions: #Each question Object----in----questions ARRAY
        answer = input(question.prompt) #STORE response = ASK the user the question
        if answer == question.answer: #Check if we got the question right
            score += 1
    print("YOU GOT "+ str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)
