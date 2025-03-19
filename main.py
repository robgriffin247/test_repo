import httpx


def api_wan(resource='films'):
    response = httpx.get(f'https://swapi.py4e.com/api/{resource}')

    response.raise_for_status()
    
    return response

if __name__ == "__main__":
    print(api_wan())