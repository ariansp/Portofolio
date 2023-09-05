import base64
import config
import streamlit as st
import pandas as pd
import googleapiclient.discovery
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
css_file = "main.css"
resume_file = "CV.pdf"
profile_pic = "profile-pic1.png"

# Set the title and a brief description
st.title("Portfolio")
st.write("Arian Syah Putra | Data Analyst | Data Engineer.")

# Add a sidebar with options
st.sidebar.title("Section")
selected_page = st.sidebar.radio("Menu", ["About Me", "Youtube Scrap"])

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
        "Instagram": "https://instagram.com/arian.tsah",
        "LinkedIn": "https://linkedin.com/Ariansyahputra",
        "GitHub": "https://github.com/ariansp",
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
    - ✔️ B.CompSc. Computer Science, North Sumatera University, Indonesia (Cumlaude, 3.73/4.00)
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
    - ✔️ Data Analytics Certification, Certiport 
    - ✔️ Database Certification, Certiport  
    - ✔️ Microsoft Excel 2019 Expert, Microsoft 
    - ✔️ Microsoft Excel 2019 Associate, Microsoft 
    """
    )
    st.write("---")

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python, SQL, Java, C/C++, Pascal
    - 📊 Data Visulization: PowerBi, MS Excel, Spreadsheet
    - 🗄️ Databases: PostgreSQl, MySQL
    """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Data Engineer Freelance | Windata**")
    st.write("07/2023 - Present")
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

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst Freelance | Windata**")
    st.write("01/2018 - 02/2022")
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
    video_link_id = st.text_input("Enter YouTube Video Link ID (e.g., Xk2Y5EsU1Ic):")

    if video_link_id:
        # Function to extract video ID from the link ID
        def extract_video_id(video_link_id):
            # Extract the video ID from the link ID
            video_id = video_link_id.split("v=")[-1]
            return video_id

        # Extract the video ID from the provided link ID
        video_id = extract_video_id(video_link_id)

        # Second video_comments function
        def video_comments_max(video_id, max_comments=100):
            replies = []
            api_service_name = "youtube"
            api_version = "v3"
            DEVELOPER_KEY = config.api_key  # Replace with your own YouTube API key

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
