# Federal Reserve Economic Data

#### Growth

# GDP - Gross Domestic Product
# GDPC1 - Real Gross Domestic Product
# GDPPOT - Real Potential Gross Domestic Product

#### Prices and Inflation

# CPIAUCSL - Consumer Price Index for All Urban Consumers: All Items
# CPILFESL - Consumer Price Index for All Urban Consumers: All Items Less Food & Energy
# GDPDEF - Gross Domestic Product: Implicit Price Deflator

#### Interest Rates

# DFF - Effective Federal Funds Rate
# DTB3 - 3-Month Treasury Bill: Secondary Market Rate
# T5YIFR - 5-Year, 5-Year Forward Inflation Expectation Rate
# DPRIME - Bank Prime Loan Rate

#### Employment

# UNRATE - Civilian Unemployment Rate
# EMRATIO - Civilian Employment-Population Ratio
# UNEMPLOY - Unemployed

#### Income and Expenditure

# MEHOINUSA672N - Real Median Household Income in the United States
# DSPIC96 - Real Disposable Personal Income
# PSAVERT - Personal Saving Rate

#### Debt

# GFDEBTN - Federal Debt: Total Public Debt
# EXCSRESNW - Excess Reserves of Depository Institutions
# TOTCI - Commercial and Industrial Loans, All Commercial Banks

import quandl
import pandas as pd
from functools import reduce
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def update_data():
    
    quandl.ApiConfig.api_key = "7wvuqmnqzu5SzffxWxGB"

    # Growth

    GDP_data = quandl.get('FRED/GDP') # Gross Domestic Product
    GDP_data.columns = ['Gross Domestic Product']

    GDPC1_data = quandl.get('FRED/GDPC1') # Real Gross Domestic Product
    GDPC1_data.columns = ['Real Gross Domestic Product']

    GDPPOT_data = quandl.get('FRED/GDPPOT') # Real Potential Gross Domestic Product
    GDPPOT_data.columns = ['Real Potential Gross Domestic Product']

    # Prices and Inflation

    CPIAUCSL_data = quandl.get('FRED/CPIAUCSL') # Consumer Price Index for All Urban Consumers: All Items
    CPIAUCSL_data.columns = ['Consumer Price Index for All Urban Consumers: All Items']

    CPILFESL_data = quandl.get('FRED/CPILFESL') # Consumer Price Index for All Urban Consumers: All Items Less Food & Energy
    CPILFESL_data.columns = ['Consumer Price Index for All Urban Consumers: All Items Less Food & Energy']

    GDPDEF_data = quandl.get('FRED/GDPDEF') # Gross Domestic Product: Implicit Price Deflator
    GDPDEF_data.columns = ['Gross Domestic Product: Implicit Price Deflator']

    # Interest Rates

    DFF_data = quandl.get('FRED/DFF') # Effective Federal Funds Rate
    DFF_data.columns = ['Effective Federal Funds Rate']

    DTB3_data = quandl.get('FRED/DTB3') # 3-Month Treasury Bill: Secondary Market Rate
    DTB3_data.columns = ['3-Month Treasury Bill: Secondary Market Rate']

    T5YIFR_data = quandl.get('FRED/T5YIFR') # 5-Year, 5-Year Forward Inflation Expectation Rate
    T5YIFR_data.columns = ['5-Year, 5-Year Forward Inflation Expectation Rate']

    DPRIME_data = quandl.get('FRED/DPRIME') # Bank Prime Loan Rate
    DPRIME_data.columns = ['Bank Prime Loan Rate']

    # Employment

    UNRATE_data = quandl.get('FRED/UNRATE') # Civilian Unemployment Rate
    UNRATE_data.columns = ['Civilian Unemployment Rate']

    EMRATIO_data = quandl.get('FRED/EMRATIO') # Civilian Employment-Population Ratio
    EMRATIO_data.columns = ['Civilian Employment-Population Ratio']

    UNEMPLOY_data = quandl.get('FRED/UNEMPLOY') # Unemployed
    UNEMPLOY_data.columns = ['Unemployed']


    # Income and Expenditure

    MEHOINUSA672N_data = quandl.get('FRED/MEHOINUSA672N') # Real Median Household Income in the United States
    MEHOINUSA672N_data.columns = ['Real Median Household Income in the United States']

    DSPIC96_data = quandl.get('FRED/DSPIC96') # Real Disposable Personal Income
    DSPIC96_data.columns = ['Real Disposable Personal Income']

    PSAVERT_data = quandl.get('FRED/PSAVERT') # Personal Saving Rate
    PSAVERT_data.columns = ['Personal Saving Rate']


    # Debt

    GFDEBTN_data = quandl.get('FRED/GFDEBTN') # Federal Debt: Total Public Debt
    GFDEBTN_data.columns = ['Federal Debt: Total Public Debt']

    EXCSRESNW_data = quandl.get('FRED/EXCSRESNW') # Excess Reserves of Depository Institutions
    EXCSRESNW_data.columns = ['Excess Reserves of Depository Institutions']

    TOTCI_data = quandl.get('FRED/TOTCI') # Commercial and Industrial Loans, All Commercial Banks
    TOTCI_data.columns = ['Commercial and Industrial Loans, All Commercial Banks']


    # Merge all DataFrames
    
    dataframes_to_merge = [
        GDP_data, GDPC1_data, GDPPOT_data, CPIAUCSL_data, CPILFESL_data,
        GDPDEF_data, DFF_data, DTB3_data, T5YIFR_data, DPRIME_data, UNRATE_data,
        EMRATIO_data, UNEMPLOY_data, MEHOINUSA672N_data, DSPIC96_data,
        PSAVERT_data, GFDEBTN_data, EXCSRESNW_data, TOTCI_data
    ]

    df_merged = reduce(
        lambda left, right: pd.merge(
            left, right, left_index=True, right_index=True, how='outer'),
        dataframes_to_merge)

    # Write the merged dataframes to a CSV
    
    df_merged.to_csv('Economic_Data.csv')

    # Upload this CSV to Google Drive
    
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'id': '10mjUvGIK_Ai5hKITCbUQcAaZhm0cl6o0'})
    file.SetContentFile('Economic_Data.csv')
    file.Upload()