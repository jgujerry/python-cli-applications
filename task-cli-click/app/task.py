import time


class Task:
    
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f"Task named '{self.name}' is for machine learning!"
    
    def run(self):
        print("Task starts to run...")
        print(time.sleep(1))
        print("Done!")
