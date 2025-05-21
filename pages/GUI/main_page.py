import streamlit as st, time, os
    
class main_page_GUI:
    def __init__(self):
        email_address = "morten.viersi@gmail.com"
        email_subject_Help = "Get help with the application"
        email_body_Help = "Hi Morten, \n\n I need help with using the Application. I need help with the following: .........."
        email_subject_BUG = "Report a Bug"
        email_body_BUG = "Hi Morten, \n\n I'm sending you an email experiencing a bug while using the SMIPPS Application. I experienced the bug after performing the following steps .........."
        email_link_Help = f"mailto:{email_address}?subject={email_subject_Help}&body={email_body_Help}"
        email_link_BUG = f"mailto:{email_address}?subject={email_subject_BUG}&body={email_body_BUG}"

        st.set_page_config(
            page_title="Pareto",
            layout="wide",
            page_icon=":billed_cap:",
            menu_items={'Get Help': email_link_Help,
            'Report a bug': email_link_BUG,
            'About': "# Project by Morten Vier Simensen"
        }
            )
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(34, 44, 92)!important;
            color: white !important;
        }
        </style>""", unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        def write_timestamp_to_file(timestamp):
            data_dir = "Data"
            try:
                with open(os.path.join(data_dir, "timestamp.txt"), "w") as file:
                    file.write(str(timestamp))
            except:
                pass
        def read_timestamp_from_file():
            data_dir = "Data"
            timestamp_file = os.path.join(data_dir, "timestamp.txt")
            if os.path.exists(timestamp_file):
                with open(timestamp_file, "r") as file:
                    timestamp = file.read()
                    return timestamp
            else:
                return "NA"

        with col5:
            load = st.button('Load New Data from Sodir',  'sodir')
        if load:
            from Data.getData import deleteAndLoadNewDataFromNPD
            if deleteAndLoadNewDataFromNPD() == True:
                timestamp = time.ctime()
                alert00 = st.warning('Data downloaded from Sodir ' + timestamp)
                time.sleep(5)
                alert00.empty()
                write_timestamp_to_file(timestamp)

        #with col4:
            #try:
                #stamp = read_timestamp_from_file()
                #mym = "Data last downloaded:" + str(stamp)
                #st.write(mym)
            #except:
             #   pass
        
        st.title('Sodir Data')
        st.write(" ")
        st.write(" ")
        col1, col2 = st.columns(2)
        with col1:
            my_path = os.path.join('Data', 'Storage', 'frontpage.png')
            st.image(my_path)
        with col2:
            on_information = st.toggle("Show me more information on how to use the application", value=False, label_visibility="visible")
            if on_information:
                st.write(
                            """The application is connected to Sodir (https://www.sodir.no/). Data can automatically be pulled from Sodirs open data sources,
                        before being used in the application. The data includes field, well and production data. The data is stored
                        in the application. The button in the top right corner <Load New Data from Sodir> deletes the stored data, and fetches the latest data
                        at Sodir. Sodir data are updated every night. During this time, Sodir's services and portals are unavailable, and the user will not be able
                        collect new data.""")
                
            st.write('Created for Olav Haugerud')
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("BY USING THIS WEB SITE YOU UNDERSTAND AND AGREE THAT YOUR USE OF THIS WEB SITE AND ANY SERVICES OR CONTENT PROVIDED IS MADE AVAILABLE AND PROVIDED TO YOU AT YOUR OWN RISK. IT IS PROVIDED TO YOU AS IS AND SMIPPS EXPRESSLY DISCLAIM ALL WARRANTIES OF ANY KIND.")















