
def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    user_answer = input("Please select an option (1-4): ")
    
    if user_answer.isdigit() and int(user_answer) - 1 == answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {options[answer]}\n")
        return False

def run_quiz():
    score = 0
    questions = [
        {
            "question": "Which gas is primarily responsible for the greenhouse effect?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
            "answer": 2
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
            "answer": 1
        },
        {
            "question": "In computer science, what does 'CPU' stand for?",
            "options": ["Central Processing Unit", "Central Personal Unit", "Control Processing Unit", "Computer Power Unit"],
            "answer": 0
        },
        {
            "question": "What is the main function of DNA?",
            "options": ["Energy production", "Protein synthesis", "Genetic information storage", "Cell division"],
            "answer": 2
        },
        {
            "question": "What is the primary purpose of an operating system?",
            "options": ["Run applications", "Manage hardware resources", "Provide security", "All of the above"],
            "answer": 3
        },
        {
            "question": "Which of the following is a renewable energy source?",
            "options": ["Coal", "Natural Gas", "Solar Power", "Nuclear Energy"],
            "answer": 2
        },
        {
            "question": "What is the basic unit of life?",
            "options": ["Atom", "Molecule", "Cell", "Organ"],
            "answer": 2
        },
        {
            "question": "What type of bond involves the sharing of electron pairs?",
            "options": ["Ionic Bond", "Covalent Bond", "Metallic Bond", "Hydrogen Bond"],
            "answer": 1
        },
        {
            "question": "Which programming language is known as the foundation of web development?",
            "options": ["Python", "Java", "HTML", "C++"],
            "answer": 2
        },
        {
            "question": "In genetics, what does 'phenotype' refer to?",
            "options": ["Genetic makeup", "Physical expression of a trait", "Inherited characteristics", "Chromosomal structure"],
            "answer": 1
        },
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()
