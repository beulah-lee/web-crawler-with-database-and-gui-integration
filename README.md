# Multi-Threaded Web Crawler with Database and GUI Integration  

This project is a multi-threaded web crawler developed using C++, Python, and MySQL. It efficiently fetches and processes URLs concurrently, extracts and displays text content from web pages, and stores URLs in a MySQL database. A user-friendly GUI built with Tkinter allows users to interact with the application, input URLs, specify filtering keywords, view stored data, and manage the database.


## **Features**  

- **High-Performance Multi-Threading:** Efficiently fetches and processes multiple URLs simultaneously to maximize performance.
- **HTML Parsing and Extraction**: Leveraged BeautifulSoup to extract and display text content from web pages.
- **Database Integration**: Utilized MySQL for organized and scalable data storage, including URL management and content retrieval.
- **URL Indexing and Normalization**: nsured all input URLs are correctly formatted by automatically adding the URL prefix `https://` if it is missing. Also, the URL indices were updated when the table was modified.
- **Content Filtering:** Filtered URLs based on keywords in their web content using regex.  
- **GUI for User Interaction:** Designed to allow users to:
  - Add and delete URLs in the database.
  - Specify filtering keywords to refine web content crawling.
  - View and analyze text content for each URLs. 
  - Display and manage stored URL data in a table.

## **Tools and Technologies**  

- **C++:** For URL management, multi-threading, and content filtering.  
- **Python:** For database management and GUI development.  
- **MySQL:** For reliable and scalable data storage.  
- **BeautifulSoup:** For parsing HTML and extracting text content.
- **Tkinter:** For building the GUI interface.  
- **CMake:** Build tool for managing C++ components.

## Functionality Showcase
### Program Launch and GUI
The GUI provides an interface for interacting with the web crawler application 

Note: The `google.com` and `youtube.com` entries displayed in the table were added to the database in a previous session.

![image](https://github.com/user-attachments/assets/9467b6e9-d6a8-4868-b2c9-f8fd26b3eee3)

### Adding a URL
When a URL is entered, a pop up displays a success message. After pressing "OK", the URL is added to the database table.

![image](https://github.com/user-attachments/assets/ea47c5e8-815d-4355-8b4c-360b6f45017b)
![image](https://github.com/user-attachments/assets/76c8ca1e-e847-4637-8824-9dc5b10495f3)
### Keyword Search with Loading Indicator
While searching for keywords in the web page content, a loading indicator is shown to inform the user of the ongoing search.

![image](https://github.com/user-attachments/assets/911ab31a-26a0-44fa-aa63-214f2297ea1f)
### Keyword Search Results: Success
If matching content is found, the results are displayed, allowing the user to view the relevant text.

![image](https://github.com/user-attachments/assets/e015525e-7264-452d-93d0-cef1fce90a76)
### View Full Content
Users can view the full text content extracted from web pages, as shown here for Google.com and YouTube.

![image](https://github.com/user-attachments/assets/18a7b254-7d61-4547-ac52-05e0a7bc55f0)
### Keyword Search Results: No Match Found
If no match is found for the entered keyword, a pop up informs the user that no matches were found.

![image](https://github.com/user-attachments/assets/850b6343-262b-41a5-9e7f-2f504b21a615)
### Removing a URL
When a URL is selected for deleation, a pop up displays a success message. After pressing "OK", the URL is deleted from the table, and the indices of remaining URLs are updated in the database accordingly

![image](https://github.com/user-attachments/assets/236082bc-f982-4e8c-b27f-f49278130b6f)
![image](https://github.com/user-attachments/assets/45fc982d-7915-4386-bc71-9dc7bf630b20)
