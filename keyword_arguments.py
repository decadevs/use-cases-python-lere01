# Document at least 3 use cases of the * and ** operators
import time

# a wrapper function that takes in a function and calculates the time it takes for the function to 
# run
def wrapper_function(func):

    def inner_function(*args, **kwargs):
        start_time = time.time
        func(args, kwargs)
        end_time = time.time

        total_duration = end_time - start_time
        return total_duration

    return inner_function


# a function that takes in a dictionary of patients and their records and returns a particular record
# based on the patient identity...it takes in one positional argument and one key word argument
def show_patient_records(patient_name, *, all_records = {}):
    return all_records[patient_name]



# a function that takes in different lists and zips them...it expects two positional arguments
# and one keyword argument
def get_student_profile(list_of_student_names, list_of_student_matric_no, **cgpa_list):
    student_profile = zip(list_of_student_names, list_of_student_matric_no, cgpa_list)
    return student_profile
