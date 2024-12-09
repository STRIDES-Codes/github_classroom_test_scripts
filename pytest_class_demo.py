import pathlib
import json

file = pathlib.Path("C:/Users/pinneyjj/Downloads/github_classroom_testing/gh_class_quiz_test_answered.ipynb")  
with open(file) as f:  
    input_data = f.read()

# content of test_class_demo.py
class TestClassDemoInstance:
    t1 = [val.lower() for val in a1]
    t2 = a2
    t3 = a3
    t4_1 = spidey
    t4_2 = flight
    t4_3 = defeats_all

    def test_one(self):
        test_list = ['star', 'bwa', 'bowtie2']
        assert all([item in test_list for item in self.t1])

    def test_two(self):
        assert self.t2.lower() == 'australian lungfish'

    def test_three(self):
        assert self.t3 == 4

    def test_four(self):
        assert self.t4_1.lower() == 'spiderman'
        assert self.t4_2.lower() == 'superman'
        assert self.t4_3.lower() == 'chuck norris'
        