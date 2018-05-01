from requests import get
from bs4 import BeautifulSoup
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

url = 'https://github.com/ajboloor'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

container = html_soup.find_all('svg', class_ = 'js-calendar-graph-svg')
commits = container[0].select('rect')

ctr = 0
commits_array = [0]*(len(commits))
days = [0]*(len(commits))
for commits_day in commits:
    commits_array[ctr]=commits_day['data-count']
    days[ctr] = ctr
    ctr = ctr+1

commits_matrix = np.array(commits_array[len(commits_array)-364:len(commits_array)],dtype=int)
commits_matrix = commits_matrix.reshape(7,52)
sns.heatmap(commits_matrix, cmap="GnBu", square=True)
plt.show()
