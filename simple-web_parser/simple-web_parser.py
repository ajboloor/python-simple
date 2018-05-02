from requests import get
from bs4 import BeautifulSoup
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

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

#myColors = ('#eee','#c6e48b','#7bc96f','#239a3b','#196127')
myColors = ((0.8, 0.0, 0.0, 1.0), (0.0, 0.8, 0.0, 1.0), (0.0, 0.0, 0.8, 1.0), \
	 (0.0, 0.0, 0.2, 1.0), (0.0, 0.2, 0, 1.0))
#cmap = LinearSegmentedColormap.from_list('Custom', myColors, len(myColors))
#cmap = sns.cubehelix_palette(start=2.8, rot=.1, light=0.9, n_colors=3)

ax = sns.heatmap(commits_matrix, cmap='GnBu', square=True, \
	 cbar_kws={"orientation": "horizontal"},linewidth=0.5)
colorbar = ax.collections[0].colorbar
#colorbar.set_ticks([0, 1, 5])
#colorbar.set_ticklabels(['0','1+', '5+'])
ax.set_ylabel('FROM')
ax.set_xlabel('TO')
_, labels = plt.yticks()
plt.setp(labels, rotation=0)
plt.show()
