import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Data Inspection",df.head())

# Jumlah Pegawai IBM
jumlah = df.shape[0]
print("Jumlah Pegawai: ",jumlah)


print("Missing Value Analysis",df.info())

print("Missing Value Analysis",df.isnull().sum())

# menampilkan daftar tipe data dari dataframe
cols = list(df.dtypes.apply(lambda x: x.name).unique())
cols

# mengubah tipe data kolom ke string
df[['Department','EnvironmentSatisfaction','JobInvolvement','JobLevel','JobSatisfaction','PerformanceRating','RelationshipSatisfaction','WorkLifeBalance']] = df[['Department','EnvironmentSatisfaction','JobInvolvement','JobLevel','JobSatisfaction','PerformanceRating','RelationshipSatisfaction','WorkLifeBalance']].astype('str')

# statistik kolom numerik
print("Statistik Deskriptif Numerik",df.describe().T)

# statistik kolom non numerik
print("Statistik Deskriptif Non Numerik",df.describe(include=['object']).T)

# Jumlah kolom kategori
cat_columns = list(df.select_dtypes(include='object').columns)
n = len(cat_columns)
print("Kolom Categorical",cat_columns)
print("Jumlah Kolom Categorical: ",n)

# Hitung ukuran grid yang pas
print("Batch Visualization of Categorical Distributions via Subplots")
n_cols = 3  # Misal 3 kolom
n_rows = (n + n_cols - 1) // n_cols  # Pembulatan ke atas

# Buat subplot
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * 5, n_rows * 4))
axes = axes.flatten()  # Ubah ke array 1D agar mudah di-loop

# Loop dan plot
for i, col in enumerate(cat_columns):
    df[col].value_counts().plot(kind='bar', ax=axes[i], title=col)
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Jumlah')
    axes[i].tick_params(axis='x', rotation=90)

# Hapus axis sisa jika jumlah kolom tidak pas
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# Jumlah Kolom Numerik
num_columns = list(df.select_dtypes(include=['int64', 'float64']).columns)
n = len(num_columns)
print("Kolom Numerikal",num_columns)
print("Jumlah Kolom Numerikal: ",n)

print("Batch Visualization of Numerical Distributions via Subplots")
n_cols = 4  # Misal 3 kolom
n_rows = (n + n_cols - 1) // n_cols  # Pembulatan ke atas

# Buat subplot
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * 5, n_rows * 4))
axes = axes.flatten()  # Ubah ke array 1D agar mudah di-loop

# Loop dan plot
for i, col in enumerate(num_columns):
    df[col].plot(kind='hist', ax=axes[i], title=col)
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Jumlah')
    axes[i].tick_params(axis='x', rotation=90)

# Hapus axis sisa jika jumlah kolom tidak pas
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# List untuk menyimpan tiap dataframe
tabel_kategori = []

for col in cat_columns:
    df_temp = df[col].value_counts().reset_index().rename(columns={
        'index': f'Nilai Unik ({col})',
        col: 'Jumlah'
    })
    # Sisipkan nama kolom & jumlah nilai unik sebagai metadata (optional)
    print(f"\n📌 Kolom: {col}  — Jumlah nilai unik: {df[col].nunique()}")
    display(df_temp)  # Jika pakai Jupyter, tampil sebagai tabel
    tabel_kategori.append((col, df_temp))