import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import re
import requests
from bs4 import BeautifulSoup
import threading

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="mysql",  
    database="web_crawler"
)
cursor = db.cursor()

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text() 
    except requests.RequestException as e:
        return f"Error fetching content from {url}: {e}"

def add_url():
    url = url_entry.get().strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    keywords = keyword_entry.get().split(",")
    if url:
        content = fetch_content(url)
        if any(re.search(rf"\b{kw.strip()}\b", content, re.IGNORECASE) for kw in keywords):
            try:
                cursor.execute("INSERT INTO urls (url) VALUES (%s)", (url,))
                db.commit()
                messagebox.showinfo("Success", "URL added successfully!")
                url_entry.delete(0, tk.END)
                refresh_table()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add URL: {e}")
        else:
            messagebox.showwarning("Content Filter", "URL content does not match any keywords.")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

def delete_url():
    selected_item = tree.selection()
    if selected_item:
        url_id = tree.item(selected_item)["values"][0]
        try:
            cursor.execute("DELETE FROM urls WHERE id = %s", (url_id,))
            db.commit()
            cursor.execute("SET @count = 0")
            cursor.execute("UPDATE urls SET id = @count:= @count + 1")
            cursor.execute("ALTER TABLE urls AUTO_INCREMENT = 1")
            messagebox.showinfo("Success", "URL deleted successfully!")
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete URL: {e}")
    else:
        messagebox.showwarning("Selection Error", "Please select a URL to delete.")

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM urls")
    for record in cursor.fetchall():
        tree.insert("", tk.END, values=record)

def search_urls():
    keywords = keyword_entry.get().split(",")
    cursor.execute("SELECT url FROM urls")
    urls = [row[0] for row in cursor.fetchall()]

    results = []
    def process_url(url):
        content = fetch_content(url)
        if any(re.search(rf"\b{kw.strip()}\b", content, re.IGNORECASE) for kw in keywords):
            results.append(f"Match Found: {url}\nText Content:\n{content[:500]}...\n")
        else:
            results.append(f"No Match: {url}\n")

    def run_search():
        for url in urls:
            process_url(url)
            progress_var.set(progress_var.get() + 1)
            root.update_idletasks()
        loading_screen.destroy()
        messagebox.showinfo("Search Results", "\n".join(results))

    loading_screen = tk.Toplevel(root)
    loading_screen.title("Searching URLs")
    tk.Label(loading_screen, text="Searching URLs, please wait...").pack(pady=10)
    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(loading_screen, maximum=len(urls), variable=progress_var)
    progress_bar.pack(pady=10)
    threading.Thread(target=run_search).start()

def display_full_content(url):
    content = fetch_content(url)
    detailed_view = tk.Toplevel(root)
    detailed_view.title(f"Text Content: {url}")
    text_widget = tk.Text(detailed_view, wrap="word")
    text_widget.insert("1.0", content)
    text_widget.pack(expand=True, fill="both")
    tk.Button(detailed_view, text="Close", command=detailed_view.destroy).pack(pady=5)

def view_selected_url():
    selected_item = tree.selection()
    if selected_item:
        url = tree.item(selected_item)["values"][1]
        display_full_content(url)
    else:
        messagebox.showwarning("Selection Error", "Please select a URL to view.")

# GUI
root = tk.Tk()
root.title("Web Crawler GUI")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter URL:").grid(row=0, column=0, padx=8)
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5)
tk.Button(frame, text="Add URL", command=add_url).grid(row=0, column=2, padx=5)

tk.Label(frame, text="To delete a URL, select a URL from the table.").grid(row=1, column=0, columnspan=3, padx=5)
tk.Button(frame, text="Delete URL", command=delete_url).grid(row=1, column=2, padx=5)

tk.Label(frame, text="Enter Keyword(s):").grid(row=3, column=0, padx=5)
keyword_entry = tk.Entry(frame, width=40)
keyword_entry.grid(row=3, column=1, padx=5)
tk.Button(frame, text="Search", command=search_urls).grid(row=3, column=2, padx=5)

tree = ttk.Treeview(root, columns=("ID", "URL"), show="headings")
tree.heading("ID", text="ID")
tree.heading("URL", text="URL")
tree.pack(pady=10)

tk.Button(root, text="View Full Content", command=view_selected_url).pack(pady=10)

refresh_table()
root.mainloop()