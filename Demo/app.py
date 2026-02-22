from flask import Flask, render_template, abort

app = Flask(__name__)

# Data Materi Lengkap Berdasarkan Kurikulum Advanced
curriculum_data = {
    "01": {
        "title": "Module 1: GUI Architecture",
        "topic": "Layout & Widgets",
        "status": "Introduction",
        "description": "Mastering the transition from procedural scripts to event-driven visual applications.",
        "content": "In this module, students learn to build visual interfaces. Unlike basic scripts, a GUI runs in a 'Main Loop' and waits for user interaction. We focus on Geometric Managers (pack and grid) to create responsive layouts that adapt to window sizes.",
        "objectives": ["Understand the Main Loop", "Master pack() and grid()", "Visual UX with Hex styling"],
        "real_world": "Used in desktop apps like Spotify or VS Code to ensure buttons stay organized when you resize the window.",
        "code": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title('Modern App')\n\n# Styled label with Hex code\nlabel = tk.Label(root, text='Hello World', fg='#3498db', font=('Arial', 14))\nlabel.pack(pady=20)\n\nroot.mainloop()",
        "quiz": {"q": "Which manager is better for precise, table-like alignment?", "a": "grid()", "b": "pack()", "correct": "a"},
        "exercise": "CHALLENGE: Create a login form with Username & Password fields using the .grid() manager."
    },
    "02": {
        "title": "Module 2: OOP for Apps",
        "topic": "Classes & State",
        "status": "Advanced Structure",
        "description": "Implementing Classes as application blueprints for clean and maintainable code.",
        "content": "Advanced projects require structure. We teach students to use Classes to encapsulate UI components, using __init__ for setup and 'self' for internal data communication between different methods.",
        "objectives": ["App blueprints with Classes", "State initialization", "Using 'self' for communication"],
        "real_world": "Professional developers use OOP so that multiple people can work on the same app without overlapping code logic.",
        "code": "class MyApp:\n    def __init__(self, root):\n        self.root = root\n        self.label = tk.Label(self.root, text='OOP Structure')\n        self.label.pack()\n\nroot = tk.Tk()\napp = MyApp(root)\nroot.mainloop()",
        "quiz": {"q": "What is the primary purpose of 'self' in a GUI Class?", "a": "To access class variables", "b": "To exit the program", "correct": "a"},
        "exercise": "CHALLENGE: Convert your login form from Module 1 into a Class-based structure."
    },
    "03": {
        "title": "Module 3: Defensive Coding",
        "topic": "Error Handling",
        "status": "Security",
        "description": "Implementing security layers to prevent application crashes and invalid inputs.",
        "content": "A robust app should never crash! We teach students to use try-except blocks to catch potential errors and use Messagebox alerts to guide the user when something goes wrong.",
        "objectives": ["Try-except implementation", "Input validation", "Messagebox alerts"],
        "real_world": "Prevents the app from closing suddenly when a user accidentally types a letter into a price field.",
        "code": "from tkinter import messagebox\n\ntry:\n    price = float(entry_price.get())\nexcept ValueError:\n    messagebox.showerror('Error', 'Please enter a valid number!')",
        "quiz": {"q": "Which Python block is used to catch an error?", "a": "try", "b": "except", "correct": "b"},
        "exercise": "CHALLENGE: Add a validation that shows an error if the user input is a negative number."
    },
    "04": {
        "title": "Module 4: Dynamic Data Control",
        "topic": "History & Logic",
        "status": "Data Lifecycle",
        "description": "Managing session-based history logs and handling live application lifecycles.",
        "content": "Learn to manage data flow in real-time. We use Listbox widgets to store calculation history and implement confirmation flows before the user deletes important data.",
        "objectives": ["Listbox management", "Dynamic UI updates", "AskYesNo confirmation"],
        "real_world": "Essential for apps like Calculators or To-Do lists where users need to track their previous activities.",
        "code": "# Adding to history listbox\nself.history.insert(0, f'Result: {final}')\n\n# Confirmation dialog\nif messagebox.askyesno('Reset', 'Clear all history?'):\n    self.history.delete(0, 'end')",
        "quiz": {"q": "Which widget is best for displaying a list of history logs?", "a": "Entry", "b": "Listbox", "correct": "b"},
        "exercise": "CHALLENGE: Create a 'Delete' button that only removes the item currently selected by the user."
    }
}

@app.route('/')
def home():
    return render_template('index.html', curriculum=curriculum_data)

@app.route('/module/<id>')
def module_detail(id):
    module = curriculum_data.get(id)
    if module:
        return render_template('detail.html', module=module)
    abort(404)

# Route tambahan untuk halaman filosofi/resource agar tombol tidak mati
@app.route('/resource')
def resource():
    return render_template('resource.html')

if __name__ == '__main__':
    # host='0.0.0.0' memungkinkan akses dari HP lewat IP Address laptop
    app.run(host='0.0.0.0', port=5000, debug=True)