import requests as r


def response_status():
    """
    Takes a URL string, makes a request, and returns the status code.
    This function also handles potential errors from the request.
    """

    url = input("Enter the URL to be invoked: ")

    try:
        response = r.get(url)

        status_code = response.status_code
        status = response.reason

        print('Status code : ' + str(status_code))
        print('Message : Request Fetched.')
        print('Request returned message - ' + status)


    except r.exceptions.RequestException as e:

        """
        Connection Errors :
        The server was never reached. 
        In this case, there is no response and no status code.
        """
        
        
        error_message = str(e).lower()

        if "failed to resolve" in error_message:
            print('Error : The domain name not found.')
            print('Suggestion: Please check the URL for typos.')
            
        elif "connection refused" in error_message:
            print('Error : The server refused the connection.')
            print('Suggestion: The service might be down or a firewall is blocking access.')

        elif "timed out" in error_message:
            print('Error : The request timed out.')
            print('Suggestion: The server is taking too long to respond.')
            
        elif "no scheme supplied" in error_message:
            suggestion = f"https://{url}"
            print('Error : The URL format is invalid.')
            print('Did you mean ' + suggestion + '?')

        elif "ssl" in error_message or "certificate verify failed" in error_message:
            print("SSL Error: Could not verify the website's security certificate.")
            print('Suggestion: The site may be insecure or have an outdated certificate.')

        elif "proxy" in error_message:
            print('Proxy Error: The request failed due to a proxy configuration issue.')

        elif "exceeded" in error_message and "redirects" in error_message:
            print('Redirect Error: The URL caused too many redirects and is stuck in a loop.')

        else:
            print(f"An unexpected connection error occurred: {e}")


if __name__ == '__main__':
    response_status()

