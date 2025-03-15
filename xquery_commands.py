import requests

def run_marklogic_xquery(query, host="localhost", port=8000, user="admin", password="admin"):
    """
    Executes an XQuery statement on a MarkLogic server via its REST API.
    
    :param query: The XQuery string to execute
    :param host: MarkLogic server hostname or IP
    :param port: MarkLogic REST API port (default: 8000)
    :param user: MarkLogic username
    :param password: MarkLogic password
    :return: Query output as a string
    """
    url = f"http://{host}:{port}/v1/eval"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"xquery": query}
    
    try:
        response = requests.post(url, headers=headers, data=data, auth=(user, password))
        response.raise_for_status()  # Raise an error for HTTP failures
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error executing XQuery: {e}"

if __name__ == "__main__":
    # Example XQuery
    xquery_string = 'xdmp:document-get("/example.xml")//title'
    
    output = run_marklogic_xquery(xquery_string)
    print("Query Output:\n", output)
