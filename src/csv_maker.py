from csv import DictWriter
import os


def csv_file_maker(student, reg):
    """_summary_

    Args:
        student (_type_): _description_
        reg (_type_): _description_
    """
    Student = student
    RegistrationNo = str(reg)
    header = [
        "Student Name",
        "Registration No",
        "Branch",
        "College",
        "College Code",
        "Course Code",
        "SEM I",
        "SEM II",
        "SEM III",
        "SEM IV",
        "SEM V",
        "SEM VI",
        "SEM VII",
        "SEM VIII",
        "CGPA",
        "createdAt",
        "updatedAt",
    ]

    # custom file name for seperate csv files
    reg_num = RegistrationNo
    clg_code = reg_num[5:8]
    branch_code = reg_num[2:5]
    csv_folder = f"Results/{reg_num[0:2]}_CLG_{clg_code}_{branch_code}.csv"

    # check file does exist or not
    file_exists = os.path.isfile(csv_folder)
    # if not os.path.exists(csv_folder):
    #     os.makedirs(csv_folder)

    # try:
    with open(csv_folder, "a") as csvfile:
        writer = DictWriter(csvfile, fieldnames=header)
        # write header once only when file does not exist
        if not file_exists:
            writer.writeheader()
        # if file does exist then write the content, not the header
        writer.writerow(Student)
    # except IOError:
    #     print("I/O error")
