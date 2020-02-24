import pandas as pd

EXCEL_PATH = "D:/000_WORK/DeepCpf1/41587_2018_BFnbt4061_MOESM39_ESM - 복사본.xlsx"
# EXCEL_PATH = "D:/000_WORK/DeepCpf1/41587_2018_BFnbt4061_MOESM39_ESM_test.xlsx"
SHEET_NAME = "Data set HT 1-1"
INPUT_PATH = "D:/000_WORK/DeepCpf1/input.txt"
OUTPUT_PATH = "D:/000_WORK/DeepCpf1/output.txt"

df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

with open(INPUT_PATH,"a") as f:
    i = 1
    for cella in df['a'].values:
        if not isinstance(cella, str):
            break
        f.write(str(i) + " " + str(cella) + " 0 " + "\n")
        i = i + 1

with open(OUTPUT_PATH,"a") as f:
    i = 1
    for cella , cellb , cellc in df[['a','b','c']].values:
        if not isinstance(cella, str):
            break
        f.write(str(i) + " " + str(cella) + " 0 " + str(cellb) + " " + str(cellc) + "\n")
        i = i + 1

# for cell in df['a'].values:
#     print(cell)
# df[['a','b']].to_csv(path_or_buf=RESULT_PATH,index=True,sep=" ", header=False,mode="w")

