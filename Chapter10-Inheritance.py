############################## Inheritance  ##########################
###################### Example 1 ########################
##
# This module defines a hierarhy of classes that model exam questions
#

## A question with a text and an answer
#
# class Question:
#     ## Constructs a question with empty question and answer strings
#     #
#     def __init__(self):
#         self._text = ""
#         self._answer = ""
#     ## Sets the question text
#     # @param questionText the text of this question
#     #
#     def setText(self, questionText):
#         self._text = questionText
#
#     ## Sets the answer for this question
#     # @param correctResponse the answer
#     #
#     def setAnswer(self, correctResponse):
#         self._answer = correctResponse
#
#     ## Checks a given response for correctness
#     # @param response the response to check
#     # @return True if the response was correcr, False otherwise
#     def checkAnswer(self, response):
#         return response == self._answer
#
#     # Display this question
#     #
#     def display(self):
#         print(self._text)


## A question with multiple choice. A subclass of Question
#
# class ChoiceQuestion(Question):
#     # Constructs a choice question with no choice
#     def __init__(self):
#         super().__init__()
#         self._choices = []
#
#     # Adds an  answer choice to this question
#     # @param choice the choice to add
#     # @param correct True if this is the correct choice, False otherwise
#     def addChoice(self, choice, correct):
#         self._choices.append(choice)
#         if correct:
#             # convert length of choice list to string
#             choicestr = str(len(self._choices))
#             self.setAnswer(choicestr)
#     # Override the method Question.display()
#     def display(self):
#         # display the question text
#         super().display()
#
#         # display answer choices
#         for i in range(len(self._choices)):
#             choiceNumber = i+1
#             print("%d : %s" %(choiceNumber, self._choices[i]))
#

### testing inheritance
# def main():
#     first = ChoiceQuestion()
#     first.setText("In what year was the Python language first released?")
#     first.addChoice("1991", True)
#     first.addChoice("1995", False)
#     first.addChoice("1998", False)
#     first.addChoice("2000", False)
#
#     second = ChoiceQuestion()
#     second.setText("In which country was the inventor of Python born?")
#     second.addChoice("Australia", False)
#     second.addChoice("Canada", False)
#     second.addChoice("Netherlands", True)
#     second.addChoice("United states", False)
#
#     presentquestion(first)
#     presentquestion(second)
#
#
# def presentquestion(q):
#     q.display()
#     response1 = input("Your answer:")
#     print(q.checkAnswer(response1))
#
#
# main()


# ### Testing polymorphism
# def main():
#     first = Question()
#     first.setText("Who is the inventor of Python")
#     first.setAnswer("Guido van Rossum")
#
#     second = ChoiceQuestion()
#     second.setText("In which country was the inventor of Python born?")
#     second.addChoice("Australia", False)
#     second.addChoice("Canada", False)
#     second.addChoice("Netherlands", True)
#     second.addChoice("United states", False)
#
#     presentquestion(first)
#     presentquestion(second)
#
#
# def presentquestion(q):
#     q.display()
#     response1 = input("Your answer:")
#     print(q.checkAnswer(response1))
#
#
# main()

# ## Test the Question class
# # Create question and expected answer
#
# q = Question()
# q.setText("Who is the inventor of Python")
# q.setAnswer("Guido van Rossum")
#
# # Display the question and obtain user's response
# q.display()
# response = input("Your answer")
# print(q.checkAnswer(response))

###################### Abstarct class ######################
# python doesn't provide any abstract class on its own.
# # You need to use built in module for python to create abtract class
#
# class Shape:
#     def area(self): pass
#
#     def perimeter(self): pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.__side = side
#
# obj1 = Shape()


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

#obj1 = Shape()  ## Error: cannot instantiate abstract class

square_object = Square(5)
print(square_object.area())
print(square_object.perimeter())