import time


class Task:
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"Task named '{self.name}' is for machine learning!"
    
    def run(self, params):
        print(f"Task starts to run with params {params}...")
        time.sleep(0.5)
        print("Done!")
