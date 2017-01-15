"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main advantages are abstraction, encapsulation, and polymorphism.
   Abstraction hides the details of way the function is created from the way it
   is used. The user doesn't need to know how the function makes a square, for
   example, just that she can use that function to do so. Abstraction is achieved
   through encapsulation, which restricts access to some of the object's internal
   parts. Polymorphism reduces redundant coding by allowing different objects
   to use the same code.

2. What is a class?
    A class defines a type of data and contains attributes and methods.

3. What is an instance attribute?
    This is a property an instance. This property applies to that instance but
    not to the class as a whole.

4. What is a method?
    This is a type of function that belongs to a class and works within that
    class. It can only be called through an instance or subclass.

5. What is an instance in object orientation?
    An instance is an object created within a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a property that everthing in the class is given. I.e,
   If our class were dogs, an attribute could be that they eat meat. An
   instance attribute is a property of that instance and does not
   apply to the class as a whole. So an instance might be a specific dog which
   could be given the attribute of eating peanut butter. Not all dogs eat
   peanut butter, but this particular one does.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = None


class Question(object):
    """A Question"""

    def __init__(self, question, correct_answer):
        """Initialize question attributes"""

        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        """Returns the question and answer"""

        return self.question + " " + self.correct_answer

    def ask_and_evaluate(self):
        """Takes a question and answer"""

        user_answer = raw_input(self.question + " >")
        return user_answer == self.correct_answer


class Exam(object):
    """An Exam"""

    def __init__(self, name):
        """Initialize exam attributes"""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Add questions to exam"""

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)

    def administer(self):
        """Ask questions and return score as %"""

        score = 0
        for each in self.questions:
            if each.ask_and_evaluate() is True:
                score += 1
        return float(score) * 100.0 / len(self.questions)


class Quiz(Exam):
    """A quiz is a pass/fail type of exam"""

    def administer(self):
        """Determine if score is pass or fail"""

        quiz_score = super(Quiz, self).administer()
        return quiz_score >= 50.0


def take_test(exam, student):
    """Take test and assign score to student"""

    score = exam.administer()
    student.score = score
    print student.first_name + " " + student.last_name + "'s score is: " + str(score)


def example():
    """Creates exam and administers test for student"""

    sample_exam = Quiz("Exam's Name")

    sample_exam.add_question("What is 3 + 2?", "5")
    sample_exam.add_question("What is 3 + 3?", "6")
    sample_exam.add_question("What is 3 + 4?", "7")

    example_student = Student("Bob", "Smith", "San Francisco")

    take_test(sample_exam, example_student)