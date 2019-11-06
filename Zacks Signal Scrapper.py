# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:43:20 2018

@author: Sajad
Zacks' Ranking scrapping
"""
workingdirectory = 'D:/Sajad/advance get/zacks'
import pandas as pd
import urllib.request
import datetime as dt
import os
os.chdir(workingdirectory)

#  
def Zacks_Rank(Symbol):
  
    # Wait for 2 seconds
    #time.sleep(2)
    url = 'https://quote-feed.zacks.com/index?t='+Symbol 
    downloaded_data  = urllib.request.urlopen(url)
    data = downloaded_data.read()
    data_str = data.decode()
    Z_Rank =["Strong Buy","Buy","Hold","Sell","Strong Sell"]
    def between(value, a, b): # extracting FUNCTION TO open ,low,high,volume from data
        # Find and validate before-part.
        pos_a = value.find(a) # return the first character index or -1= Not exist
        if pos_a == -1: return ""
        # Find and validate after part.
        pos_b = value.rfind(b)
        if pos_b == -1: return ""
        # Return middle part.
        adjusted_pos_a = pos_a + len(a)
        if adjusted_pos_a >= pos_b: return ""
        return value[adjusted_pos_a:pos_b]
    for Rank in Z_Rank:
       #data_str.find(Rank)# az tooye list Z_Rank doone doone check kon va yeki ra dar str_data
       # peyda kon ;; faghat index harf aval ro retrun mikond
       if(data_str.find(Rank) != -1):
           return Rank #data_str[res:res+len(Rank)]# 
        
def Market_Rank(Symbols):
    Strong_Buy=[]
    Buy=[]
    Hold=[]
    Sell=[]
    Strong_Sell=[]
    for symbol in Symbols:
        Rank = Zacks_Rank(symbol)# 
        if(Rank == 'Strong Buy'):
            Strong_Buy.append(symbol)
        elif(Rank == 'Buy'):
            Buy.append(symbol)
        elif(Rank == 'Hold'):
            Hold.append(symbol)
        elif(Rank == 'Sell'):
            Sell.append(symbol)
        elif(Rank == 'Strong Sell'):
            Strong_Sell.append(symbol)
    
    Result = {'Strong_Buy':Strong_Buy,'Buy':Buy,'Hold':Hold,'Sell':Sell,'Strong_Sell':Strong_Sell}
    return Result

SP500=["A","AAL","AAP","AAPL","ABBV","ABC","ABT","ACN","ADBE","ADI","ADM","ADP",
        "ADS","ADSK","AEE","AEP","AES","AET","AFL","AGN","AIG","AIV","AIZ","AJG",
        "AKAM","ALB","ALGN","ALK","ALL","ALLE","ALXN","AMAT","AMD","AME","AMG",
        "AMGN","AMP","AMT","AMZN","ANDV","ANSS","ANTM","AON","AOS","APA","APC",
        "APD","APH","ARE","ARNC","ATVI","AVB","AVGO","AVY","AWK","AXP","AYI",
        "AZO","BA","BAC","BAX","BBT","BBY","BCR","BDX","BEN","BHF","BHGE",
        "BIIB","BK","BLK","BLL","BMY","BSX","BWA","BXP","C","CA","CAG",
        "CAH","CAT","CB","CBG","CBOE","CBS","CCI","CCL","CELG","CERN","CF","CFG",
        "CHD","CHK","CHRW","CHTR","CI","CINF","CL","CLX","CMA","CMCSA","CME","CMG",
        "CMI","CMS","CNC","CNP","COF","COG","COH","COL","COO","COP","COST","COTY",
        "CPB","CRM","CSCO","CSRA","CSX","CTAS","CTL","CTSH","CTXS","CVS","CVX",
        "CXO","D","DAL","DE","DFS","DG","DGX","DHI","DHR","DIS","DISCA","DISCK",
        "DISH","DLPH","DLR","DLTR","DOV","DPS","DRE","DRI","DTE","DUK","DVA","DVN",
        "DWDP","DXC","EA","EBAY","ECL","ED","EFX","EIX","EL","EMN","EMR","EOG",
        "EQIX","EQR","EQT","ES","ESRX","ESS","ETFC","ETN","ETR","EVHC","EW","EXC",
        "EXPD","EXPE","EXR","F","FAST","FB","FBHS","FCX","FDX","FE","FFIV","FIS",
        "FISV","FITB","FL","FLIR","FLR","FLS","FMC","FOX","FOXA","FRT","FTI","FTV",
        "GD","GE","GGP","GILD","GIS","GLW","GM","GOOG","GOOGL","GPC","GPN","GPS",
        "GRMN","GS","GT","GWW","HAL","HAS","HBAN","HBI","HCA","HCN","HCP","HD",
        "HES","HIG","HLT","HOG","HOLX","HON","HP","HPE","HPQ","HRB","HRL","HRS",
        "HSIC","HST","HSY","HUM","IBM","ICE","IDXX","IFF","ILMN","INCY","INFO",
        "INTC","INTU","IP","IPG","IR","IRM","ISRG","IT","ITW","IVZ","JBHT","JCI",
        "JEC","JNJ","JNPR","JPM","JWN","K","KEY","KHC","KIM","KLAC","KMB","KMI",
        "KMX","KO","KORS","KR","KSS","KSU","L","LB","LEG","LEN","LH","LKQ","LLL",
        "LLY","LMT","LNC","LNT","LOW","LRCX","LUK","LUV","LVLT","LYB","M","MA",
        "MAA","MAC","MAR","MAS","MAT","MCD","MCHP","MCK","MCO","MDLZ","MDT","MET",
        "MGM","MHK","MKC","MLM","MMC","MMM","MNST","MO","MON","MOS","MPC","MRK",
        "MRO","MS","MSFT","MSI","MTB","MTD","MU","MYL","NAVI","NBL","NDAQ","NEE",
        "NEM","NFLX","NFX","NI","NKE","NLSN","NOC","NOV","NRG","NSC","NTAP","NTRS",
        "NUE","NVDA","NWL","NWS","NWSA","O","OKE","OMC","ORCL","ORLY",'OXY',"PAYX",
        "PBCT","PCAR","PCG","PCLN","PDCO","PEG","PEP","PFE","PFG","PG","PGR","PH",
        "PHM","PKG","PKI","PLD","PM","PNC","PNR","PNW","PPG","PPL","PRGO","PRU",
        "PSA","PSX","PVH","PWR","PX","PXD","PYPL","Q","QCOM","QRVO","RCL","RE",
        "REG","REGN","RF","RHI","RHT","RJF","RL","RMD","ROK","ROP","ROST","RRC",
        "RSG","RTN","SBAC","SBUX","SCG","SCHW","SEE","SHW","SIG","SJM","SLB",
        "SLG","SNA","SNI","SNPS","SO","SPG","SPGI","SRCL","SRE","STI","STT","STX",
        "STZ","SWK","SWKS","SYF","SYK","SYMC","SYY","T","TAP","TDG","TEL","TGT",
        "TIF","TJX","TMK","TMO","TRIP","TROW","TRV","TSCO","TSN","TSS","TWX","TXN",
        "TXT","UA","UAA","UAL","UDR","UHS","ULTA","UNH","UNM","UNP","UPS","URI",
        "USB","UTX","V","VAR","VFC","VIAB","VLO","VMC","VNO","VRSK","VRSN","VRTX",
        "VTR","VZ","WAT","WBA","WDC","WEC","WFC","WHR","WLTW","WM","WMB","WMT",
        "WRK","WU","WY","WYN","WYNN","XEC","XEL","XL","XLNX","XOM","XRAY","XRX",
        "XYL","YUM","ZBH","ZION","ZTS"]
condition= True
if(condition == True):
    result = Market_Rank(SP500)
    print('Strong Buy are:\n')
    print(result['Strong_Buy'])
    print('===================================')
    print('Buy are:\n')
    print(result['Buy'])
    print('===================================')
    print('HOLD are:\n')
 #   print(result['Hold'])
    print('===================================')
    print('SELL are:\n')
    print(result['Sell'])
    print('===================================')
    print('STRONG SELL are:\n')
    print(result['Strong_Sell'])
    # append the result into data frame :: different key sizes so it should produce NAN values 
    dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in result.items() })
    today = dt.datetime.today().strftime('%Y-%m-%d')
    dict_df.to_csv(path_or_buf=workingdirectory +'/SP500'+today+'.csv',index =False)
    #path be hamrah filename, index=False::> row NO Number

#for filename in os.listdir(workingdirectory):
#    if filename.startswith("Last_"):
#       os.rename('l.csv', 'OLD_11.csv')

if(condition==False):
# converting Nasdaq dataframe to list in order or scraping data
    Nasdaq = pd.read_csv('D:/sajad/advance get/Nasdaq.csv')
    Nasdaq_list = []
    for sym in Nasdaq['Symbol']:
        Nasdaq_list.append(sym)
    
    
    Nasdaq_result = Market_Rank(Nasdaq_list)# it is a dictionary
    # append the result into data frame :: different key sizes so it should produce NAN values 
    dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in Nasdaq_result.items() })
    today = dt.datetime.today().strftime('%Y-%m-%d')
    dict_df.to_csv(path_or_buf=workingdirectory +'/Nasdaq_'+today+'.csv',index =False)
    #path be hamrah filename, index=False::> row NO Number

### getting all files in the working directory
file_list=os.listdir(workingdirectory)
if (condition==True):
# filter all file that contains SP500 in its name
    file_list=[k for k in file_list if 'SP500' in k]
else:
    file_list=[k for k in file_list if 'Nasdaq' in k]
    
previous_file=file_list[-2]
previous_rank=pd.read_csv(previous_file)

# check the latest change in the ranks
for ran in ['Strong_Buy','Buy','Hold','Sell','Strong_Sell']:
    change=[]
    #ran = 'Strong_Buy'
    # removing all nan from list except one
    previous_z_rank=list(set(previous_rank[ran]))
    for item in result[ran]:
        if(item not in previous_z_rank):
            
            change.append(item)
    if ran == 'Strong_Buy':
        new_To_Strong_Buy=change
    elif ran == 'Buy':
        new_To_Buy=change
    elif ran == 'Hold':
        new_To_Hold=change
    elif ran == 'Sell':
        new_To_Sell=change
    elif ran == 'Strong_Sell':
        new_To_Strong_Sell=change

    
    print('============= New added to '+ran+' Rank ==============')
    print(change)
    print('\n')
New_Change_in_Ranks = {'Strong_Buy':new_To_Strong_Buy,'Buy':new_To_Buy,'Hold':new_To_Hold,'Sell':new_To_Sell,'Strong_Sell':new_To_Strong_Sell}
Changes_df = pd.DataFrame({ key:pd.Series(value) for key, value in New_Change_in_Ranks.items() })
today = dt.datetime.today().strftime('%Y-%m-%d')
if (condition):
    Changes_df.to_csv(path_or_buf=workingdirectory +'/changeSP_'+today+'.csv',index =False)
#path be hamrah filename, index=False::> row NO Number
else:
    Changes_df.to_csv(path_or_buf=workingdirectory +'/changeNAS_'+today+'.csv',index =False)
    
    





