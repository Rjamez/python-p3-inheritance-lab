#!/usr/bin/env python

from user import User

class Student(User):  
    def __init__(self, first_name, last_name):  
        super().__init__(first_name, last_name)  # Initialize the User part  
        self.knowledge = []  # Empty list for student's knowledge  

    def learn(self, info):  
        self.knowledge.append(info)  # Add the learned string to knowledge