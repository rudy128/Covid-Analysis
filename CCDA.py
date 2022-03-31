from os import *
from tkinter import *
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np



clearconsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear')


path=getcwd()

def tkinter_window():
	root=Tk()
	root.title("Choose Your CSV File")
	root.filename=filedialog.askopenfilename(initialdir=path, title="Select A File")
	root.destroy()
	return root.filename


def csv():
	data = pd.read_csv(tkinter_window())
	datas={}
	datas1={}
	names=data["State"].tolist()
	conf_case=data["Confirmed"].tolist()
	reco_case=data["Recovered"].tolist()
	death_case=data["Deaths"].tolist()
	active_case=data["Active"].tolist()
	total=data["Total"].tolist()
	for i in range(len(conf_case)):
		datas[conf_case[i]]=names[i]
		datas1[names[i]]=reco_case[i],death_case[i],active_case[i]
	ch='y'
	while ch=='y' or ch=='yes':
		clearconsole()
		choice=int(input("""
Welcome to the Covid Cases Analysis System (CCAS)

Please Choose between 1-6:
1. To analyze the Covid Cases of different states.
2. To Calculate Total and Percentage of active, recovered, deceased and confirmed cases
3. To find Top States
4. To compare different states on the basis of increased cases of deaths due to covid or increased cases of recovered people.
5. To show graphically number and percentage of active, recovered, deceased and confirmed cases with in a state.
6. To Show Graphically percentage of active, recovered, deceased, confirmed cases in whole country

Your Choice:- """))
		clearconsole()

		if choice==1:
			fig1,ax1=plt.subplots()
			ax1.barh(list(datas.values()),list(datas.keys()),color="crimson")
			plt.show()
		elif choice==2:
			print(f"""Total Confirmed Cases are={total[0]}
Total Recovered Cases= {total[1]}
Percentage of Recovered Cases or Recovery rate= {(total[1]/total[0])*100}
Total Death Cases= {total[2]}
Percentage Death Cases= {(total[2]/total[0])*100}
Total Active Cases= {total[3]}
Percentage of Active Cases= {(total[3]/total[0])*100}\n""")
		elif choice==3:
			first3={}
			counter=0
			for i in sorted(datas.keys())[::-1]:
				first3[i]=datas[i]
				if counter==9:
					break
				counter+=1

			print(f"""Top States are:
       States\t\tNo. of Cases""")
			count=1
			for i in first3.keys():
				print(f"{count}.{first3[i]}\t\t{i}")
				count+=1

		elif choice==4:
			compare1=input("Enter the State Name You wanna Compare= ")
			compare2=input("Enter the State Name You wanna compare with= ")
			if compare1 in datas1.keys() and compare2 in datas1.keys():
				state1=datas1[compare1]
				state2=datas1[compare2]
				print(f"""{compare1}\t\t\t\t\t{compare2}
No. of Recovered Cases={state1[0]}\t\tNo. of Recovered Cases={state2[0]}
No. of Death Cases={state1[1]}\t\tNo. of Death Cases={state2[1]}""")
			else:
				print("Wrong State name please try again")
		elif choice==5:
			compare1=input("Enter the name of State")
			if compare1 in datas1.keys():
				plt.pie(datas1[compare1],labels=["Recovered Cases","Death Cases","Active Cases"],explode=[0,0.6,0.6],shadow=True)
				plt.show()

		elif choice==6:
			fix,ax=plt.subplots(figsize=(10,7))
			ax.barh(["Recovered","Deaths","Active"],[total[1],total[2],total[3]])
			plt.title("Analysis of Number of cases in India")
			plt.show()
		ch=input("Do you wanna Continue?\n:-")


csv()
