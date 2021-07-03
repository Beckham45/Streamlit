import streamlit as st 
import pandas as pd
import numpy as np  


###############
#Adding a title
###############

st.title("Data visualization")


#Adding a text column
st.write("""
	Building Visualization applications is critical to achieve state of the art in 
	Artificial Intelligence
	""")


#Writing a dataframe
st.write(pd.DataFrame({
	'first column': [1,2,3,4],
	'second column': [10,20,30,40]

	}))

"""
# Visualizations are just beautiful
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

#####################
#Draw Charts and maps
#####################

chart_data = pd.DataFrame(
	np.random.randn(20, 3),
 	columns = ['a', 'b', 'c',]
 	)

st.line_chart(chart_data)


###################
#Plot  a map
###################
"""
#  A map containing lat and long coordinates which has been generated from a standard normal
"""
map_data = pd.DataFrame(
	np.random.randn(1000,2) / [50,50] + [38.76, -122.4],
	columns=['lat','lon'])

st.map(map_data)

################
#Adding widgets
################

if st.checkbox('Show map'):
	map_data2 = pd.DataFrame(
		np.random.randn(1000, 2) / [90,70] + [38.76, -122.4],
		columns=['lat', 'lon'])

	st.map(map_data2)



################
#Using Selectbox
################
option = st.selectbox(
	'Which number do you like best?',
	df['first column'])

'You selected: ', option


##############################################################
#LAying out the app
##############################################################


favourite_number = st.sidebar.selectbox(
	'Which number is your favorite?',
	df['first column'])

'You selected: ', favourite_number


###############################################
#Showing progress for long running computations
###############################################
import time 
#adding a placeholder


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
