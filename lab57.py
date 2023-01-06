#!/usr/bin/python3

"""Module Import Challenge | Author: Mike Greene
   Code meant to slice out trivia questions and answers from a dictionary and render
   them using the Python html library."""

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
}

def main():
    question = trivia["question"]
    correct_answer = trivia["correct_answer"]
    incorrect_answers = trivia["incorrect_answers"]

    print("Welcome to Trivia Night!\n\n")
    print(question)
    print("Is it...\n")
    
    num = 1
    for answer in incorrect_answers:
        answer = html.unescape(answer)
        print(num, ") ", answer, "\n", sep="")
        num += 1

    print(num, ") ", html.unescape(correct_answer), sep="")


if __name__ == "__main__":
    main()
