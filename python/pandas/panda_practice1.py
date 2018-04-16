import quandl
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
import pickle
style.use('fivethirtyeight')


web_stats = {
            "Day":[1,2,3,4,5,6],
            "Visitors":[43,53,34,45,64,34],
            "Bounce_Rate":[65,72,62,64,54,66]
}

df = pd.DataFrame(web_stats)

# print(df)
# print(df.tail())
# print(df.tail(2))
# print(df.set_index('Day',inplace=True))
# print(df.head())
# print(df['Visitors'])
# print(df.Visitors)
# print(df[['Bounce_Rate','Visitors']])
# print(df.Visitors.tolist())
# print(np.array(df[['Bounce_Rate','Visitors']]))

# df2 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
# print(df2)




# #Pandas IO's 
# df = pd.read_csv('ZILLOW-M1060_PHIVAH.csv')
# print(df.head())
# df.set_index('Date',inplace=True)
# df.to_csv('newcsv2.csv')
# df = pd.read_csv('newcsv2.csv')
# print(df.head())


# df = pd.read_csv('newcsv2.csv',index_col=0)
# print(df.head())

# df.columns = ['Austin_HPI']
# print(df.head())
# df.to_csv('newcsv3.csv')
# df.to_csv('newcsv4.csv',header=False)


# df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'],index_col=False)
# print(df.head())
# df.to_html('example.html')
# df.rename(columns={'Austin_HPI':'770006_HPI'},inplace=True)
# print(df.head())

# api_key = open('quandlapikey.txt','r').read()



# fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(fiddy_states)

##Dataframe 
#print(fiddy_states[0])

##Read column zero 
# print(fiddy_states[0][1][1:])

# for abbv in fiddy_states[0][1][1:]:
#     df = quandl.get('FMAC/HPI_'+str(abbv), authtoken=api_key)
#     df.columns=[str(abbv)]
#     print(df.head())

# main_df = pd.DataFrame()
# for abbv in fiddy_states[0][1][1:]:
#     df = quandl.get("FMAC/HPI_"+str(abbv), authtoken=api_key)
#     df.columns=[str(abbv)]
#     if main_df.empty:
#         main_df = df
#     else:
#         main_df = main_df.join(df)
# print(main_df.head())

    

# Pandas concatination and appending 

# df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2,3,2,2],
#                     'US_GDP_Thousand':[50,55,65,55]},
#                     index=[2001,2002,2003,2004])

# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2,3,2,2],
#                     'US_GDP_Thousand':[50,55,65,55]},
#                     index=[2005,2006,2007,2008])                

# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2,3,2,2],
#                     'Low_tier_HPI':[50,52,50,53]},
#                     index=[2001,2002,2003,2004])

# concat = pd.concat([df1,df2,df3])
# print(concat)

# df4=df1.append(df2)

# print(df4.head())

# s = pd.Series([80,2,50],index=['HPI','Int_rate','US_GDP_Thousand'])
# df4 = df1.append(s,ignore_index=True)
# print(df4)

#Merging and joining 

# print(pd.merge(df1,df2,on='HPI', how='left'))
# print(pd.merge(df1,df2,on='HPI', how='right'))
# print(pd.merge(df1,df2,on='HPI', how='outer'))
# print(pd.merge(df1,df2,on='HPI', how='inner'))


# df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)

# joined = df1.join(df3)
# joined = df1.join(df3)
# print(joined)

## pickling the data 

# api_key = open('quandlapikey.txt','r').read()

# fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states)

# ## Dataframe 
# print(fiddy_states[0])

# ## Read column zero 
# print(fiddy_states[0][1][1:])

# main_df = pd.DataFrame()

# for abbv in fiddy_states[0][1][1:]:
#     query = "FMAC/HPI_"+str(abbv)
#     df = quandl.get(query, authtoken=api_key)

#     if main_df.empty:
#         main_df = df 
#     else:
#          main_df=main_df.join(df)
# print(main_df.head())



# api_key = open('quandlapikey.txt','r').read()

# def state_list():
#     fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#     return fiddy_states[0][1][1:]


# def grab_initial_state_data():
#     states = state_list()
#     main_df = pd.DataFrame()
#     for abbv in states:
#         query = "FMAC/HPI_"+str(abbv)
#         df = quandl.get(query, authtoken=api_key)
#         df.columns = [str(abbv)]
#         if main_df.empty:
#             main_df = df 
#         else:
#             main_df=main_df.join(df)

#     pickle_out = open('fiddy_states.pickle','wb')
#     pickle.dump(main_df,pickle_out)
#     pickle_out.close()

# grab_initial_state_data()

# pickle_in = open('fiddy_states.pickle','rb')
# print_out = pickle.load(pickle_in)
# print(print_out)

# print_out.to_pickle('pickle.pickle')
# HPI_data = pd.read_pickle('pickle.pickle')
# print(print_out2)
# HPI_data.plot()
# plt.legend().remove()
# plt.show()



# api_key = open('quandlapikey.txt','r').read()

# def state_list():
#     fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#     return fiddy_states[0][1][1:]


# def grab_initial_state_data():
#     states = state_list()
#     main_df = pd.DataFrame()
#     for abbv in states:
#         query = "FMAC/HPI_"+str(abbv)
#         df = quandl.get(query, authtoken=api_key)
#         df.columns = [str(abbv)]
#         df[abbv] = (df[abbv] - df[abbv][0])/df[abbv][0] * 100
#         #df = df.pct_change()
#         if main_df.empty:
#             main_df = df 
#         else:
#             main_df=main_df.join(df)
#     print(main_df.head())
#     pickle_out = open('fiddy_states.pickle','wb')
#     pickle.dump(main_df,pickle_out)
#     pickle_out.close()

# grab_initial_state_data()

# pickle_in = open('fiddy_states.pickle','rb')
# print_out = pickle.load(pickle_in)
# print(print_out)

#print_out.to_pickle('pickle.pickle')
HPI_data = pd.read_pickle('fiddy_states.pickle')
# HPI_data_correlation = HPI_data.corr()
# HPI_data_correlation.describe()
# print(HPI_data_correlation)
# HPI_data.plot()
# plt.legend().remove()
# plt.show()

## subplot example 

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))
# HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')
# print(HPI_data[['TX','TX1yr']].head())
# #HPI_data.fillna(method='ffill',inplace=True)
# HPI_data.fillna(value=-999,inplace=True)
# #HPI_data.dropna(how='any',inplace=True)
# print(HPI_data[['TX','TX1yr']].head())

# print(HPI_data.isnull().values.sum())
# HPI_data[['TX','TX1yr']].plot(ax=ax1)
# plt.legend(loc=4)
# plt.show()


# benchmark = HPI_Benchmark()

## Rolling  fucntions 

# fig = plt.figure()
# ax1 = plt.subplot2grid((2,1),(0,0))
# ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)


# HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'],12)
# HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'],12)
# print(HPI_data[['TX','TX12MA','TX12STD']].head())

# HPI_data[['TX','TX12MA']].plot(ax=ax1)
# HPI_data[['TX12STD']].plot(ax=ax2)


# plt.legend(loc=1)
# plt.show()


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)

TX_AK_12corr = pd.rolling_corr(HPI_data['TX'],HPI_data['AK'],12)
HPI_data['TX'].plot(ax=ax1,label='TX HPI')
HPI_data['AK'].plot(ax=ax1,label='AK HPI')

ax1.legend(loc=4)
TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

plt.legend(loc=4)
plt.show()








    
    
