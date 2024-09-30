import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def generate_grade_distribution(grades):
    plt.figure(figsize=(10, 6))
    plt.hist(grades, bins=10, edgecolor='black')
    plt.title('Grade Distribution')
    plt.xlabel('Grades')
    plt.ylabel('Frequency')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def calculate_statistics(grades):
    df = pd.DataFrame(grades, columns=['grade'])
    stats = {
        'mean': df['grade'].mean(),
        'median': df['grade'].median(),
        'std': df['grade'].std(),
        'min': df['grade'].min(),
        'max': df['grade'].max()
    }
    return stats