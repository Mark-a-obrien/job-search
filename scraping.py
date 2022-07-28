import requests
from bs4 import BeautifulSoup
   
URL = "https://weworkremotely.com/categories/remote-customer-support-jobs"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
remoteTypes=[]  # a list to store quotes

features = soup.findAll('span', attrs = {'class': 'featured'}) 
table = soup.findAll('span', attrs = {'class':'region company'}) 


def findJob(remoteLocation, role, blockedTitles=[]) :
    for a in soup.find_all('a', href=True):
        remoteType = a.parent.findAll('span', attrs = {'class': 'region company'})
        jobTitle = a.parent.findAll('span', attrs = {'class': 'title'})

        if remoteType != [] :
            remote = str(remoteType[0])[29:len(remoteType[0])-8] # formating to only show text
            job = str(jobTitle[0])[20:len(jobTitle[0])-8]
            # print("Job :", job)
            if (remote == remoteLocation and checkJobRole(role, job.lower(), blockedTitles)) : # prints the jobs in a specific remote location
                print("Job :", job)
                print("Link :","https://weworkremotely.com" + a["href"])
                print ("Location :", remote, "\n")


# finds the role searched for and filters out job titles with blocked titles "example : Manager"
def checkJobRole(roles, job, blockedTitles) :
    for i in roles :
        if i.lower() in job :
            for j in blockedTitles :
                if (j.lower() in job) :
                    return False
            return True
    return False


findJob("Anywhere in the World", ["Technical Support", "Customer Support"], ["Manager", "Director"])