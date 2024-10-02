import os
import subprocess
import sys


def run_pylint(file_path):
    """Run pylint on the given Python file and return the result."""
    try:
        # Find the full path to pylint in the virtual environment
        pylint_path = os.path.join(os.path.dirname(sys.executable), 'pylint')

        # Running pylint on the file
        result = subprocess.run([pylint_path, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running pylint: {str(e)}"
def analyze_python_file(file_path):
    """Analyzes the given Python file for code quality."""
    if not os.path.exists(file_path):
        return "File does not exist."
    if not file_path.endswith('.py'):
        return "Not a Python file."

    print(f"Analyzing {file_path}...\n")
    # Running pylint on the file
    pylint_result = run_pylint(file_path)

    # Displaying pylint feedback
    if pylint_result:
        return f"Pylint Feedback:\n{pylint_result}"
    else:
        return "No issues detected."


def main():
    print("Welcome to the AI-Powered Code Review Bot!")

    # Example: Change the path to any Python file you'd like to analyze
    file_to_review = input("Enter the path to the Python file you want to review: ")

    # Analyze the file
    review_result = analyze_python_file(file_to_review)

    # Output the result
    print(f"\nReview Result:\n{review_result}")


if __name__ == "__main__":
    main()
