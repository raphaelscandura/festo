import pandas as pd

def main():
    try:
        df = pd.read_csv('products-2000000.csv')

        summary = df.groupby('Category').sum(numeric_only=True).reset_index()

        print(summary.to_dict(orient='records'))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
