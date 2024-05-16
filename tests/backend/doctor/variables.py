import json

with open('initial_data.json') as file:
    data = json.load(file)

with open('post_data.json') as file:
    post_data = json.load(file)

    valid_doctor = post_data["doctors"][0]

    doctor_without_name = post_data["doctors"][0].copy()
    doctor_without_name.pop("name")

    doctor_without_lastname = post_data["doctors"][0].copy()
    doctor_without_lastname.pop("lastname")

    doctor_without_rut = post_data["doctors"][0].copy()
    doctor_without_rut.pop("rut")

    doctor_without_city = post_data["doctors"][0].copy()
    doctor_without_city.pop("city")

    doctor_without_specialties = post_data["doctors"][0].copy()
    doctor_without_specialties["specialties"] = []

    '''
    doctor_without_experience_job_title = post_data["doctors"][0].copy()
    doctor_without_experience_job_title["experiences"][0].pop("job_title")

    doctor_without_experience_institution = post_data["doctors"][0].copy()
    doctor_without_experience_institution["experiences"][0].pop("institution")

    doctor_without_experience_city = post_data["doctors"][0].copy()
    doctor_without_experience_city["experiences"][0].pop("city")

    doctor_without_experience_country = post_data["doctors"][0].copy()
    doctor_without_experience_country["experiences"][0].pop("country")

    doctor_without_experience_start_date = post_data["doctors"][0].copy()
    doctor_without_experience_start_date["experiences"][0].pop("start_date")

    doctor_without_experience_end_date = post_data["doctors"][0].copy()
    doctor_without_experience_end_date["experiences"][0].pop("end_date")
    
    doctor_without_education_degree = post_data["doctors"][0].copy()
    doctor_without_education_degree["educations"][0].pop("degree")

    doctor_without_education_institution = post_data["doctors"][0].copy()
    doctor_without_education_institution["educations"][0].pop("institution")

    doctor_without_education_city = post_data["doctors"][0].copy()
    doctor_without_education_city["educations"][0].pop("city")

    doctor_without_education_country = post_data["doctors"][0].copy()
    doctor_without_education_country["educations"][0].pop("country")

    doctor_without_education_start_date = post_data["doctors"][0].copy()
    doctor_without_education_start_date["educations"][0].pop("start_date")

    doctor_without_education_end_date = post_data["doctors"][0].copy()
    doctor_without_education_end_date["educations"][0].pop("end_date")
'''
'''
# print all
print(data)
print(post_data)
print(doctor_without_name)
print(doctor_without_lastname)
print(doctor_without_rut)
print(doctor_without_city)
print(doctor_without_specialties)

print(doctor_without_experience_job_title)
print(doctor_without_experience_institution)
print(doctor_without_experience_city)
print(doctor_without_experience_country)
print(doctor_without_experience_start_date)
print(doctor_without_experience_end_date)
print(doctor_without_education_degree)
print(doctor_without_education_institution)
print(doctor_without_education_city)
print(doctor_without_education_country)
print(doctor_without_education_start_date)
print(doctor_without_education_end_date)

'''