# CLI Quiz Example 2

# Quiz questions list
quiz_questions = [
    {
        "question": "Which programming language is known for its snake logo?",
        "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
        "correct_answer": "B"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "A. Hyper Text Markup Language",
            "B. High Tech Machine Language",
            "C. Hyperlink Text Making Language",
            "D. Home Tool Markup Language"
        ],
        "correct_answer": "A"
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["A. Apple", "B. IBM", "C. Microsoft", "D. Google"],
        "correct_answer": "C"
    }
]

# Function to calculate and display the result
def show_result(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"\nFinal Score: {score}/{total_questions} ({percentage:.2f}%)")
    if percentage >= 50:
        print("🎉 You passed the quiz!")
    else:
        print("😞 You failed the quiz. Try again!")

# Main quiz loop
score = 0
for item in quiz_questions:
    print("\n" + item["question"])
    for opt in item["options"]:
        print(opt)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    if user_answer == item["correct_answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is {item['correct_answer']}.")

# Show final result
show_result(score, len(quiz_questions))