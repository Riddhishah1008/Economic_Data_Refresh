# Economic_Data_Refresh

This code refreshes the data for a [Tableau Dashboard](https://prod-apnortheast-a.online.tableau.com/#/site/riddhi1008/workbooks/168022?:origin=card_share_link) hosted on Tableau Online. 

When the Refresh Data button on the FLASK App is clicked, it runs a py file which sends requests to the Quandl API to get the latest data. The py file also updates the CSV on Google Drive which is the live data connection for the Tableau dashboard.
