 📸 Photo Renamer  

A simple Python automation script that batch renames photos in a folder.  
It sorts images by their creation date (or last modified time) and renames them with a prefix, today’s date, and a sequence number.  

---

 ✨ Features  
- Renames `.jpg`, `.jpeg`, `.png` files.  
- Sorts photos in chronological order before renaming.  
- Adds a prefix, today’s date, and sequential numbering.  
- Works on Windows, macOS, and Linux.  

---

 🛠️ Example  
Before: 
```
IMG_003.jpg
IMG_120.jpg
IMG_050.jpg
```

After running script (prefix = "vacay"):  
```
vacay_20250908_1.jpg
vacay_20250908_2.jpg
vacay_20250908_3.jpg
```

---

 🚀 Usage  

1. Clone or download this repo.  
2. Place your images inside a folder (e.g., `Pictures/Test`).  
3. Run the script:  

```bash
python photo_renamer.py
```

4. Example with custom prefix:  
```python
rename_photos("C:/Users/YourName/Pictures/Test", prefix="birthday")
```

---

 📦 Requirements  
- Python 3.x  
- Standard libraries: `os`, `datetime` (no extra installs needed).  

---

 📂 Project Structure  
```
photo-renamer/
│── photo_renamer.py     # main script
│── README.md            # project description
│── samples/             # (optional) before/after screenshots
```

---

 ✅ Future Improvements  
- Rename based on EXIF metadata (actual photo taken date).  
- Add GUI version with Tkinter.  
- Add drag-and-drop support.  

---

 👤 Author  
- Angela Fredy  
- 📧 angelafredy9a3@gmail.com  
- 🌐 [GitHub Profile](https://github.com/AngF07)  
