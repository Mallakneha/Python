def read_marks(filename):
    students={}

    with open(filename,'r') as f:
        next(f)
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(',')
            if len(parts)!=4:
                print("Skipping malformed line:", line)
                continue
            id,name,subject,marks=parts
            id=int(id)
            marks=int(marks)
            if id not in students:
                students[id]={
                "name":name,
                "subjects":{}
                }
            students[id]["subjects"][subject]=marks
    return students
def generate_report(students):
    report=[]
    for sid,info in students.items():
        subjects=info["subjects"]
        total=sum(subjects.values())
        average=total/len(subjects)
        highest_sub=max(subjects,key=subjects.get)
        lowest_sub=min(subjects,key=subjects.get)
        report.append({
            "id": sid,
            "name": info["name"],
            "total": total,
            "average": average,
            "highest": (highest_sub,subjects[highest_sub]),
            "lowest": (lowest_sub,subjects[lowest_sub]),
        })
    report.sort(key=lambda x:x["average"] ,reverse=True)
    return report
def write_summary(report,filename):
    with open(filename,"w") as f:
        for student in report:
            f.write(f"Student Id: {student['id']}\n")
            f.write(f"Name:{student['name']}\n ")
            f.write(f"Total marks: {student['total']}\n")
            f.write(f"Average marks: {student['average']}\n")
            f.write(f"Highest Scored Subject: {student['highest'][0]} ({student['highest'][1]})\n")
            f.write(f"Lowest Scored Subject: {student['lowest'][0]} ({student['highest'][1]})\n")
            f.write("--------------------------------------------\n")
def main():
    input_file="marks.txt"
    output_file="report.txt"
    data=read_marks(input_file)
    if not data:
        print("No data found")
        return
    report=generate_report(data)
    write_summary(report,output_file)
    print("Report generated sucessfully ! Check 'report.txt'")
if __name__=="__main__":
    main()

   



                  
