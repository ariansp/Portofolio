import base64
import streamlit as st
import pandas as pd
import googleapiclient.discovery
from pathlib import Path
from PIL import Image
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# --- PATH SETTINGS ---
css_file = "main.css"
resume_file = "CV.pdf"
porto_file = "Portofolio - Big 5 Personalities .pdf"
profile_pic = "profile-pic1.png"

# Set the title and a brief description
st.title("Portfolio")
st.write("Arian Syah Putra | Data Analyst | Data Engineer.")

# Add a sidebar with options
st.sidebar.title("Section")
selected_page = st.sidebar.selectbox("Menu", ["About Me", "Youtube Scrap", "Dashboard & ML"])

if selected_page is None:
    selected_page = "About Me"

if selected_page == "About Me":
    st.write("Welcome to my portfolio!")
    # --- GENERAL SETTINGS ---
    NAME = "Arian Syah Putra"
    DESCRIPTION = """
    Experienced in addressing real-world challenges, I excel in both collaborative teams and independent problem-solving. My strong
communication and leadership skills, honed through hands-on experience, make me an effective asset. Specializing in Data Engineer and
Data Analysis to enhance your data team.
    """
    EMAIL = "Ariansp08@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://linkedin.com/in/ariansyahputra",
        "GitHub": "https://github.com/ariansp",
        "Portofolio": "https://drive.google.com/drive/folders/1qBKCV_oZlt3Y8zsWHAIW3oAbqR9s7gkm?usp=sharing"
    }
    
    # --- LOAD CSS, PDF & PROFILE PIC ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.text("")
        st.text("")
        st.image(profile_pic, width=None, output_format="auto")

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=Path(resume_file).name,
            mime="application/octet-stream",
        )
        st.download_button(
            label=" 📄 Download Portofolio",
            data=PDFbyte,
            file_name=Path(porto_file).name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Education & Certification")
    st.write("08/2019 - 06/2023")
    st.write(
        """
    - ✔️ B.CompSc. Computer Science, North Sumatera University, Indonesia (Cumlaude, 3.78/4.00)
    """
    )
    st.write("08/2022 - 12/2022")
    st.write(
        """
    - ✔️ Data Analyst Study Independent, MyEduSolve, Indonesia (4.00/4.00) 
    """
    )
    st.write("2022")
    st.write(
        """
    - ✔️ [Data Analytics Certification](https://www.credly.com/badges/fb421988-9b39-472c-9be6-f6b0d9c7b338/public_url), Certiport 
    - ✔️ [Database Certification](https://www.credly.com/badges/3c60bc6d-9a1b-41bd-9d04-f712063dd19d/public_url), Certiport  
    - ✔️ [Microsoft Excel 2019 Expert](https://www.credly.com/badges/f6c0e511-37a3-4945-be63-6fc5a17844a2/public_url), Microsoft 
    - ✔️ [Microsoft Excel 2019 Associate](https://www.credly.com/badges/e8945665-6188-48eb-bdb5-7173126ad740/public_url), Microsoft 
    """
    )
    st.write("---")

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python, SQL, Java, C/C++, Spark
    - 📊 Data Visulization & Tools: PowerBi, MS Excel, Spreadsheet, Power Automate, Powerapps, Azure Databricks, Azure Datafactory, Azure Data Warehouse
    - 🗄️ Databases: PostgreSQl, MySQL
    """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Business Intellegence Specialist | OCS Group Indonesia**")
    st.write("11/2023 - Present")
    st.write(
        """
    - ► Crafting interactive data visualizations on maintenance, employee attendance, and performance metrics, Empower operational teams with actionable insights for informed decision-making. Transforming raw data into dynamic visuals enhances efficiency and productivity.
    - ► Maximizing Power BI efficiency, I orchestrate near real-time data preprocessing using Azure Data Factory and Azure Databricks. This dynamic approach ensures seamless integration and transformation, significantly enhancing data analysis and reporting performance.
    - ► Python-based data scraping to generate news updates from various news portals. This automated process efficiently gathers relevant information, providing timely news updates for analysis and dissemination
        """
    )

    # --- JOB 2
    st.write("🚧", "**Data Engineer Freelance | Windata**")
    st.write("07/2023 - 11/2023")
    st.write(
        """
    - ► Armed with RapidAPI, I became a data detective. Imagine crafting queries to fetch real-time data, maneuvering around rate limits, and uncovering trends and sentiments. Each API call felt like solving a puzzle, revealing stories hidden in the data
    - ► Utilized Python and Torch to optimize data processing and improve query performance, reducing processing time
    - ► My meticulous data cleaning skills included error rectification and noise reduction, resulting in pristine datasets
    - ► Expertly engineered features, encoded data, and scaled variables for optimized data readiness.
    - ► Harnessed Streamlit to craft interactive, user-friendly data visualizations and dashboards
    - ► Beyond the technical aspect, I have focused on enhancing user experiences by making data accessible and insightful, ultimately empowering decision-makers to drive impactful outcomes.
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst Freelance | Windata**")
    st.write("12/2022 - 06/2023")
    st.write(
        """
    - ► Proficiently managed and analyzed data encompassing sentiment analysis, with a particular focus on prevailing topics in Indonesia. Employed advanced techniques to classify sentiments into negative, neutral, and positive categories
    - ► Visualized and disseminated findings effectively on [@remajajompoid • Instagram](https://instagram.com/remajajompoid)
    - ► Compiled, studied, and inferred large amounts of data
    """
    )

    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects")
    st.write(
        """
    - ► [Big Five Personalities with K-Mean Clustering](https://www.canva.com/design/DAFtZSHbnUI/Yl-bMlE8tg9ggzjZzfO6SA/edit?utm_content=DAFtZSHbnUI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), MyEduSolve Study Independent
    - ► Visualized and disseminated findings effectively on [@remajajompoid • Instagram](https://instagram.com/remajajompoid)
    - ► Implemented Youtube scraped to [Streamlit](https://ariansp-porto.streamlit.app/)
    """
    )
    st.write("---")

elif selected_page == "Youtube Scrap":
    st.header("YouTube Scrap")

    # Input field to enter the YouTube video link ID
    video_link_id = st.text_input("Enter YouTube Video Link :")

    if video_link_id:
        # Function to extract video ID from the link ID
        def extract_video_id(video_link_id):
            # Extract the video ID from the link ID
            if "youtube.com/watch?v=" in video_link_id:
                video_id = video_link_id.split("v=")[1].split("&")[0] # https://www.youtube.com/watch?v=SjkFTqmgegA
        # Check if the input is a short YouTube URL
            elif "youtu.be" in video_link_id: #https://youtu.be/B-gHb2gPGIs?feature=shared
                video_id = video_link_id.split("?")[0].split("/")[-1]
        # Handle other formats or invalid inputs
            else:
                st.warning("Invalid YouTube link. Please enter a valid YouTube video link.")
                return None
            return video_id

        # Extract the video ID from the provided link ID
        video_id = extract_video_id(video_link_id)

        # Second video_comments function
        def video_comments_max(video_id, max_comments=100):
            replies = []
            api_service_name = "youtube"
            api_version = "v3"
            DEVELOPER_KEY = st.secrets["api_key"]  # Replace with your own YouTube API key

            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=DEVELOPER_KEY
            )

            df_list = []

            next_page_token = None
            total_comments = 0

            while total_comments < max_comments:
                request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId=video_id,
                    pageToken=next_page_token
                )
                video_response = request.execute()

                for item in video_response["items"]:
                    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    user_name = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
                    reply_count = item["snippet"]["totalReplyCount"]

                    if reply_count > 0:
                        for reply in item["replies"]["comments"]:
                            reply_text = reply["snippet"]["textDisplay"]
                            replies.append(reply_text)

                    df_list.append({
                        "user_name": user_name,
                        "comment": comment,
                        "replies": replies.copy(),
                    })
                    replies.clear()

                    total_comments += 1

                    if total_comments >= max_comments:
                        break

                if "nextPageToken" in video_response:
                    next_page_token = video_response["nextPageToken"]
                else:
                    break

            df = pd.DataFrame(df_list)
            return df

        # Call the second function with the extracted video ID and limit
        limit_comments = 100
        comments_df_limit = video_comments_max(video_id, max_comments=limit_comments)

        # Display the scraped comments with a limit
        st.subheader(f"Scraped comments from YouTube video (limited to {limit_comments} comments):")
        st.dataframe(comments_df_limit)

        def download_data(dataframe, filename):
            csv = dataframe.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download {filename} CSV</a>'
            return href

        if st.button("Download Scraped Data"):
            st.markdown(download_data(comments_df_limit, "youtube_comments"), unsafe_allow_html=True)

