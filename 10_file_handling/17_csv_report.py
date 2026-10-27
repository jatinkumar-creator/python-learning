import csv
from statistics import mean
from common import SCRATCH

src = SCRATCH / "marks.csv"
src.write_text("name,subject,marks\nAsha,Math,82\nAsha,Sci,90\nRavi,Math,91\n"
               "Ravi,Sci,85\nMeera,Math,77\nMeera,Sci,70\n", encoding="utf-8")

by_student = {}
with open(src, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        by_student.setdefault(row["name"], []).append(int(row["marks"]))

report = SCRATCH / "report.csv"
with open(report, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["name", "average", "best"])
    for name, marks in sorted(by_student.items()):
        w.writerow([name, round(mean(marks), 1), max(marks)])

print(report.read_text(encoding="utf-8"))