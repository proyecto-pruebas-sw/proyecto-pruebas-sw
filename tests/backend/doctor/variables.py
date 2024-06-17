import json

with open('put_data.json') as file:
    put_data = json.load(file)
    valid_doctor_put = put_data["doctors"][0]
    file.close()

with open('initial_data.json') as file:
    data = json.load(file)
    file.close()

with open('expected_data.json') as file:
    expected_data = json.load(file)
    file.close()

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

    doctor_without_experience_job_title = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("job_title")
    doctor_without_experience_job_title["experiences"] = [experience_copy]

    doctor_without_experience_institution = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("institution")
    doctor_without_experience_institution["experiences"] = [experience_copy]

    doctor_without_experience_city = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("city")
    doctor_without_experience_city["experiences"] = [experience_copy]

    doctor_without_experience_country = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("country")
    doctor_without_experience_country["experiences"] = [experience_copy]

    doctor_without_experience_start_date = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("start_date")
    doctor_without_experience_start_date["experiences"] = [experience_copy]

    doctor_without_experience_end_date = post_data["doctors"][0].copy()
    experience_copy = post_data["doctors"][0]["experiences"][0].copy()
    experience_copy.pop("end_date")
    doctor_without_experience_end_date["experiences"] = [experience_copy]

    doctor_without_education_degree = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("degree")
    doctor_without_education_degree["educations"] = [education_copy]

    doctor_without_education_institution = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("institution")
    doctor_without_education_institution["educations"] = [education_copy]

    doctor_without_education_city = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("city")
    doctor_without_education_city["educations"] = [education_copy]

    doctor_without_education_country = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("country")
    doctor_without_education_country["educations"] = [education_copy]

    doctor_without_education_start_date = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("start_date")
    doctor_without_education_start_date["educations"] = [education_copy]

    doctor_without_education_end_date = post_data["doctors"][0].copy()
    education_copy = post_data["doctors"][0]["educations"][0].copy()
    education_copy.pop("end_date")
    doctor_without_education_end_date["educations"] = [education_copy]

    doctor_with_invalid_rut = post_data["doctors"][0].copy()
    doctor_with_invalid_rut["rut"] = "123456789"

    doctor_with_invalid_email = post_data["doctors"][0].copy()
    doctor_with_invalid_email["email"] = "invalid_email.com"

    file.close()