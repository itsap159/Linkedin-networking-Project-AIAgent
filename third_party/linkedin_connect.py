import os
import requests

from dotenv import load_dotenv

load_dotenv()

def get_profile(linkedin_profile: str='x', stored: bool = True):
    """ Get the information from Linkedin for the likedin profile provided"""

    if stored:
        linkedin_profile = "https://gist.githubusercontent.com/itsap159/afde6245456075f3a468282785605e22/raw/c08d540a8ff31ffad2a1d59be2b642e62ff663ca/file1.json"
        response = requests.get(
            linkedin_profile
        )
    else:

        headers = {'Authorization': f'Bearer {os.getenv("proxyurl_api_key")}'}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
        'linkedin_profile_url': linkedin_profile,
        }
        response = requests.get(
            api_endpoint,
            params = params,
            headers = headers)

    data = response.json()

    data = {
        k : v
        for k,v in data.items()
        if v not in ([],"",'',None)
           and k not in ["people_also_viewed","certifications"]

    }
    if 'groups' in data:
        for all in data['groups']:
            all.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        get_profile()
    )