elif selected_page == "Dashboard &":

    option = st.sidebar.selectbox("Dashboard:", ("Transaction dashboard", "Lung Cancer With ML"))
    
    if option == 'Transaction dashboard':
        def get_data_from_csv():
            df = pd.read_csv("transaction_clean.csv", nrows=10000)
            return df

        df = get_data_from_csv()

        # Create a dropdown filter for TransactionDay
        days = df["TransactionDay"].unique()
        selected_day = st.selectbox("Select Transaction Day", ["All Days"] + list(days))

        # Filter the dataframe based on the selected day or show all days
        if selected_day == "All Days":
            filtered_df = df
        else:
            filtered_df = df[df["TransactionDay"] == selected_day]

        # Display the top 5 Transaction Hours based on TransactionHour
        top_hours = filtered_df["TransactionTime"].value_counts().head(10)
        st.write("Top 10 Transaction Time:")

        # Display the top hours in a table with customized column names and remove the index
        top_hours_df = pd.DataFrame({"Transaction Time": top_hours.index, "Total of Transaction": top_hours.values})
        st.table(top_hours_df.rename(columns={"Transaction Time": "Transaction Time", "Total of Transaction": "Total Transaction"}))


        # Create a bar chart for the count of transactions per country
        country_count = filtered_df["Country"].value_counts()

        # Create a bar chart for the count of transactions per day
        day_count = filtered_df["TransactionDay"].value_counts()

        # Calculate and display the most transaction hour  
        most_transaction_hour = filtered_df["TransactionHours"].value_counts()

        # Display the "Country" bar chart in the first column
        col1, col2= st.columns(2)
        with col1:
            st.bar_chart(country_count)
            st.write("Transaction Count by Country")
            # Add a separator between contents of col1 and col2

        # Display the "TransactionDay" bar chart in the second column (col2)
        with col2:
            st.bar_chart(day_count)
            st.write("Transaction Count by Day")

    elif option == 'Lung Cancer With ML':
        def get_data_from_csv():
            df = pd.read_csv("survey_lung_cancer.csv", delimiter=",", nrows=10000)
            df.drop_duplicates(inplace=True)
            df['GENDER'] = df['GENDER'].replace(['M', 'F'], [0, 1])
            df['LUNG_CANCER'] = df['LUNG_CANCER'].replace(['YES', 'NO'], [1, 0])
            
            return df

        df = get_data_from_csv()

        st.write("Displaying DataFrame (structured view):")
        st.dataframe(df)
        st.write("---")
        st.write("Lung Cancer Description")
        st.dataframe(df.describe())

        st.write("---")
        st.write("Lung Cancer Data Visualization")
        num_list=['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
       'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
       'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
       'SWALLOWING DIFFICULTY', 'CHEST PAIN']

        fig, axes = plt.subplots(6, 3, figsize=(15, 20))

        for i, ax in enumerate(axes.flatten()):
            if i < len(num_list):
                sns.histplot(data=df, x=num_list[i], hue='LUNG_CANCER', kde=True, ax=ax)
                ax.set_title(num_list[i])
            else:
                ax.axis('off')  # Turn off extra subplots if there are not enough features

        plt.tight_layout()

        hist_fig = plt.gcf()
        st.pyplot(hist_fig)

