
"""
nested collection -> collection inside collection

eg:

list of list
data = [
    [],
    [],
    []
]

list of dictionary
data = [
    {k:v},
    {k:v},
    {k:v}
]
"""

#exampls

students=[
    {"id":1,"name":"basith","qualifiaction":"bca","colloege":"st joseph","pass_out_year":2025},
    {"id":2,"name":"abhin","qualifiaction":"btech","colloege":"ace","pass_out_year":2025},
    {"id":3,"name":"adarsh","qualifiaction":"bca","colloege":"amstk","pass_out_year":2025},
    {"id":4,"name":"aibin","qualifiaction":"btech","colloege":"mbits","pass_out_year":2024},
    {"id":5,"name":"alfiya","qualifiaction":"bsccs","colloege":"kmm","pass_out_year":2025},
]

for st in students:

    print(st.get("name"))
    
print()

for st in students:

    print(st.get("colloege"))

print()

all_students_name = [st.get("name") for st in students]

print(all_students_name)

collages = [st.get("colloege") for st in students]

print(collages)

bca_students_name = [st.get("name") for st in students if st.get("qualifiaction")=="bca"]

print(bca_students_name)

pass_out_2025 = [st.get("name") for st in students if st.get("pass_out_year")==2025]

print(pass_out_2025)
