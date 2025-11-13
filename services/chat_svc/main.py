import pandas as pd

df = pd.read_excel(
    '/home/luu-quang-huy/project/chatpetro/services/chat_svc/DanhMuc_ObjectType.xlsx',
    sheet_name='OBject Type'
)


mask = df['Object type text'].str.lower() == 'Máy nén khí'.lower()
print(df[mask]['ObjectType'].iloc[0])