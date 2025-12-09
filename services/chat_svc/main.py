import pandas as pd

# df = pd.read_excel(
#     '/home/luu-quang-huy/project/chatpetro/services/chat_svc/DanhMuc_ObjectType.xlsx',
#     sheet_name='OBject Type'
# )
# mask = df['Object type text'].str.lower() == 'Máy nén khí'.lower()
# print(df[mask]['ObjectType'].iloc[0])


df = pd.read_excel(
    '/home/luu-quang-huy/project/chatpetro/services/chat_svc/chat_svc/data/common_question.xlsx',
)

df.dropna(how='all', inplace=True)

df['group'] = df['CÂU HỎI (INPUT)'].notna().cumsum()

# Forward-fill trong từng nhóm
df['CÂU HỎI (INPUT)'] = df.groupby('group')['CÂU HỎI (INPUT)'].ffill()

# Xóa cột nhóm phụ
df.drop(columns=['group'], inplace=True)

print(df)
