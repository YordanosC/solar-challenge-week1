import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Load and combine cleaned datasets."""
    benin_df = pd.read_csv('./notebooks/data/benin_clean.csv')
    sierra_leone_df = pd.read_csv('./notebooks/data/sierraleone-bumbuna_clean.csv')
    togo_df = pd.read_csv('./notebooks/data/togo-dapaong_qc_clean.csv')
    
    benin_df['Country'] = 'Benin'
    sierra_leone_df['Country'] = 'Sierra Leone'
    togo_df['Country'] = 'Togo'
    
    return pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)

def create_boxplot(df, metric, countries):
    """Create a boxplot for the specified metric."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='Country', y=metric, data=df, hue='Country', ax=ax)
    ax.set_title(f'{metric} by Country')
    return fig

def create_summary_table(df, countries):
    """Create a summary table for selected countries."""
    metrics = ['GHI', 'DNI', 'DHI']
    summary_data = []
    
    for metric in metrics:
        for country in countries:
            country_data = df[df['Country'] == country][metric]
            summary_data.append({
                'Country': country,
                'Metric': metric,
                'Mean': round(country_data.mean(), 2),
                'Median': round(country_data.median(), 2),
                'Std': round(country_data.std(), 2)
            })
    
    return pd.DataFrame(summary_data).pivot(index='Metric', columns='Country', values=['Mean', 'Median', 'Std'])