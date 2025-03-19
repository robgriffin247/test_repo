import httpx


def api_wan(resource='films'):
    response = httpx.get(f'https://swapi.dev/api/')
    response.raise_for_status()

    return response

if __name__ == "__main__":
    print(api_wan())