# Heatmap
        df = get_data_from_csv()

 
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write("---")
        st.write("Lung Cancer Heatmap")
        plt.figure(figsize=(15, 15))
        sns.heatmap(df.corr(), annot=True, cbar=True, cmap='Blues', fmt='.1f')
        heatmap_fig = plt.gcf()
        st.pyplot(heatmap_fig)

        #SVM
        # Split data into features and target
        st.write("---")
        st.write("Data Modelling")

               # Split data into features and target
        X = df.drop(columns=['LUNG_CANCER'])
        y = df['LUNG_CANCER']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Models
        models = [
            ('SVM', svm.SVC(kernel='linear')),
            ('Random Forest', RandomForestClassifier(n_estimators=100)),
            ('Decision Tree', DecisionTreeClassifier())
        ]

        # Evaluate models and display results
        for i, (name, model) in enumerate(models):
            st.write(f"--- {name} ---")
            st.write(f"{name} Model Evaluation:")
            model.fit(X_train, y_train)
            train_score = model.score(X_train, y_train)
            test_pred = model.predict(X_test)
            test_acc = accuracy_score(y_test, test_pred)
            st.write(f"Training Accuracy: {train_score:.2f}")
            st.write(f"Test Accuracy: {test_acc:.2f}")
            st.write("Classification Report:")
            if name == 'Support Vector Machine':
                report = classification_report(y_test, test_pred, output_dict=True)
                report_df = pd.DataFrame(report).transpose()
                st.dataframe(report_df)
            else:
                report_df = classification_report(y_test, test_pred, output_dict=True)
                st.dataframe(pd.DataFrame(report_df).transpose())


# Add a footer with improved styling
st.markdown(
    """
    <style>
    footer {
        text-align: center;
        margin-top: 2rem;
        font-size: 12px;
        color: #888;
    }
    </style>
    """
    , unsafe_allow_html=True
)
st.markdown("ariansp08@gmail.com")