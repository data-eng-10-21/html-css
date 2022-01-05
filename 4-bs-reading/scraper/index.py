# Import necessary libraries
import requests
from src.adapters.indeed_client import get_job_cards
from src.adapters.indeed_adapter import IndeedAdapter


header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

technologies = ['2 years', '1 year', '3 years', '5 years', '7 years', 'AWS', 'Airflow', 'Alteryx', 'Azure', 'Bayes', 'BigQuery', ' C ', 'C#', 'C++', 'Caffe', 'Calculus', 'Cassandra', 'D3', 'Communication', 'Databricks', 'Django', 'Data Lake', 'Data Pipeline', 'Deep Learning', 'Docker', 'Excel', 'ETL', 'EMR', 'Fastai', 'Flask', 'GCP', 'Git', 'Google Cloud', 'Hadoop', 'Hbase', 
 'Hive','Java', 'Javascript','Kafka', 'Keras', 'Kubernetes', 'KPI',  'Linux', 'Matlab', 'MongoDB','Masters', 'MySQL', 'Linear Algebra', 'Metric', 'Natural Language Processing', 'Neural Networks', 'NLP', 'NoSQL','NumPy', 'OOP', 'Object Oriented', 'Probability', 'Pandas', 'Perl', 'Phd',  'Pig', 'Project Management', 'PyTorch', 'Pyspark', 'Python', 'Random Forests', ' R ', 'Regression', 'Redshift', 'SAS', 'Sklearn', 'SPSS', 'SQL', 'Scala', 'Scikit', 'Shell', 'Spark', 'Spacy', 'Stakeholder', 'Statistics', 'Tableau', 'Testing', 'test driven', 'TDD',
 'TensorFlow', 'postgresql', 'Visualization', 'XGboost', 'Catboost', 'Kaggle']

def run():
    cards = get_job_cards()
    position_infos = []
    for card in cards:
        adapter = IndeedAdapter(card)
        position_info = adapter.run()
        position_infos.append(position_info)
    return position_infos

def run_once():
    cards = get_job_cards()
    card = cards[0]
    adapter = IndeedAdapter(card)
    position_info = adapter.run()
    return position_info