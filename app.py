import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
)

st.write('Did seniors have a higher or lower survival rate than other age groups?')

# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)
st.markdown('*The answer seems to be that there is not a significant difference with seniors, as there is with children.*')


st.write(
'''
# Titanic Visualization 2
'''
)

st.write('Did passengers with larger families have lower fares?')
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)
st.markdown("""*It seems that passengers with larger families may have had higher fares, 
but to better confirm we would have to also look at how the family size relates to other
factors such as class and age.*""")

st.markdown('**')


# st.write(
# '''
# # Titanic Visualization Bonus
# '''
# )
# # Generate and display the figure
# fig3 = visualize_family_size()
# st.plotly_chart(fig3, use_container_width=True)