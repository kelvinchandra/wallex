import json 
import re

def case2():
    data = [
        {
            "name": "JOKO",
            "year": 2009,
            "department": "IT",
            "city": "Bandung Selatan"
        },
        {
            "name": "Budi Susanto",
            "year": 1998,
            "department": "Marketing",
            "city": "Malang"
        },
        {
            "name": "Sendi",
            "year": 2000,
            "department": "Sales",
            "city": None
        },
        {
            "name": "YOKO",
            "year": 2002,
            "department": "Sales",
            "city": "Surabaya"
        },
        
    ]
    json_object = {}
    for row in data:
        department = row.get("department")
        if json_object == {}:
            json_object.update({department: [row]})
        else:
            if json_object.get(department) is not None:
                json_object.get(department).append(row)
            else:
                json_object.update({department: [row]})

    print(json_object)


##Sample Answer
# {'IT': [{'name': 'JOKO', 'year': 2009, 'department': 'IT', 'city': 'Bandung Selatan'}], 'Marketing': [{'name': 'Budi Susanto', 'year': 1998, 'department': 'Marketing', 'city': 'Malang'}], 'Sales': [{'name': 'Sendi', 'year': 2000, 'department': 'Sales', 'city': None}, {'name': 'YOKO', 'year': 2002, 'department': 'Sales', 'city': 'Surabaya'}]}


def case1():
    data = [
        "JOKO 2009IT-Bandung Selatan",
        "Budi Susanto 1998Marketing-Malang",
        "Sendi 2000Sales",
        "YOKO 2002Sales-Surabaya"
    ]
    result = []
    for row in data:
        split= row.split("-")
        regex = re.compile("([a-zA-Z]+)([0-9]+)([a-zA-Z]+)")
        test_str = str(split[0]).replace(" ", "")
        # print(test_str)
        res = regex.match(test_str).groups() 
        print(res[0])
        if len(split) > 1:
            result.append({"name":res[0], "year":res[1], "department":res[2],"city":split[1]})        
        else:
            result.append({"name":res[0], "year":res[1], "department":res[2],"city":None}) 

    print(result)

## Sample Answer
#[{'name': 'JOKO', 'year': '2009', 'department': 'IT', 'city': 'Bandung Selatan'}, {'name': 'BudiSusanto', 'year': '1998', 'department': 'Marketing', 'city': 'Malang'}, {'name': 'Sendi', 'year': '2000', 'department': 'Sales', 'city': None}, {'name': 'YOKO', 'year': '2002', 'department': 'Sales', 'city': 'Surabaya'}]

#uncomment this and run python python.py (I use python 3.7)
# case1()
# case2()