import logging
import azure.functions as func
from .. import EnergiBeregning


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    calc: EnergiBeregning
    req_body: str = req.get_body().decode("utf-8")

    # Generate calc object
    try:
        calc = EnergiBeregning.EnergiBeregning.from_json(req_body)
    except KeyError as e:
        logging.error(f"Could not parse request body for calc: {req_body}, {str(e)}")
        return func.HttpResponse(
            f"Could not parse request body, key not found: {str(e)}", status_code=400
        )

    return func.HttpResponse(body=calc.calculate().to_json(), status_code=200, mimetype="application/json")
