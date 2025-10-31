def read_expenses(filename):
    records=[]
    try:
        with open(filename,'r') as f:
   
            for line in f:
                line=line.strip()
                if not line:
                    continue
                parts=line.split(',')
                if(len(parts)!=3):
                    print("Miss fields",line)
                    continue
                date,category,amount_str=parts
                try:
                    amount=int(amount_str)
                except ValueError:
                    print("invalid amount",amount_str)
                    continue
                records.append((date,category,amount))
    except FileNotFoundError:
        print("file not found",filename)
        return[]
    return records
def calculate_summary(records):
    total=0
    category_totals={}
    day_total={}
    for date,category,amount in records:
        total=total+amount
        category_totals[category]=category_totals.get(category,0)+amount
        day_total[date]=day_total.get(date,0)+amount
    if day_total:
        high_spent=max(day_total,key=day_total.get)
        highest_amount=day_total[high_spent]
    else:
        high_spent,highest_amount=None,0
    return{
        "total":total,
        "category_totals":category_totals,
        "highest_day":high_spent,
        "highest_amount":highest_amount,
    }
def write_summary(summary,filename):
    with open(filename,'w') as f:
        f.write(f"================= Expense Summary (October 2025) =================\n")
        f.write(f"Total Monthly Expense: {summary['total']}\n")
        f.write(f"Category-wise Breakdown:\n")
        for category,total in summary["category_totals"].items():
            f.write(f"{category} : {total}\n")
        f.write("\n")
        if summary["highest_day"]:
            f.write(f"Highest Spenting day: {summary['highest_day']}({summary['highest_amount']})\n")
        f.write("===============================================================\n")
        print(f"Monthly summary saved to '{filename}' successfully!")
def main():
    input_file="expenses.csv"
    output_file="monthly_summary.txt"
    records=read_expenses(input_file)
    if not records:
        print("no valid records found")
        return
    summary=calculate_summary(records)
    write_summary(summary,output_file)
if __name__ =='__main__':
    main()




    

        






            
                


            
        
