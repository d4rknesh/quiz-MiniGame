import functions as func

questions = {
    "what does CPU stand for? " :   "central processing unit", 
    "what does GPU stand for? " :   "graphics processing unit",
    "what does RAM stand for? " :   "random access memory",
    "what does PSU stand for? " :   "power supply" 
}


if __name__ == "__main__" :
    func.welcome() 
    points = func.ask_question(questions) 
    func.ending(points)
