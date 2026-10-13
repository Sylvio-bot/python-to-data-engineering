students = [
    {
        "name" : "Sylvio",
        "house" : "SoaTsiadiana",
        "patronus" : "otter"
    } ,  
    {

        "name" : "Rasoa",
        "house" : "chicago",
        "patronus" : "Stag"
    },
    {
        "name" : "Harry",
        "house" : "USA",
        "patronus" : "otter"
    },
    {
        "name" : "Draco",
        "house" : "London",
        "patronus" : None # it means absent a value  
    }
]

for student in students:
    print(student["name"], student['house'])
