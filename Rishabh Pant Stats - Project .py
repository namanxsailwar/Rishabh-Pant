#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df = pd.read_csv("deliveries.csv")


# In[3]:


df


# In[4]:


df.batting_team.unique()


# In[5]:


RP_df = df[df.batter == "RR Pant"]


# In[6]:


# Categories - Right-arm fast (RAF) / Right-arm fast-medium (RAFM), Left-arm fast (LAF) / Left-arm fast-medium (LAFM)
#  Right arm medium, left arem medium paser, Right-arm off-spin (RAOS), 
# Left-arm orthodox spin (LAOS), Right-arm leg-spin (RALG):, Left-arm unorthodox spin (Chinaman/LAUG),
# Mystery Bowlers


# ## Mystery Bowler

# In[7]:


MB = ["SP Narine","A Dananjaya","KC Cariappa"]


# In[8]:


RPvsMB = RP_df[RP_df['bowler'].isin(MB)]


# In[9]:


RPvsMB.head()


# In[10]:


RPvsMB["dots"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsMB["ones"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsMB["twos"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsMB["threes"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsMB["fours"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsMB["sixes"]=RPvsMB["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsMB.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsMB.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsMB.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsMB.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsMB.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsMB.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsMB.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsMB.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsMB.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsMB.groupby("bowler")["sixes"].sum()).reset_index()

rpmb=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")   


# In[71]:


rpmb.sort_values(by="runs",ascending=False)


# In[12]:


rpmb["RPI"] = rpmb.apply(lambda x: x["runs"]/x["innings"],axis=1)

rpmb["SR"] = rpmb.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

rpmb["BPB"]= rpmb.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


rpmb["BPD"]= rpmb.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[160]:


rpmb = rpmb.sort_values(by="runs", ascending=False)
rpmb


# In[175]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=rpmb.values,
    colLabels=rpmb.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(rpmb.columns))))

# Save the table as an image
output_path = "database_as_image.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Right-arm off-spin (RAOS)

# In[14]:


Raos = ["Harbhajan Singh","R Ashwin"
,"Washington Sundar"
,"J Yadav"
,"Jalaj S Saxena"
,"Shahbaz Ahmed"
,"HR Shokeen","SK Raina","MM Ali","TM Head","LS Livingstone","M Shahrukh Khan"]


# In[15]:


RPvsRaos =  RP_df[RP_df['bowler'].isin(Raos)]


# In[16]:


RPvsRaos.head()


# In[17]:


RPvsRaos["dots"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsRaos["ones"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsRaos["twos"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsRaos["threes"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsRaos["fours"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsRaos["sixes"]=RPvsRaos["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsRaos.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsRaos.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsRaos.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsRaos.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsRaos.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsRaos.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsRaos.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsRaos.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsRaos.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsRaos.groupby("bowler")["sixes"].sum()).reset_index()

RPvsRaos=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsRaos["RPI"] = RPvsRaos.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsRaos["SR"] = RPvsRaos.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsRaos["BPB"]= RPvsRaos.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsRaos["BPD"]= RPvsRaos.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[161]:


RPvsRaos = RPvsRaos.sort_values(by="runs",ascending=False)
RPvsRaos


# In[176]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsRaos.values,
    colLabels=RPvsRaos.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsRaos.columns))))

# Save the table as an image
output_path = "database_as_image1.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Left-arm orthodox spin (LAOS):

# In[35]:


Laos = ["RA Jadeja"
,"Iqbal Abdulla"
,"Axar Patel"
,"Shakib Al Hasan"
,"Harpreet Brar"
,"R Sai Kishore","Noor Ahmad","KH Pandya"]


# In[36]:


RPvsLaos = RP_df[RP_df["bowler"].isin(Laos)]


# In[37]:


RPvsLaos["dots"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsLaos["ones"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsLaos["twos"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsLaos["threes"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsLaos["fours"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsLaos["sixes"]=RPvsLaos["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsLaos.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsLaos.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsLaos.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsLaos.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsLaos.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsLaos.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsLaos.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsLaos.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsLaos.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsLaos.groupby("bowler")["sixes"].sum()).reset_index()

RPvsLaos=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsLaos["RPI"] = RPvsLaos.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsLaos["SR"] = RPvsLaos.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsLaos["BPB"]= RPvsLaos.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsLaos["BPD"]= RPvsLaos.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[162]:


RPvsLaos = RPvsLaos.sort_values(by="runs",ascending=False)
RPvsLaos


# In[183]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsLaos.values,
    colLabels=RPvsLaos.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsLaos.columns))))

# Save the table as an image
output_path = "database_as_image7.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Right-arm leg-spin (RALG):

# In[39]:


Ralg = ["A Zampa",
"YS Chahal",
"Rashid Khan",
"Imran Tahir",
"Kuldeep Yadav",
"Mujeeb Ur Rahman",
"M Markande",
"RD Chahar",
"IS Sodhi","KV Sharma"]


# In[40]:


RPvsRalg = RP_df[RP_df["bowler"].isin(Ralg)]


# In[41]:


RPvsRalg["dots"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsRalg["ones"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsRalg["twos"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsRalg["threes"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsRalg["fours"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsRalg["sixes"]=RPvsRalg["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsRalg.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsRalg.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsRalg.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsRalg.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsRalg.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsRalg.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsRalg.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsRalg.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsRalg.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsRalg.groupby("bowler")["sixes"].sum()).reset_index()

RPvsRalg=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsRalg["RPI"] = RPvsRalg.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsRalg["SR"] = RPvsRalg.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsRalg["BPB"]= RPvsRalg.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsRalg["BPD"]= RPvsRalg.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[163]:


RPvsRalg = RPvsRalg.sort_values(by="runs",ascending=False)
RPvsRalg


# In[178]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsRalg.values,
    colLabels=RPvsRalg.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsRalg.columns))))

# Save the table as an image
output_path = "database_as_image3.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Right-arm fast (RAF) / Right-arm fast-medium (RAFM)

# In[165]:


Raf = ["DS Kulkarni", "UT Yadav",
"AB Dinda",
"MM Sharma",
"Sandeep Sharma", "MJ McClenaghan"
"JJ Bumrah","Basil Thampi", "SL Malinga","Navdeep Saini",
"AJ Tye",
"L Ngidi",
"TG Southee",
"LH Ferguson",
"Mohammed Shami",
"K Rabada",
"JR Hazlewood",
"KA Jamieson",
"JA Richardson",
"Kartik Tyagi",
"PVD Chameera",
"TU Deshpande",
"Simarjeet Singh",
"Naveen-ul-Haq",
"Yash Thakur", "BA Stokes","MP Stoinis", "CH Morris","C de Grandhomme"]


# In[166]:


RPvsRaf = RP_df[RP_df["bowler"].isin(Raf)]


# In[167]:


RPvsRaf["dots"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsRaf["ones"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsRaf["twos"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsRaf["threes"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsRaf["fours"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsRaf["sixes"]=RPvsRaf["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsRaf.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsRaf.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsRaf.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsRaf.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsRaf.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsRaf.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsRaf.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsRaf.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsRaf.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsRaf.groupby("bowler")["sixes"].sum()).reset_index()

RPvsRaf=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsRaf["RPI"] = RPvsRaf.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsRaf["SR"] = RPvsRaf.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsRaf["BPB"]= RPvsRaf.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsRaf["BPD"]= RPvsRaf.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[169]:


RPvsRaf = RPvsRaf.sort_values(by="runs",ascending=False)
RPvsRaf


# In[180]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsRaf.values,
    colLabels=RPvsRaf.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsRaf.columns))))

# Save the table as an image
output_path = "database_as_image4.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Left-arm fast (LAF) / Left-arm fast-medium (LAFM)

# In[31]:


Laf = ["T Natarajan",
"TA Boult",
"OC McCoy"
"MA Starc","C Sakariya", "Arshdeep Singh","JD Unadkat","Mustafizur Rahman","A Nehra","IK Pathan","JP Faulkner"]


# In[32]:


RPvsLaf = RP_df[RP_df["bowler"].isin(Laf)]


# In[33]:


RPvsLaf["dots"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsLaf["ones"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsLaf["twos"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsLaf["threes"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsLaf["fours"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsLaf["sixes"]=RPvsLaf["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsLaf.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsLaf.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsLaf.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsLaf.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsLaf.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsLaf.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsLaf.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsLaf.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsLaf.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsLaf.groupby("bowler")["sixes"].sum()).reset_index()

RPvsLaf=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsLaf["RPI"] = RPvsLaf.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsLaf["SR"] = RPvsLaf.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsLaf["BPB"]= RPvsLaf.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsLaf["BPD"]= RPvsLaf.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[170]:


RPvsLaf = RPvsLaf.sort_values(by="runs",ascending=False)
RPvsLaf


# In[181]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsLaf.values,
    colLabels=RPvsLaf.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsLaf.columns))))

# Save the table as an image
output_path = "database_as_image2.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Medium Pacers

# In[59]:


MP = ["Nithish Kumar Reddy","Azmatullah Omarzai","S Sandeep Warrier","DR Smith","AD Russell",
    "STR Binny","SR Watson","R Bhatia", "DJ Bravo", "KA Pollard", "Ramandeep Singh"]


# In[60]:


RPvsMP = RP_df[RP_df["bowler"].isin(MP)]


# In[61]:


RPvsMP["dots"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==0 else 0) 
RPvsMP["ones"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==1 else 0)
RPvsMP["twos"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==2 else 0)
RPvsMP["threes"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==3 else 0)
RPvsMP["fours"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==4 else 0)
RPvsMP["sixes"]=RPvsMP["batsman_runs"].apply(lambda x: 1 if x==6 else 0)

Runs=pd.DataFrame(RPvsMP.groupby("bowler")["batsman_runs"].sum()).reset_index().rename(columns={"batsman_runs":"runs"})

Innings = pd.DataFrame(RPvsMP.groupby("bowler")["match_id"].apply(lambda x: len(list(np.unique(x))))).reset_index().rename(columns={"match_id":"innings"})

Balls = pd.DataFrame(RPvsMP.groupby("bowler")["match_id"].count()).reset_index().rename(columns={"match_id":"balls"})

Dismissals = pd.DataFrame(RPvsMP.groupby("bowler")["player_dismissed"].count()).reset_index().rename(columns={"player_dismissed":"dismissals"})

Dots = pd.DataFrame(RPvsMP.groupby("bowler")["dots"].sum()).reset_index()

Ones=pd.DataFrame(RPvsMP.groupby("bowler")["ones"].sum()).reset_index()
Twos=pd.DataFrame(RPvsMP.groupby("bowler")["twos"].sum()).reset_index()
Threes=pd.DataFrame(RPvsMP.groupby("bowler")["threes"].sum()).reset_index()
Fours=pd.DataFrame(RPvsMP.groupby("bowler")["fours"].sum()).reset_index()
Sixes=pd.DataFrame(RPvsMP.groupby("bowler")["sixes"].sum()).reset_index()

RPvsMP=pd.merge(Runs,Innings,on="bowler",how="right").merge(Balls,on="bowler").merge(Dismissals,on="bowler").merge(Dots,on="bowler").merge(Ones,on="bowler").merge(Twos,on="bowler").merge(Threes,on="bowler").merge(Fours,on="bowler").merge(Sixes,on="bowler")
RPvsMP["RPI"] = RPvsMP.apply(lambda x: x["runs"]/x["innings"],axis=1)

RPvsMP["SR"] = RPvsMP.apply(lambda x: 100*(x["runs"]/x["balls"]),axis=1)

RPvsMP["BPB"]= RPvsMP.apply(lambda x: (x["balls"]/(x["fours"]+x["sixes"])) if (x["fours"]+x["sixes"])!= 0 else 0,axis=1)


RPvsMP["BPD"]= RPvsMP.apply(lambda x: (x["balls"]/x["dismissals"]) if (x["dismissals"]) != 0 else 0, axis=1)


# In[171]:


RPvsMP = RPvsMP.sort_values(by="runs",ascending=False)
RPvsMP


# In[182]:


fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the size as needed

# Hide axes
ax.axis('off')

# Create a table
table = plt.table(
    cellText=RPvsMP.values,
    colLabels=RPvsMP.columns,
    cellLoc='center',
    loc='center'
)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(RPvsMP.columns))))

# Save the table as an image
output_path = "database_as_image5.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the table (optional)
plt.show()

print(f"Table saved as {output_path}.")


# ### Combined Data

# In[79]:


combined_df = pd.concat([rpmb,RPvsMP,RPvsLaf, RPvsRaf, RPvsRalg, RPvsLaos, RPvsRaos], ignore_index=True)


# In[88]:


combined_df = combined_df.sort_values(by="runs", ascending= False)


# In[89]:


combined_df


# ### Making of the dataset visualization

# In[141]:


data = {
    "Bowler_Type": ["Right Arm Fast","Left Arm Fast", "Medium", "Off-spin", "Leg-spin", "Left-arm Spin","Mystery Spin"],
    "Runs": [451,204,213,281,372,210,81],
    "Dismissals": [14, 4,7,4,13,5,0],
    "Strike_Rate": [153.4, 146.7, 144.8,127.1,135.7,155.5,142.2],
    "Sixes": [23,12,11,13,14,11,3]}
    


# In[156]:


data = pd.DataFrame(data)
data


# In[92]:


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[143]:


plt.figure(figsize=(8, 5))
sns.barplot(x="Bowler_Type", y="Runs", data=data, palette="coolwarm")
plt.title("Runs Scored by Rishabh Pant Against Different Bowler Types")
plt.ylabel("Runs")
plt.xlabel("Bowler Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[158]:


plt.savefig("rishabh_pant_vs_bowlers.png", dpi=300, bbox_inches="tight")


# In[159]:


from IPython.display import FileLink
FileLink("rishabh_pant_vs_bowlers.png")


# In[144]:


plt.figure(figsize=(6, 6))
plt.pie(data["Dismissals"], labels=data["Bowler_Type"], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("Dismissals Distribution Against Different Bowler Types")
plt.show()


# In[ ]:





# In[145]:


import pandas as pd
import numpy as np

df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
sns.heatmap(df.pivot_table(index="Bowler_Type", values="Strike_Rate"), annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Strike Rate Against Different Bowler Types")
plt.xlabel("Metrics")
plt.ylabel("Bowler Type")
plt.tight_layout()
plt.show()


# In[ ]:





# In[146]:


from math import pi
import pandas as pd

df = pd.DataFrame(data)
categories = list(df["Bowler_Type"])
metrics = ['Strike_Rate', 'Sixes']

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

for metric in metrics:
    values = df[metric].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=metric)
    ax.fill(angles, values, alpha=0.25)

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
plt.legend(loc='upper right')
plt.title("Comparative Metrics of Rishabh Pant Against Bowler Types")
plt.show()


# In[ ]:





# In[147]:


fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar plot for sixes
sns.barplot(x="Bowler_Type", y="Sixes", data=data, palette="magma", ax=ax1)
ax1.set_ylabel("Sixes", color="purple")
ax1.tick_params(axis="y", labelcolor="purple")
ax1.set_xticklabels(data["Bowler_Type"], rotation=45)

# Line plot for strike rate
ax2 = ax1.twinx()
sns.lineplot(x="Bowler_Type", y="Strike_Rate", data=data, marker="o", color="blue", ax=ax2)
ax2.set_ylabel("Strike Rate", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

plt.title("Sixes and Strike Rate Against Bowler Types")
plt.tight_layout()
plt.show()


# In[ ]:





# In[148]:


import numpy as np

fig, ax = plt.subplots(figsize=(8, 5))
width = 0.4
x = np.arange(len(data["Bowler_Type"]))

ax.barh(x - width/2, data["Runs"], width, label="Runs", color="green")
ax.barh(x + width/2, data["Dismissals"], width, label="Dismissals", color="red")

ax.set_yticks(x)
ax.set_yticklabels(data["Bowler_Type"])
ax.set_xlabel("Metrics")
ax.set_title("Runs and Dismissals Against Bowler Types")
ax.legend()
plt.tight_layout()
plt.show()


# In[ ]:




