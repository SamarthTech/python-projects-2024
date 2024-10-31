import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from typing import List, Tuple

class FileRenamer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bulk File Renamer")
        self.geometry("800x600")
        
        self.files: List[str] = []
        self.setup_ui()

    def setup_ui(self):
        # Top frame for file/folder selection
        select_frame = ttk.Frame(self, padding="10")
        select_frame.pack(fill=tk.X)

        # File and folder selection buttons
        ttk.Button(select_frame, text="Select Files", command=self.select_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(select_frame, text="Select Folder", command=self.select_folder).pack(side=tk.LEFT, padx=5)

        # File filter frame
        filter_frame = ttk.LabelFrame(select_frame, text="File Filters", padding="5")
        filter_frame.pack(side=tk.LEFT, padx=10)

        # File extension filter
        ttk.Label(filter_frame, text="Extensions (e.g., .jpg,.png):").pack(side=tk.LEFT, padx=5)
        self.extension_var = tk.StringVar()
        ttk.Entry(filter_frame, textvariable=self.extension_var, width=15).pack(side=tk.LEFT, padx=5)

        # Include subfolders checkbox
        self.include_subfolders = tk.BooleanVar(value=False)
        ttk.Checkbutton(filter_frame, text="Include Subfolders", 
                       variable=self.include_subfolders).pack(side=tk.LEFT, padx=5)

        # Clear selection button
        ttk.Button(select_frame, text="Clear Selection", 
                  command=self.clear_selection).pack(side=tk.RIGHT, padx=5)

        # Renaming options frame
        rename_frame = ttk.LabelFrame(self, text="Renaming Options", padding="10")
        rename_frame.pack(fill=tk.X, padx=10, pady=5)

        # Prefix input
        ttk.Label(rename_frame, text="Prefix:").pack(side=tk.LEFT, padx=5)
        self.prefix_var = tk.StringVar()
        ttk.Entry(rename_frame, textvariable=self.prefix_var).pack(side=tk.LEFT, padx=5)

        # Start number input
        ttk.Label(rename_frame, text="Start Number:").pack(side=tk.LEFT, padx=5)
        self.start_num_var = tk.StringVar(value="1")
        ttk.Entry(rename_frame, textvariable=self.start_num_var, width=5).pack(side=tk.LEFT, padx=5)

        # Padding digits input
        ttk.Label(rename_frame, text="Padding Digits:").pack(side=tk.LEFT, padx=5)
        self.padding_var = tk.StringVar(value="2")
        ttk.Entry(rename_frame, textvariable=self.padding_var, width=5).pack(side=tk.LEFT, padx=5)

        # Preview and Apply buttons
        ttk.Button(rename_frame, text="Preview Changes", 
                  command=self.preview_changes).pack(side=tk.LEFT, padx=5)
        ttk.Button(rename_frame, text="Apply Rename", 
                  command=self.apply_rename).pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(self, textvariable=self.status_var).pack(fill=tk.X, padx=10)

        # Create treeview for file list
        self.tree = ttk.Treeview(self, columns=("Original", "New Name"), show="headings")
        self.tree.heading("Original", text="Original Filename")
        self.tree.heading("New Name", text="New Filename")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    def select_files(self):
        """Open file dialog and add selected files to the list"""
        files = filedialog.askopenfilenames(title="Select files to rename")
        self.files = list(files)
        self.update_status()
        self.preview_changes()

    def select_folder(self):
        """Open folder dialog and add all files from the selected folder"""
        folder = filedialog.askdirectory(title="Select folder containing files to rename")
        if not folder:
            return

        self.files = []
        extensions = [ext.strip().lower() for ext in self.extension_var.get().split(',') if ext.strip()]

        for root, dirs, files in os.walk(folder):
            if not self.include_subfolders.get() and root != folder:
                continue

            for file in files:
                if not extensions or any(file.lower().endswith(ext) for ext in extensions):
                    self.files.append(os.path.join(root, file))

        self.update_status()
        self.preview_changes()

    def clear_selection(self):
        """Clear the current file selection"""
        self.files = []
        self.tree.delete(*self.tree.get_children())
        self.update_status()

    def update_status(self):
        """Update the status label with current file count"""
        self.status_var.set(f"Selected {len(self.files)} files")

    def generate_new_name(self, index: int, original_filename: str) -> Tuple[str, str]:
        """Generate new filename based on current settings"""
        try:
            prefix = self.prefix_var.get()
            start_num = int(self.start_num_var.get())
            padding = int(self.padding_var.get())
            
            file_extension = os.path.splitext(original_filename)[1]
            new_number = str(start_num + index).zfill(padding)
            new_name = f"{prefix}{new_number}{file_extension}"
            
            return original_filename, new_name
        except ValueError:
            return original_filename, "Invalid settings"

    def preview_changes(self):
        """Update the treeview with preview of changes"""
        self.tree.delete(*self.tree.get_children())
        
        for i, filepath in enumerate(self.files):
            original = os.path.basename(filepath)
            original, new_name = self.generate_new_name(i, original)
            self.tree.insert("", tk.END, values=(original, new_name))

    def apply_rename(self):
        """Apply the renaming to all files"""
        if not self.files:
            messagebox.showwarning("No Files", "Please select files to rename first.")
            return

        try:
            renamed_count = 0
            for i, filepath in enumerate(self.files):
                directory = os.path.dirname(filepath)
                original = os.path.basename(filepath)
                _, new_name = self.generate_new_name(i, original)
                
                new_filepath = os.path.join(directory, new_name)
                
                if os.path.exists(new_filepath) and new_filepath != filepath:
                    if not messagebox.askyesno("File Exists", 
                                             f"File {new_name} already exists. Skip this file?"):
                        continue
                
                os.rename(filepath, new_filepath)
                renamed_count += 1
            
            messagebox.showinfo("Success", f"Successfully renamed {renamed_count} files!")
            self.preview_changes()
            self.update_status()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = FileRenamer()
    app.mainloop()
