from src.scraper import result_scrapper

# import itertools


def generate_registration_numbers(reg_year, branch_code, college_code, student_num):
    """return the all combinations of registration number:
    reg_year:[18, 19, 20, 21]
    branch_code:[101, 102, 103, 104]
    college_code:[130, 131, 132]"""

    # for reg, branch, clg, student_id in itertools.product(
    #     reg_year, branch_code, college_code, student_num
    # ):
    #     new_reg = f"{reg}{branch}{clg}{student_id:03d}"
    #     print(new_reg)
    #     print(url)

    for reg in reg_year:
        for clg in college_code:
            for branch in branch_code:
                for student_id in student_num:
                    new_reg = f"{reg}{branch}{clg}{student_id:03d}"
                    url = f"http://results.university.net/ResultsBTechBPharm8thSemPub.aspx?&RegNo={new_reg}"
                    result_scrapper(new_reg, url)
                    # result_scrapper(int(new_reg), url)
            # print("college code not available", clg)


"""The value of student_id is formatted to always have 3 digits by using the :03d syntax. This means that if student_id is less than 100, it will be padded with leading zeros to make it have 3 digits. For example, if student_id is 5, the resulting string will be 005. If student_id is 123, the resulting string will be 123."""
