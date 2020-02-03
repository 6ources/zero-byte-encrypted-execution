import subprocess
from tkinter import *	
from tkinter import messagebox
import xlwt 
from xlwt import Workbook 

#dictionary

data ={
'jalandhar' : {
	 "a":"ludhiana",
	"ad":"61",
	"at":"00:50",
	"an":"south-east",
	 "b":"patiala",
	"bd":"93",
	"bt":"01:30",
	"bn":"south-east",
 	 "c":"chandigarh",
	"cd":"75",
	"ct":"01:20", 
	"cn":"north-west",
	 "d":"amritsar",
	"dd":"229",
	"dt":"03:00",
	"dn":"west",
	 "e":"jalandhar(home)",
	"ed":"80",
	"et":"01:10",
	"en":"south-east",
	"nav":"https://goo.gl/maps/ZkmBTfPMyr8Whsbw5",
	"lat":31.3260,
	"lon":75.5762
	}, 
'amritsar' : {
	 "a":"jalandhar",
	"ad":"80",
	"at":"01:10",
	"an":"south-east",
	 "b":"ludhiana",
	"bd":"61",
	"bt":"00:50",
	"bn":"south-east",
	 "c":"patiala",
	"cd":"93",
	"ct":"01:30",	
	"cn":"south-east",
	 "d":"chandigarh",
	"dd":"75",
	"dt":"01:20",
	"dn":"east",
	 "e":"amritsar(home)",
	"ed":"229",
	"et":"03:00",
	"nav":"https://goo.gl/maps/59MNdnZVskiMJAPb9",
	"lat":31.6340,
	"lon":74.8723
	},
'ludhiana' : {
	 "a":"jalandhar",
	"ad":"61",
	"at":"00:50",
	"an":"west",
	 "b":"amritsar",
	"bd":"80",
	"bt":"01:10",
	"bn":"west",
	 "c":"chandigarh",
	"cd":"229",
	"ct":"01:30",
	"cn":"south-east",	
	 "d":"patiala",
	"dd":"75",
	"dt":"01:20",
	"dn":"east",
	 "e":"ludhiana(home)",
	"ed":"93",
	"et":"01:30",
	"en":"west",
	"nav":"https://goo.gl/maps/HrMxXAtgrDUur64Q9",
	"lat":30.9010,
	"lon":75.8573
	},
'chandigarh' : {
	 "a":"patiala",
	"ad":"75",
	"at":"01:20",
	"an":"west",
	 "b":"ludhiana",
	"bd":"93",
	"bt":"01:30",
	"bn":"west",
	 "c":"jalandhar",
	"cd":"61",
	"ct":"00:50",
	"cn":"west",	
	 "d":"amritsar",
	"dd":"80",
	"dt":"01:10",
	"dn":"west",
	 "e":"chandigarh(home)",
	"ed":"229",
	"et":"03:00",
	"en":"west",
	"nav":"https://goo.gl/maps/hKv8Wu7PNkpofHMW7",
	"lat":30.7333,
	"lon":76.7794
	},
'patiala' : {
	 "a":"chandigarh",
	"ad":"75",
	"at":"01:20",
	"an":"west",
	 "b":"ludhiana",
	"bd":"106",
	"bt":"02:00",
	"bn":"south-west",
	 "c":"jalandhar",
	"cd":"61",
	"ct":"00:50",	
	"cn":"west",
	 "d":"amritsar",
	"dd":"80",
	"dt":"01:10",
	"dn":"west",
	 "e":"patiala(home)",
	"ed":"235",
	"et":"03:00",
	"en":"south-east",
	"nav":"https://goo.gl/maps/te3TbmS16HqFQT5e8",
	"lat":30.3398,
	"lon":76.3869
	}
	}
	#functions
