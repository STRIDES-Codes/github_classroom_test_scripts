import json
import ast

with open('pytest_class_demo.ipynb','r') as file:  
    input_data = json.load(file)

data_subset = input_data['cells']
#print(len(data_subset))
for item in data_subset:
    if "answers to Q1" in item.get("source", "")[0]:
        res = item.get("source", "")[1]
        a1 = ast.literal_eval(res.split('=')[1].strip())
        print(a1)
    if "answer to Q2" in item.get("source", "")[0]:
        res = item.get("source", "")[1]
        a2 = res.split('=')[1].strip()
        print(a2)
    if "answer to Q3" in item.get("source", "")[0]:
        res = item.get("source", "")[1]
        a3 = int(res.split('=')[1].strip())
        print(a3)
    if "answers to Q4" in item.get("source", "")[0]:
        res1 = item.get("source", "")[1]
        flight = res1.split('=')[1].strip()
        print(flight)
        res2 = item.get("source", "")[2]
        spidey = res2.split('=')[1].strip()
        print(spidey)
        res3 = item.get("source", "")[3]
        defeats_all = res3.split('=')[1].strip()
        print(defeats_all)


# content of test_class_demo.py
class TestClassDemoInstance:
    t1 = [val.lower() for val in a1]
    t2 = a2
    t3 = a3
    t4_1 = flight
    t4_2 = spidey
    t4_3 = defeats_all

    def test_one(self):
        test_list = ['star', 'bwa', 'bowtie2']
        assert all([item in test_list for item in self.t1])

    def test_two(self):
        assert self.t2.strip("'").lower() == 'australian lungfish'

    def test_three(self):
        assert self.t3 == 4

    def test_four(self):
        assert self.t4_1.strip("'").lower() == 'superman'
        assert self.t4_2.strip("'").lower() == 'spiderman'
        assert self.t4_3.strip("'").lower() == 'chuck norris'
        
