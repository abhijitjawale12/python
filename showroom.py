vehicle= input("what are u looking for bike/car:")

data= {"bike":['honda','hero','suzuki'],
       "car":['maruti','suzuki','toyota','Mahindra'],
       "company":{'honda':['shine','activa','Dio'],
                  'hero':['splender','hf dulex','yoga'],
                  'suzuki':['Access125','Burgman125','Avenis125']}}

bike = {"shine":{'price':120000,'d-date':'20/05/2024','loan':"yes,you do"},
        "Activa":{'price':70000,'d-date':'20/05/2024','loan':"yes,you do"},
         "Dio":{'price':80000,'d-date':'20/05/2024','loan':"yes,you do"}}
        

print(data[vehicle])
select_veh = input(f"which company {vehicle} are u looking for:")
print(data["company"][select_veh])
model = input(f" which model do u looking for (select_veh):")
print(bike[model])
