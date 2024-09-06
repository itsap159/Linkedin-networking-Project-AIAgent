from tavily import TavilyClient
import os
def get_profile_url(name: str):
    """ Searches for linkedin profile page"""
    tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
    query = f"Here is the name and information about the person :- {name}. Find the linkedin profile page of the person with the given name and given information. Make sure the url is a linkedin profile page of the person and not 'https://www.linkedin.com/pub/dir/' and the url should have 'linkedin' in it."
    response = tavily_client.search(query)
    print("Hi")
    print('Tavily response', response)
    return response['results'][0]['url']


if __name__ == '__main__':
    ans = get_profile_url('AmanParikh','Studied at University of California San Diego')
    print(ans)



