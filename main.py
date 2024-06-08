from encode import read_financial_data, share_data

def main():
    file_path = 'data/financial_data.xlsx'  # or 'data/financial_data.csv'
    financial_data = read_financial_data(file_path)
    employees = ["Alice", "Bob", "Charlie"]
    share_data(financial_data, employees)

if __name__ == "__main__":
    main()
