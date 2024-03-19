from tkinter import *
root = Tk()

root.title("% Calculation")
root.geometry("600x600")

pa_grade_3_label = Label(root)
pa_grade_5_label = Label(root)
pa_grade_10_label = Label(root)

class grade_3():
    
    def __init__(self, lang_arts, maths):
        self.lang_arts = lang_arts
        self.maths = maths
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths
        tm_with_100 = total_marks * 100
        grade_3_pa = tm_with_100 / 200
        pa_grade_3_label["text"] = grade_3_pa
        
class grade_5():
    
    def __init__(self, lang_arts, maths, sst):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst
        tm_with_100 = total_marks * 100
        grade_5_pa = tm_with_100 / 300
        pa_grade_5_label["text"] = grade_5_pa
        
class grade_10():
    
    def __init__(self, lang_arts, maths, sst, foreign_lang):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        self.foreign_lang = foreign_lang
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst + self.foreign_lang
        tm_with_100 = total_marks * 100
        grade_10_pa = tm_with_100 / 400
        pa_grade_10_label["text"] = grade_10_pa
        
root.mainloop