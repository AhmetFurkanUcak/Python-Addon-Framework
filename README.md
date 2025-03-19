## **Python-Addon-Framework** 🚀  
A lightweight and flexible addon management framework for Python. Easily load, list, and run addons dynamically without modifying the core application.  

### **🔹 Features**  
✔️ Dynamically loads addons from the `addons/` directory  
✔️ Lists available addons with their `name` attribute  
✔️ Allows running a single addon or all at once  
✔️ Simple and easy-to-use CLI interface  

### **🔹 How It Works**  
1. Place your addon `.py` files inside the `addons/` folder.  
2. Each addon should have:  
   ```python
   name = "My Addon"

   def run():
       print(f"{name} is running!")
   ```  
3. Run `main.py` and select an addon from the menu.  

### **🔹 Installation & Usage**  
```bash
git clone https://github.com/AhmetFurkanUcak/Python-Addon-Framework.git
cd Python-Addon-Framework
python main.py
```

### **🔹 License**  
MIT License  

---
