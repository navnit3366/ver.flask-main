import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter='$')
    # writer.writerow(["회사","사업자등록번호","업종","사원수(명)","매출규모(억)","주소(도로명 주소)", "웹사이트 주소", "기업소개 및 기업규모", "담당업무", "지원요건","채용인원", "제출서류", "서류제출 마감일", "기타"])
    # writer.writerow(["회사","사업자등록번호","업종","사원수(명)","매출규모(억)","주소(도로명 주소)", "웹사이트 주소", "기업소개 및 기업규모", "담당업무"])
    for job in jobs:
        writer.writerow(job)
# for job in jobs:
#     writer.writerow(list(job.values()))