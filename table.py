import tkinter as tk
from tkinter import ttk
import random

class TimetableGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timetable Generator")
        # Define variables for user input
        self.num_days = tk.IntVar(value=5)
        self.num_timeslots = tk.IntVar(value=6)
        self.num_subjects = tk.IntVar(value=7)
        self.num_classes = tk.IntVar(value=3)
        self.population_size = tk.IntVar(value=100)
        self.num_generations = tk.IntVar(value=50)
        # Lists to store user-defined subjects and timeslots
        self.subject_entries = []
        self.timeslot_entries = []
        # Create labels and entry fields for user input
        self.create_input_fields()
        # Button to generate timetable
        ttk.Button(self, text="Generate Timetable", command=self.generate_timetable).grid(row=7, columnspan=2)
        # Text area to display generated timetable
        self.timetable_text = tk.Text(self, height=20, width=50)
        self.timetable_text.grid(row=8, columnspan=2)

    def create_input_fields(self):
        ttk.Label(self, text="Number of days in a week:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.num_days).grid(row=0, column=1)
        ttk.Label(self, text="Number of timeslots per day:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.num_timeslots).grid(row=1, column=1)
        ttk.Label(self, text="Number of subjects:").grid(row=2, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.num_subjects).grid(row=2, column=1)
        ttk.Label(self, text="Number of classes:").grid(row=3, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.num_classes).grid(row=3, column=1)
        ttk.Label(self, text="Population size for GA:").grid(row=4, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.population_size).grid(row=4, column=1)
        ttk.Label(self, text="Number of generations:").grid(row=5, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.num_generations).grid(row=5, column=1)
        ttk.Label(self, text="Subjects:").grid(row=6, column=0, sticky="w")
        for i in range(self.num_subjects.get()):
            entry = ttk.Entry(self)
            entry.grid(row=6, column=i+1)
            self.subject_entries.append(entry)
        ttk.Label(self, text="Timeslots:").grid(row=7, column=0, sticky="w")
        for i in range(self.num_timeslots.get()):
            entry = ttk.Entry(self)
            entry.grid(row=7, column=i+1)
            self.timeslot_entries.append(entry)

    def generate_timetable(self):
        num_days = self.num_days.get()
        num_timeslots = self.num_timeslots.get()
        num_subjects = self.num_subjects.get()
        num_classes = self.num_classes.get()
        population_size = self.population_size.get()
        num_generations = self.num_generations.get()
        # Get user-defined subjects and timeslots
        subjects = [entry.get() for entry in self.subject_entries]
        timeslots = [entry.get() for entry in self.timeslot_entries]
        # Generate timetable (replace this with your algorithm)
        timetable = self.generate_dummy_timetable(num_days, num_timeslots, subjects, num_classes)
        # Display generated timetable
        self.timetable_text.delete(1.0, tk.END)
        self.timetable_text.insert(tk.END, timetable)

    def generate_dummy_timetable(self, num_days, num_timeslots, subjects, num_classes):
        timetable = ""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        timeslots = [f"{i}:00 - {i+1}:00" for i in range(9, 15)]
        for class_idx in range(num_classes):
            timetable += f"Timetable for Class {class_idx + 1}:\n"
            for day in days:
                timetable += f"{day}\n"
                for timeslot in timeslots:
                    subject = random.choice(subjects)
                    timetable += f"{timeslot}: {subject}\n"
        return timetable

if __name__ == "__main__":
    app = TimetableGenerator()
    app.mainloop()
