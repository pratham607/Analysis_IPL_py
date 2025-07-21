import pandas  as pd
df=pd.read_csv("deliveries.csv",encoding="latin1")
print(df)
print(df.info())
print(df.iloc[:,0])
import pandas as pd
df=pd.read_csv("matches.csv",encoding="latin1")
print(df.info())
#no of matches
print(df[["Season","team1","team2"]])
#no of mathces per season
print()
ipl2008=df[df["Season"]=="IPL-2008"]
print(ipl2008)
ipl2009=df[df["Season"]=="IPL-2009"]
print(ipl2009)
ipl2010=df[df["Season"]=="IPL-2010"]
print(ipl2010)
ipl2011=df[df["Season"]=="IPL-2011"]
print(ipl2011)
ipl2012=df[df["Season"]=="IPL-2012"]
print(ipl2012)
ipl2013=df[df["Season"]=="IPL-2013"]
print(ipl2013)
ipl2014=df[df["Season"]=="IPL-2014"]
print(ipl2014)
ipl2015=df[df["Season"]=="IPL-2015"]
print(ipl2015)
ipl2016=df[df["Season"]=="IPL-2016"]
print(ipl2016)
ipl2017=df[df["Season"]=="IPL-2017"]
print(ipl2017)
ipl2018=df[df["Season"]=="IPL-2018"]
print(ipl2018)
ipl2019=df[df["Season"]=="IPL-2019"]
print(ipl2019)
#Most successful team (max wins)
win_count=df["winner"].value_counts()
print(win_count)
print(df[["win_by_runs","win_by_wickets"]])
#Most matches won chasing vs defending
win_run=df["win_by_runs"] !=0
run=win_run.sum()
print("Run wins :",run)
win_wickets=df["win_by_wickets"] !=0
wickets=win_wickets.sum()
print("Wicket wins:",wickets)
#player
import pandas as pd
df=pd.read_csv("most_runs_average_strikerate.csv",encoding="latin1")
print(df)
print(df.describe())


