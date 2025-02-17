

from quiz_brain import QuizBrain
from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        
        self.window=Tk()
        self.window.title("Trivia API")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        #,Score label
        self.text_score=Label(text=f"Score:0", bg=THEME_COLOR, fg="white")
        self.text_score.grid(column=1,row=0)
        #,Canvas
        self.canvas=Canvas(bg="white",width=300, height=250)
        self.question_text=self.canvas.create_text(150,125,width=250,text="Question",font=("Arial",20,"italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=25,pady=20)
        
        
        #,Buttons
        true_img=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2, pady=20)
        
        false_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2,pady=20)
        
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.text_score.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_answer(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_answer(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        
    
        