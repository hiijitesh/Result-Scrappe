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
    college_code_list = [
        102,
        103,
        106,
        107,
        108,
        109,
        110,
        111,
        113,
        115,
        117,
        118,
        119,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        136,
        139,
        140,
        141,
        142,
        144,
        145,
        146,
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        154,
        155,
        156,
        157,
        158,
        159,
        165,
    ]

    for reg in reg_year:
        for clg in college_code:
            # if clg in college_code_list:
            for branch in branch_code:
                for student_id in student_num:
                    new_reg = f"{reg}{branch}{clg}{student_id:03d}"
                    url = f"http://results.university.net/ResultsBTechBPharm8thSemPub.aspx?&RegNo={new_reg}"
                    result_scrapper(new_reg, url)
                    # result_scrapper(int(new_reg), url)
            # print("college code not available", clg)


"""The value of student_id is formatted to always have 3 digits by using the :03d syntax. This means that if student_id is less than 100, it will be padded with leading zeros to make it have 3 digits. For example, if student_id is 5, the resulting string will be 005. If student_id is 123, the resulting string will be 123."""


def get_college_name(collge_code):
    """_summary_

    Args:
        collge_code (int): get college code

    Returns:
        string: college name
    """
    college_data = {
        "102": "Vidya Vihar Institute of Technology, Purnia",
        "103": "Netaji Subhash Institute of Technology, Patna",
        "106": "Sityog Institute of Technology, Aurangabad",
        "107": "Muzaffarpur Institute of Technology, Muzaffarpur",
        "108": "Bhagalpur College of Engineering, Bhagalpur",
        "109": "Nalanda College of Engineering, Nalanda",
        "110": "Gaya College of Engineering, Gaya",
        "111": "Darbhanga College of Engineering, Darbhanga",
        "113": "Motihari College Of Engineering, Mothihari",
        "115": "Azmet Institute of Technology, Kishanganj",
        "117": "Lok Nayak Jai Prakash Institute of Technology, Chhapra",
        "118": "Buddha Institute of Technology, Gaya",
        "119": "Adwaita Mission Institute of Technology, Banka",
        "121": "Moti Babu Institute of Technology, Forbesganj",
        "122": "Exalt College of Engineering & Technology, Vaishali",
        "123": "Siwan Engineering & Technical Institute, Siwan",
        "124": "Sershah Engineering College, Sasaram, Rohtas",
        "125": "Rashtrakavi Ramdhari Singh Dinkar College of Engineering, Begusarai",
        "126": "Bakhtiyarpur College of Engineering, Patna",
        "127": "Sitamarhi Institute of Technology, Sitamarhi",
        "128": "B.P. Mandal College of Engineering, Madhepura",
        "129": "Katihar Engineering of College, Katihar",
        "130": "Supaul College of Engineering, Supaul",
        "131": "Purnea College of Engineering, Purnea",
        "132": "Saharsa College of Engineering, Saharsa",
        "133": "Government Engineering College, Jamui",
        "134": "Government Engineering College, Banka",
        "135": "Government Engineering College, Vaishali",
        "136": "Mother's Institute of Technology, Bihta, Patna",
        "139": "R.P. Sharma Institute of Technology, Patna",
        "140": "Maulana Azad College of Engineering & Technology, Patna",
        "141": "Government Engineering College, Nawada",
        "142": "Government Engineering College, Kishanganj",
        "144": "Government Engineering College, Munger",
        "145": "Government Engineering College, Sheohar",
        "146": "Government Engineering College, West Champaran",
        "147": "Government Engineering College, Aurangabad",
        "148": "Government Engineering College, Kaimur",
        "149": "Government Engineering College, Gopalganj",
        "150": "Government Engineering College, Madhubani",
        "151": "Government Engineering College, Siwan",
        "152": "Government Engineering College, Jehanabad",
        "153": "Government Engineering College, Arwal",
        "154": "Government Engineering College, Khagaria",
        "155": "Government Engineering College, Buxar",
        "156": "Government Engineering College, Bhojpur",
        "157": "Government Engineering College, Sheikhpura",
        "158": "Government Engineering College, Lakhisarai",
        "159": "Government Engineering College, Samastipur",
        "165": "Shri Phanishwar Nath Renu Engineering College, Araria",
    }
    if collge_code in college_data:
        return college_data[collge_code]
    else:
        return "College code not found."


# college_code = int(input("Enter college code: "))
# college_name = college_check(college_code)
# print(college_name)
