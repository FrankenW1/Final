from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Calculations import *


tax_router = APIRouter(prefix="/tax")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

states = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA",
          "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE",
          "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA",
          "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO",
          "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS",
          "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
state_abb = ["AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
              "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
              "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX",
              "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
@tax_router.get("/calculate_tax")
def calc_tax(state: str, income: int or float):

    for item in list_states:
        if state.upper() == item.name or state.upper() == item.abbreviation:
            total_inc = (1 - item.tax) * income
            tax = calculate_federal_tax(income)
            total_inc = (tax) * (1-item.tax)
            total_tax = income - total_inc
            return {"remaining": float("{:.2f}".format(total_inc)),
                    "tax": float("{:.2f}".format(total_tax)),
                    "state":f"{state}"}

@tax_router.get("/calculate_asset")
def calc_asset(invested: int or float):
    amount_return_month = invested * (0.1/12)
    amount_return_year = invested * 0.1
    return {"amount invested": float("{:.2f}".format(invested)),
            "return per month": float("{:.2f}".format(amount_return_month)),
            "return per year": float("{:.2f}".format(amount_return_year))}
app.include_router(tax_router)
if __name__ == "__main__":
    uvicorn.run("serv:app", host="0.0.0.0", reload="true")
