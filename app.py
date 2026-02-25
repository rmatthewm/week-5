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

st.write("""
For the comparison between the family_groups() and last_names(), I feel like they do not
have a direct comparison because they are looking at different things. If I understand
correctly, family_groups() is looking more at how the fare relates to family size, so had to modify it
to get a direct comparison with last_names().

However, estimating the number of families of different sizes by using unique last names seems
to give a pretty similar result compared to the family_groups(). It also seems to be significantly more accurate
for identifying individuals than for finding larger families.
""")

# st.write(
# '''
# # Titanic Visualization Bonus
# '''
# )
# # Generate and display the figure
# fig3 = visualize_family_size()
# st.plotly_chart(fig3, use_container_width=True)