import requests as rqst
from bs4 import BeautifulSoup as bs
from utils.mongo_utils import find_update_existing_result
from src.csv_maker import csv_file_maker
import logging
from datetime import date
import datetime

logger = logging.getLogger(__name__)


def result_scrapper(RegistrationNo, url):
    """
    This function scrap the data from webpage using BeautifulSoup4
    """
    web = rqst.get(url)
    # print(url)

    soup = bs(web.content, "html.parser")
    status = soup.find("table", {"id": "ctl00_ContentPlaceHolder1_DataList4"})

    if str(status) != "None":
        # print("okk")
        Student_Name = soup.find(
            "span", {
                "id": "ctl00_ContentPlaceHolder1_DataList1_ctl00_StudentNameLabel"}
        ).text
        College_Name = soup.find(
            "span", {
                "id": "ctl00_ContentPlaceHolder1_DataList1_ctl00_CollegeNameLabel"}
        ).text
        College_Code = soup.find(
            "span", {
                "id": "ctl00_ContentPlaceHolder1_DataList1_ctl00_CollegeCodeLabel"}
        ).text
        Course_Code = soup.find(
            "span", {
                "id": "ctl00_ContentPlaceHolder1_DataList1_ctl00_CourseCodeLabel"}
        ).text
        Course_Name = soup.find(
            "span", {"id": "ctl00_ContentPlaceHolder1_DataList1_ctl00_CourseLabel"}
        ).text

        SEM_SGPA = soup.find(
            "table", {"id": "ctl00_ContentPlaceHolder1_GridView3"})

        SEM_values = []
        for td in SEM_SGPA.find_all("td"):
            CGPA_SGPA = td.text.strip()
            SEM_values.append(CGPA_SGPA)

        Student = {
            "Student Name": Student_Name,
            "Branch": Course_Name,
            "Registration No": RegistrationNo,
            "College": College_Name,
            "College Code": College_Code,
            "Course Code": Course_Code,
            "SEM I": SEM_values[0],
            "SEM II": SEM_values[1],
            "SEM III": SEM_values[2],
            "SEM IV": SEM_values[3],
            "SEM V": SEM_values[4],
            "SEM VI": SEM_values[5],
            "SEM VII": SEM_values[6],
            "SEM VIII": SEM_values[7],
            "CGPA": SEM_values[-1],  # Current CGPA at End of the Table
            "createdAt": datetime.datetime.now(),
            "updatedAt": datetime.datetime.now(),
        }
        print(Student)
        find_update_existing_result(RegistrationNo, Student)
        # store data in csv
        csv_file_maker(Student, RegistrationNo)
    else:
        logger.info(f"Result Unavailable: {RegistrationNo}")
