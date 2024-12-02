import plotly.express as px
import pandas as pd

def generate_report(data):
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Category', y='Count', title='Document Verification Analytics')
    fig.write_html('static/uploads/analytics_report.html')
