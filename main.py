import uvicorn
from fastapi import FastAPI, HTTPException
from src.utils.invalid_input_error import InvalidInputError
from src.utils.helper import is_valid_flow
from src.handler.package_inflow_processor import PackageInflowProcessor


app = FastAPI()


@app.get("/")
def get_total_package_inflows(acme: str):
    # Initially check if 'acme' contains a character not present in the 'encoding'
    if not is_valid_flow(acme):
        message = "contains an invalid character"
        print("ERROR: '{}' {}".format(acme, message)) # for terminal output
        raise HTTPException(status_code=400, detail=message)
    

    processor = PackageInflowProcessor()
    try:
        total_package_inflows = processor.process_input(acme)
        return {"total_package_inflows": total_package_inflows}
    except InvalidInputError as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=400, detail=e.message)
        # return {"ERROR": "'{}' {}".format(e.expression, e.message)}

