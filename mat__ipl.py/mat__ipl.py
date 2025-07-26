#importing nesscary library
import pandas as pd
import matplotlib.pyplot as plt
#creating a subset
df=pd.read_csv("most_runs_average_strikerate.csv",encoding="latin1")


#Top 5 run scorer 


df=df.dropna(subset=['batsman','total_runs'])
run_count=df["total_runs"].head(5)
bats_name=df['batsman'].head(5)
plt.bar(bats_name,run_count.values)
plt.title("Top 5 run scorer")
plt.xlabel("X axis = Batsman's name")
plt.ylabel("Y axis = Runs Scored" )
plt.tight_layout()
plt.savefig("Top 5 run scorer")
plt.show()

#Win % by team

import pandas as pd
df=pd.read_csv("matches.csv",encoding="latin1")
import matplotlib.pyplot as plt
df=df.dropna(subset=['winner'])
match_winner=df['winner'].value_counts()
plt.pie(match_winner,autopct="%1.1f%%")
plt.title("Wins by teams")
plt.tight_layout()
plt.savefig("Win % by team")
plt.show()

#Toss impact

import pandas as pd
df=pd.read_csv("matches.csv",encoding="latin1")
#print(df.columns)
import matplotlib.pyplot as plt
df=df.dropna(subset=['toss_winner','toss_decision'])
decision=df['toss_decision'].value_counts()
plt.barh(decision.index,decision.values)
plt.title("Toss impact")
plt.xlabel("X axis = filding/batting")
plt.ylabel("Y axis =Number")
plt.tight_layout()
plt.savefig("Toss impact")
plt.show()


#matchs per season
import pandas as pd
df=pd.read_csv("matches.csv",encoding="latin1")
import matplotlib.pyplot as plt
df=df.dropna(subset=['Season'])
match_peryer=df['Season'].value_counts()
plt.plot(match_peryer.index,match_peryer.values)
plt.title("matches per season")
plt.xlabel("X axis = Year")
plt.ylabel("Y axis = Matches")
plt.tight_layout()
plt.savefig("matchs per season")
plt.show()