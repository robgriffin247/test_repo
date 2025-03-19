import sys
import httpx


def api_wan(resource='films'):
    
    resource = resource.lower()

    if resource not in ['films', 'people', 'planets', 'starships', 'vehicles', 'species']:
        raise ValueError('Resource type must be films, people, planets, starships, vehicles or species')
    
    response = httpx.get(f'https://swapi.dev/api/{resource}/')
    
    response.raise_for_status()

    return response.data

if __name__ == "__main__":
    print(api_wan(sys.argv[1]))
