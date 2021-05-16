# Tax Calculator
## OVERVIEW
The TAX CALCULATOR APP is composed of a SWIFT frontend and a Python(FastAPI) backend.  The backend is very simple.  FastAPI is simply connected to the swift front end, which is
sending a request to FastAPI, and pulling/returning values based on the inputs.  This is stored in JSON in order to be compatable with the front end.

- Tax Calculation


The tax calculation had a few steps.  First, we had to create a python class that would contain the state, abbreviation, and tax rate.  
```python
class StateIncomeTax:
    def __init__(self,name: str, abbreviation: str, tax: float):
        self.name = name
        self.tax = tax
        self.abbreviation = abbreviation
```


Next, we had to create an object for each state.  This was achieved by taking in the state, abbreviation, and then manually calculating the average income tax rate for each state and
manually inputting it.  

```python
Alaska = StateIncomeTax("ALASKA", "AK", 0.00)
Florida = StateIncomeTax("FLORIDA","FL",0.00)
Nevada = StateIncomeTax("NEVADA","NV",0.00)
South_Dakota = StateIncomeTax("SOUTH DAKOTA", "SD", 0.00)
Tennessee = StateIncomeTax("TENNESSEE", "TN", 0.00)
Texas = StateIncomeTax("TEXAS", "TX", 0.00)
Washington = StateIncomeTax("WASHINGTON","WA", 0.00)
Wyoming = StateIncomeTax("WYOMING", "WY", 0.00)
# -------------------------------
# FLAT INCOME TAX
New_Hampshire = StateIncomeTax("NEW HAMPSHIRE", "NH", 0.05)
Colorado = StateIncomeTax("COLORADO", "CO", 0.0455)
Illinois = StateIncomeTax("ILLINOIS", "IL", 0.0495)
Indiana = StateIncomeTax("INDIANA", "IN", 0.0323)
Kentucky = StateIncomeTax("KENTUCKY", "KY", 0.05)
Massachusetts = StateIncomeTax("MASSACHUSETTS", "MA", 0.05)
Michigan = StateIncomeTax("MICHIGAN", "MI", 0.0425)
North_Carolina = StateIncomeTax("NORTH CAROLINA", "NC", 0.0525)
Pennsylvania = StateIncomeTax("PENNSYLVANIA", "PA", 0.0307)
Utah = StateIncomeTax("UTAH", "UT", 0.0495)
# ------------------------------
# BRACKETED INCOME TAX
Alabama = StateIncomeTax("ALABAMA", "AL", 0.0367)
Arizona = StateIncomeTax("ARIZONA", "AZ", 0.0515)
Arkansas = StateIncomeTax("ARKANSAS", "AR", 0.0397)
California = StateIncomeTax("CALIFORNIA", "CA", 0.09)
Connecticut = StateIncomeTax("CONNECTICUT", "CT", 0.0479)
Delaware = StateIncomeTax("DELAWARE", "DE", 0.0389)
Georgia = StateIncomeTax("GEORGIA", "GA", 0.287)
Hawaii = StateIncomeTax("HAWAII", "HI", 0.078)
Idaho = StateIncomeTax("IDAHO", "ID", 0.314)
Iowa = StateIncomeTax("IOWA", "IA", 0.0578)
Kansas = StateIncomeTax("KANSAS", "KS", 0.0451)
Louisiana = StateIncomeTax("LOUISIANA", "LA", 0.04)
Maine = StateIncomeTax("MAINE", "ME", 0.06)
Maryland = StateIncomeTax("MARYLAND", "MD", 0.0413)
Minnesota = StateIncomeTax("MINNESOTA", "MN", 0.0763)
Mississippi = StateIncomeTax("MISSISSIPPI", "MS", 0.04)
Missouri = StateIncomeTax("MISSOURI", "MO", 0.0387)
Montana = StateIncomeTax("MONTANA", "MT", 0.043)
Nebraska = StateIncomeTax("NEBRASKA", "NE", 0.0531)
New_Jersey = StateIncomeTax("NEW JERSEY", "NJ", 0.0735)
New_Mexico = StateIncomeTax("NEW MEXICO", "NM", 0.0378)
New_York = StateIncomeTax("NEW YORK", "NY", 0.0631)
North_Dakota = StateIncomeTax("NORTH DAKOTA", "ND", 0.0189)
Ohio = StateIncomeTax("OHIO", "OH", 0.0283)
Oklahoma = StateIncomeTax("OKLAHOMA", "OK", 0.05)
Oregon = StateIncomeTax("OREGON", "OR", 0.079)
Rhode_Island = StateIncomeTax("RHODE ISLAND", "RI", 0.453)
South_Carolina = StateIncomeTax("SOUTH CAROLINA", "SC", 0.07)
Vermont = StateIncomeTax("VERMONT", "VT", 0.0532)
Virginia = StateIncomeTax("VIRGINIA", "VA", 0.0575)
West_Virginia = StateIncomeTax("WEST VIRGINIA", "WV", 0.0585)
Wisconsin = StateIncomeTax("WISCONSIN", "WI", 0.0585)
# ---------------------------------------
```


After all this was achieved, we input each state into a list so that we could iterate through and call it at will.  

```Python
list_states = [Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut,
               Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa,
               Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan,
               Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada,
               New_Hampshire, New_Jersey, New_Mexico, New_York, North_Carolina,
               North_Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode_Island,
               South_Carolina, South_Dakota, Tennessee, Texas, Utah, Vermont,
               Virginia, Washington, West_Virginia, Wisconsin, Wyoming]
```

Now we were able to worry about the tax calculations. This was used via a function that would take in two endpoints: state and income.

 ```python
 def calc_tax(state: str, income: int or float):

    for item in list_states:
        if state.upper() == item.name or state.upper() == item.abbreviation:
            tax = calculate_federal_tax(income)
            total_inc = (tax) * (1-item.tax)
            total_tax = income - total_inc
            return {"remaining": float("{:.2f}".format(total_inc)),
                    "tax": float("{:.2f}".format(total_tax)),
                    "state":f"{state}"}
```

Here, you first see that we iterate through the list of states, and if the input matches either the name or the abbreviation,
we calculate the income.  First, we find the reamianing income through total_inc.  This first calculates the federal taxes.  After doing this,
total_inc equals the federal tax (tax) times the item tax to give the remaining income.  We then calculated the total income taken from 
taxes using "total_tax".  This simply took the gross income minus the taxed income.  This returned how much one lost through taxes.
This was then returned in JSON format in order to be compatable with the swift front end.

- Assets Calculation

Assets calculation was much simpler.  Here, there was only one endpoint needed- amount invested.  After this, we decided to take
both the yearly and monthly returns on investment calculated.  Using the average rate of 10% return on investment per year, we simply 
took in the amount invested and calculated the return based on that.  

 ```python
 def calc_asset(invested: int or float):
    amount_return_month = invested * (0.1/12)
    amount_return_year = invested * 0.1
    return {"amount_invested": float("{:.2f}".format(invested)),
            "return_per_month": float("{:.2f}".format(amount_return_month)),
            "return_per_year": float("{:.2f}".format(amount_return_year))}
 ```
 
 
 # Conclusion
 
 This project was very involved and had lots of parts.  The hardest part of this project was definitely collection of data.  Each 
 state is unique with their income laws etc.  This made it difficult to find everything needed.  It was also a pain to keep in mind 
 that I attempting to keep compatability with something else, but was a good requirement as it provided me with the experience of keeping 
 other things in mind rather than just building it to output the results I wanted.  




