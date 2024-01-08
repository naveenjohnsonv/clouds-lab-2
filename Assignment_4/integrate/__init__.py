import logging
import azure.functions as func
import numpy as np
import json

def integrate(lower, upper, N):
    dx = (upper - lower) / N
    x = np.linspace(lower, upper, N+1)
    y = np.abs(np.sin(x))
    integral = dx * np.sum(y)
    return integral

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Attempt to get the 'lower' and 'upper' parameters from the query or route parameters
    lower = req.params.get('lower')
    upper = req.params.get('upper')

    # If not found, attempt to get them from the request body
    if not lower or not upper:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            lower = req_body.get('lower')
            upper = req_body.get('upper')

    # Convert the parameters to floats if they are not None
    if lower is not None and upper is not None:
        try:
            lower = float(lower)
            upper = float(upper)
        except ValueError:
            return func.HttpResponse(
                "Invalid input: 'lower' and 'upper' must be numeric.",
                status_code=400
            )

        n_values = [10, 100, 1000, 10000, 100000, 1000000]
        integrals = []
        for n in n_values:
            result = integrate(lower, upper, n)
            integrals.append(result)

        return func.HttpResponse(json.dumps(integrals), status_code=200)
    else:
        return func.HttpResponse(
             "Please pass 'lower' and 'upper' in the query string or in the request body",
             status_code=400
        )