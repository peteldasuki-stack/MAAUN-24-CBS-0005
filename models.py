#[span_8](start_span)from datetime import datetime[span_8](end_span)

# [span_9](start_span)Requirement: OOP Class[span_9](end_span)
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    # [span_10](start_span)Requirement: Custom behavior method[span_10](end_span)
    def check_answer(self, user_choice):
        return user_choice.lower() == self.correct_answer.lower()

# [span_11](start_span)Requirement: Data Structure (Stack for Recent Results)[span_11](end_span)
class QuizHistory:
    def __init__(self):
        self.history_stack = []

    def add_result(self, score, total):
        # [span_12](start_span)[span_13](start_span)Requirement: datetime module[span_12](end_span)[span_13](end_span)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"Score: {score}/{total} at {timestamp}"
        self.history_stack.append(entry)

    def get_recent(self):
        # [span_14](start_span)LIFO: Returns the last result added[span_14](end_span)
        return self.history_stack[-1] if self.history_stack else "No history yet"