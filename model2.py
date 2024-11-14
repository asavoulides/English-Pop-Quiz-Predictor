import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    'Type': ['Annotation Check', 'Annotation Check', 'Reading Quiz', 'Annotation Check', 'Annotation Check', 
             'Annotation Check', 'Reading Quiz', 'Annotation Check', 'N/A', 'N/A', 'Reading Quiz', 'Annotation Check',
             'Annotation Check', 'Annotation Check', 'Annotation Check', 'Annotation Check', 'Annotation Check',
             'Annotation Check', 'Annotation Check', 'Reading Quiz', 'Annotation Check', 'Annotation Check',
             'Annotation Check', 'Annotation Check', 'Annotation Check', 'Annotation Check', 'N/A', 'N/A',
             'Reading Quiz', 'Annotation Check', 'Annotation Check', 'Annotation Check', 'Reading Quiz',
             'Annotation Check', 'Annotation Check', 'Annotation Check', 'Annotation Check', 'Annotation Check',
             'Annotation Check', 'Annotation Check', 'Annotation Check', 'Reading Quiz', 'Annotation Check',
             'Annotation Check'],
    'Date': ['9/18/2023', '9/19/2023', '9/20/2023', '9/22/2023', '9/26/2023', '9/27/2023', '9/29/2023', 
             '10/3/2023', '10/10/2023', '10/11/2023', '10/11/2023', '10/16/2023', '10/17/2023', '10/18/2023', 
             '10/20/2023', '10/23/2023', '10/24/2023', '10/25/2023', '10/27/2023', '10/31/2023', '11/1/2023', 
             '11/3/2023', '11/6/2023', '11/28/2023', '11/29/2023', '12/1/2023', '12/4/2023', '12/5/2023', 
             '12/6/2023', '1/22/2024', '1/23/2024', '1/24/2024', '1/29/2024', '1/30/2024', '1/31/2024', '2/2/2024',
             '2/5/2024', '2/6/2024', '2/7/2024', '2/9/2024', '2/13/2024', '5/6/2024', '5/7/2024', '5/8/2024'],
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Tuesday', 'Wednesday', 'Friday', 'Tuesday', 'Tuesday',
            'Wednesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Tuesday', 'Wednesday',
            'Friday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 
            'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday', 'Friday',
            'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Tuesday', 'Monday', 'Tuesday', 'Wednesday']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Type'] == 'Reading Quiz']  # Filter only Reading Quizzes

quiz_counts = df['Day'].value_counts()
quiz_counts = quiz_counts.sort_index()

# Plot the frequency of quizzes by day of the week
plt.figure(figsize=(10, 6))
quiz_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Reading Quizzes by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Quizzes')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
