

questions = [
    {
        "prompt": "What is the state capital of California?",
        "options": ["A. Fresno", "B. Los Angeles", "C. Sacramento", "D. San Jose"],
        "answer": "C"
    },
    {
        "prompt": "Who wrote 'Fight Club'?",
        "options": ["A. Chuck Palahniuk", "B. Stephen King", "C. Mark Twain", "D. Harper Lee"],
        "answer": "A"
    },
    {
        "prompt": "What is the highest hand in a typical five card poker game?",
        "options": ["A. Full House", "B. Straight Flush", "C. 4 of a kind", "D. Flush"],
        "answer": "B"
    },
    {
        "prompt": "What is the best lean/fat ratio of beef for making a smash burger?",
        "options": ["A. 95/5", "B. 60/40", "C. 50/50", "D. 80/20"],
        "answer": "D"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper() 
        #The '.upper()' makes it so that even if a lowercase answer is given it converts it to upper to match the answer.
        if answer == question["answer"]:
            print("Correct, well done!\n")
            score += 1
        else:
            print("Incorrect, the correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")    



run_quiz(questions)
