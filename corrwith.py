company = df = pd.read_csv('/content/drive/MyDrive/Стажировки_ИИ/Сажировка_производители/company_ids.csv', sep = ';')
company.head(10)


matrix = company.pivot_table(index = 'user_id', values = 'raiting', columns = 'company_id')
matrix[100:200]


matrix.fillna(0, inplace = True)
matrix


fabric = matrix[5120]
fabric = fabric.dropna()
fabric.head(10)


similar_to_fabric = matrix.corrwith(fabric)
corr_fabric = pd.DataFrame(similar_to_fabric, columns = ['correlation'])
corr_fabric.dropna(inplace = True)
corr_fabric = corr_fabric.join(company['raiting'])
corr_fabric.head()