def click():
		#clear input
		output.delete(0.0,END)
		try:
			entered = location.get()
			output.insert(END,data[entered]["a"] + " is "+ data[entered]["ad"] + " km far from here ,\n")
			output.insert(END,data[entered]["b"] +"  is "+ data[entered]["bd"] + " km far from " + data[entered]["a"] +",\n")
			output.insert(END,data[entered]["c"] + " is "+ data[entered]["cd"] + " km far from " + data[entered]["b"] +",\n")
			output.insert(END,data[entered]["d"] + " is "+ data[entered]["dd"] + " km far from " + data[entered]["c"] +",\n")
			output.insert(END,data[entered]["e"] + " will be "+ data[entered]["ed"] + " km far from " + data[entered]["d"]+".\n")
			
		except:
			final = "sorry can't help in this route"
			output.insert(END,final)

def printer():
		entered = location.get()
		# Workbook is created 
		wb = Workbook() 

		# add_sheet is used to create sheet. 
		data1 = wb.add_sheet('instructions') 
		#col-01
		data1.write(0, 0, 'From city') 
		data1.write(1, 0, data[entered]["e"]) 
		data1.write(2, 0, data[entered]["a"])
		data1.write(3, 0, data[entered]["b"])
		data1.write(4, 0, data[entered]["c"])
		data1.write(5, 0, data[entered]["d"])
		#col-02
		data1.write(0, 1, 'To city') 
		data1.write(1, 1, data[entered]["a"]) 
		data1.write(2, 1, data[entered]["b"])
		data1.write(3, 1, data[entered]["c"])
		data1.write(4, 1, data[entered]["d"])
		data1.write(5, 1, data[entered]["e"])
		#col-03
		data1.write(0, 2, 'Distance (km)') 
		data1.write(1, 2, data[entered]["ad"]) 
		data1.write(2, 2, data[entered]["bd"])
		data1.write(3, 2, data[entered]["cd"])
		data1.write(4, 2, data[entered]["dd"])
		data1.write(5, 2, data[entered]["ed"])
		#col-04
		data1.write(0, 3, 'Time')
		data1.write(1, 3, data[entered]["at"]) 
		data1.write(2, 3, data[entered]["bt"])
		data1.write(3, 3, data[entered]["ct"])
		data1.write(4, 3, data[entered]["dt"])
		data1.write(5, 3, data[entered]["et"])
		#col-05
		data1.write(0, 4, 'Direction')
		data1.write(1, 4, data[entered]["an"]) 
		data1.write(2, 4, data[entered]["bn"])
		data1.write(3, 4, data[entered]["cn"])
		data1.write(4, 4, data[entered]["dn"])
		data1.write(5, 4, data[entered]["en"])

		#col-06
		data1.write(0, 5, 'Google Navigation (link)')
		data1.write(1, 5, data[entered]["nav"]) 
		
		wb.save('instruction.xls')
		messagebox.showinfo('status','your file has been exported.\ncheck the working directory.')




def mapping():
		#---------------------------------------------------------------
		from mpl_toolkits.basemap import Basemap
		import matplotlib.pyplot as plt
		entered = location.get()
		map = Basemap(
			projection='mill',
			llcrnrlat=1.274271,
			llcrnrlon=56.476081,
			urcrnrlat=38.135286,
			urcrnrlon=106.199909,
			resolution='l'
			
		)
		#test streetview
