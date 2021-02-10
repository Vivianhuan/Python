#At first we import the requests module. Next we store the URL of the API
#call in the url variable. GitHub is currently on the third version of 
#its API, so we define headers for the API call w that ask explicitly to 
#use this version of the API. Then we use requests to make the call to 
#the API x. We call get() and pass it the URL and the header that we 
#defined, and we assign the response object to the variable r. The 
#response object has an attribute called status_code, which tells us 
#whether the request was successful. (A status code of 200 indicates a 
#successful response.) At y we print the value of status_code so we can 
#make sure the call went through successfully. The API returns the 
#information in JSON format, so we use the json() method to convert the 
#information to a Python dictionary z. We store the resulting dictionary 
#in response_dict.

import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3_json'}
r = requests.get(url,headers = headers)
print(f"Status code: {r.status_code}")

# Store API reponse in a variable. 
response_dict = r.json()
# Process results.
print(response_dict.keys())


print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositoris. 
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")


### Examin the first repository. ###
#repo_dict=repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted (repo_dict.keys()):
#	print(key)

#print("\nSelected information about first repository:")
#print(f"Name: {repo_dict['name']}")
#print(f"Owner: {repo_dict['owner']['login']}")
#print(f"Stars: {repo_dict['stargazers_count']}")
#print(f"Repository: {repo_dict['html_url']}")
#print(f"Created: {repo_dict['created_at']}")
#print(f"Updated: {repo_dict['updated_at']}")
#print(f"Description: {repo_dict['description']}")	

### Summarizing the Top Repositories.###

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")	

from plotly.graph_objs import Bar
from plotly import offline

repo_names, stars, labels, repo_links = [],[],[],[]
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

	owner = repo_dict['owner']['login']
	description= repo_dict['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)

# Make visulization
data = [{
	'type':'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker':{
		'color':'rgb(60,100,150)',
		'line':{'width':1.5,'color':'rgb(25,25,25)'}
	},
	'opacity': 0.6,
}]	

my_layout ={
	'title': 'Most-Starred Python Projects on Github',
	'titlefont': {'size': 28},
	'title_x': 0.5,
	'xaxis':{
		'title':'Repository',
		'titlefont': {'size': 20},
		'tickfont':{'size':14}
		},
	'yaxis':{
		'title':'Stars',
		'titlefont': {'size': 20},
		'tickfont':{'size':14}
		},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')



 


