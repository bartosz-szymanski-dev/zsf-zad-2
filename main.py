import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Klient': ['BI20', 'BI13', 'BI11', 'BI7', 'BI14', 'BI17', 'BI19', 'BI16', 'BI18', 'BI8', 'BI2', 'BI15', 'BI9',
               'BI3', 'BI12', 'BI5', 'BI4', 'BI10', 'BI6', 'BI1'],
    'Sprzedaż 2021-2023': [1800, 6400, 620, 80, 1500, 19100, 1100, 200, 12300, 530, 760, 850, 840, 480, 590, 710, 580,
                           50, 350, 170],
    'Planowana sprzedaż 2024-2026': [2200, 7000, 720, 150, 2000, 32200, 1400, 340, 14800, 610, 1500, 1000, 24000, 4700,
                                     600, 800, 18200, 120, 190, 380]
}

df = pd.DataFrame(data)

df['Wzrost przychodów'] = df['Planowana sprzedaż 2024-2026'] - df['Sprzedaż 2021-2023']
df['Wzrost procentowy'] = (df['Wzrost przychodów'] / df['Sprzedaż 2021-2023']) * 100

df_sorted_total = df.sort_values(by='Wzrost przychodów', ascending=False)

df_sorted_percentage = df.sort_values(by='Wzrost procentowy', ascending=False)

greatest_potential_growth_portfolio = df_sorted_percentage.head(3)

diversified_portfolio = df[(df['Sprzedaż 2021-2023'] > 1000) & (df['Sprzedaż 2021-2023'] < 15000)].sort_values(
    by='Wzrost przychodów', ascending=False).head(3)

more_stability_portfolio = df[(df['Sprzedaż 2021-2023'] > 500) & (df['Sprzedaż 2021-2023'] < 2000)].sort_values(
    by='Wzrost przychodów', ascending=False).head(3)

fig, axes = plt.subplots(3, 2, figsize=(15, 18))

greatest_potential_growth_portfolio.plot(kind='bar', x='Klient', y=['Sprzedaż 2021-2023', 'Planowana sprzedaż 2024-2026'],
                                         ax=axes[0, 0])
axes[0, 0].set_title('Portfel o Najwyższym Potencjale Wzrostu - Przychody')
axes[0, 0].set_ylabel('Przychody (mln zł)')
greatest_potential_growth_portfolio.plot(kind='bar', x='Klient', y='Wzrost przychodów', ax=axes[0, 1])
axes[0, 1].set_title('Portfel o Najwyższym Potencjale Wzrostu - Wzrost przychodów')
axes[0, 1].set_ylabel('Wzrost przychodów (mln zł)')

diversified_portfolio.plot(kind='bar', x='Klient', y=['Sprzedaż 2021-2023', 'Planowana sprzedaż 2024-2026'],
                           ax=axes[1, 0])
axes[1, 0].set_title('Zdywersyfikowany Portfel - Przychody')
axes[1, 0].set_ylabel('Przychody (mln zł)')
diversified_portfolio.plot(kind='bar', x='Klient', y='Wzrost przychodów', ax=axes[1, 1])
axes[1, 1].set_title('Zdywersyfikowany Portfel - Wzrost przychodów')
axes[1, 1].set_ylabel('Wzrost przychodów (mln zł)')

more_stability_portfolio.plot(kind='bar', x='Klient', y=['Sprzedaż 2021-2023', 'Planowana sprzedaż 2024-2026'],
                              ax=axes[2, 0])
axes[2, 0].set_title('Portfel o Największej Stabilności - Przychody')
axes[2, 0].set_ylabel('Przychody (mln zł)')
more_stability_portfolio.plot(kind='bar', x='Klient', y='Wzrost przychodów', ax=axes[2, 1])
axes[2, 1].set_title('Portfel o Największej Stabilności - Wzrost przychodów')
axes[2, 1].set_ylabel('Wzrost przychodów (mln zł)')

plt.tight_layout()

fig.savefig('./portfel_klientow_wzrost.png')