#		map.arcgisimage(service='ESRI_StreetMap_World_2D',xpixels=1500,verbose=True)epsg=3857
		map.drawcountries()
		map.drawcoastlines()
		map.drawstates(color='g')
		map.bluemarble()
		plt.title("map view")
		#plt.text()
		#plotting
		xs=[]
		ys=[]
		lat,lon =data[entered]["lat"],data[entered]["lon"]
		
		xpt,ypt=map(lat,lon)
		plt.text(xpt,ypt,'abc',fontsize=12,fontweight='bold',color='k',bbox=dict(facecolor='b',alpha=0.2))	
		xs.append(xpt)
		ys.append(ypt)
		map.plot(xpt,ypt,'c*',markersize=105)
		#location lat lon grab
		aloc=data[entered]["a"]
		bloc=data[entered]["b"]
		cloc=data[entered]["c"]
		dloc=data[entered]["d"]
		#dictionary grab
		alat,alon=data[aloc]["lat"],data[aloc]["lon"]
		blat,blon=data[bloc]["lat"],data[bloc]["lon"]
		clat,clon=data[cloc]["lat"],data[cloc]["lon"]
		dlat,dlon=data[dloc]["lat"],data[dloc]["lon"]
		#marker
		map.scatter(data[entered]["lon"],data[entered]["lat"],latlon=True,s=50,c='red',marker='^',edgecolor='white',zorder=1)
		map.scatter(data[aloc]["lon"],data[aloc]["lat"],latlon=True,s=50,c='blue',marker='o',edgecolor='white',zorder=1)
		map.scatter(data[bloc]["lon"],data[bloc]["lat"],latlon=True,s=50,c='green',marker='o',edgecolor='white',zorder=1)
		map.scatter(data[cloc]["lon"],data[cloc]["lat"],latlon=True,s=50,c='yellow',marker='o',edgecolor='white',zorder=1)
		map.scatter(data[dloc]["lon"],data[dloc]["lat"],latlon=True,s=50,c='black',marker='o',edgecolor='white',zorder=1)

		map.drawgreatcircle(lon,lat,alon,alat,color='violet',linewidth=2,label='a')
		map.drawgreatcircle(alon,alat,blon,blat,color='blue',linewidth=2,label='b')
		map.drawgreatcircle(blon,blat,clon,clat,color='g',linewidth=2,label='c')
		map.drawgreatcircle(clon,clat,dlon,dlat,color='y',linewidth=2,label='d')
		map.drawgreatcircle(dlon,dlat,lon,lat,color='orange',linewidth=2,label='e')

		plt.show()






#------------------------------------------------------------------------------------------------------------


def nav():
		entered = location.get()
		subprocess.call("x-www-browser " + data[entered]["nav"],shell=True)
	
def exit():
		window.destroy()




	

#head

window=Tk()
window.title("travelling salesman navigator")
#SIZING & window config
window.geometry('1000x500')
window.configure(background="brown")
#logo & title
#icom=PhotoImage(file='icom.png')
#Label(window,image=icom,bg="white").grid(row=0,column=0,sticky=W,pady=(10,10),padx=(400,1))
Label(window,text="Travelling Salesman Navigator",fg="black",font="none 16 bold").grid(row=0,column=1,sticky=W)

#intros
Label(window,text="Hi there,",fg="black",font="none 12 bold").grid(row=2,column=0,sticky=W ,padx=10,pady=5)
Label(window,text="Where are you now?...",fg="black",font="none 12 bold").grid(row=3,column=0,sticky=W,padx=10,pady=(0,5))

#inputs
location = Entry(window,width=35,bg="green",fg="white")
location.grid(row=4,column=0,sticky=W,padx=(60,10),pady=(25,10))
#submit
Button(window,text="submit",command=click,width=6,fg="white",bg="red").grid(row=5,column=0,sticky=W,padx=(160,10),pady=(0,25))
#outputbox
output=Text(window,width=50,height=10,wrap=WORD,background="white")
output.grid(row=6,column=0,columnspan=2,sticky=W,padx=10,pady=(0,5))
#map
Button(window,text="show the plotted map",bg="skyblue",fg="black",command=mapping).grid(sticky=W,row=5,column=1,padx=(100,10),pady=10)
#print route
Button(window,text="Print this route information",fg="black",bg="yellow",command=printer).grid(row=7,column=0,sticky=W,padx=(100,10),pady=10)
#gNav
Button(window,text="Open GOOGLE Navigation in the browser",fg="black",bg="limegreen",command=nav).grid(row=6,column=1,sticky=W,padx=(100,10),pady=(0,5))
Button(window,text="exit",bg="white",fg="red",command=exit).grid(row=7,column=1,sticky=W,padx=(440,10),pady=(10,10))

#end
window.mainloop()



