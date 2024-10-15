from pytz import timezone
from tkinter import Tk, Frame, Label, LabelFrame, Canvas
from tkinter import RIDGE
from tkcalendar import Calendar
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from PIL import Image, ImageTk


class AgeFinder:
    def __init__(self, root):
        self.root = root
        self._birth_info = ""
        self._current_info = ""

        # UI-related attributes
        self.birth_calendar = None
        self.birth_date_labels = {}
        self.current_date_labels = {}
        self.age_labels = {}
        self.time_label = None

        self.initialize_ui()

    def initialize_ui(self):
        """Initialize the user interface."""
        self.root.geometry("800x500+200+50")
        self.root.title("Age Finder | Developed by Prathmesh")
        self.root.resizable(False, False)

        # Create frames with rounded corners
        cal_frame = self.create_rounded_frame(self.root, 0, 0, 0.625, 1)
        date_frame = self.create_rounded_frame(self.root, 5 / 8, 0, 0.375, 0.5)
        age_frame = self.create_rounded_frame(self.root, 5 / 8, 0.5, 0.375, 1 / 3)
        time_frame = self.create_rounded_frame(self.root, 5 / 8, 5 / 6, 0.375, 1 / 6)

        # Calendar for birth date selection
        self.birth_calendar = Calendar(
            cal_frame,
            selectmode="day",
            year=2000,
            month=1,
            day=1,
            date_pattern="ddmmyyyy",
        )
        self.birth_calendar.bind(
            "<<CalendarSelected>>", lambda event: self.update_labels()
        )
        self.birth_calendar.place(x=0, y=0, relwidth=1, relheight=1)

        # Setup labels and time
        self.setup_labels(date_frame, age_frame)
        self.setup_time_label(time_frame)

        # Initial updates for labels and clock
        self.update_labels()
        self.update_clock()

    def create_rounded_frame(self, parent, relx, rely, relwidth, relheight, radius=20):
        """Create a frame with rounded corners."""
        frame = Frame(parent, bg="white")
        canvas = Canvas(frame, bg="lightgray", highlightthickness=0)
        rounded_rect = self.create_rounded_rectangle(0, 0, 1, 1, radius)
        canvas.create_polygon(
            rounded_rect, fill="lightgray", outline="lightgray", smooth=True
        )
        canvas.pack(fill="both", expand=True)
        frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame

    def create_rounded_rectangle(self, x1, y1, x2, y2, r):
        """Calculate the coordinates for a rounded rectangle."""
        return [
            (x1 + r, y1),  # Top right
            (x2 - r, y1),  # Top left
            (x2, y1 + r),  # Right
            (x2, y2 - r),  # Bottom right
            (x2 - r, y2),  # Bottom
            (x1 + r, y2),  # Left
            (x1, y2 - r),  # Bottom left
            (x1, y1 + r),  # Top left
        ]

    def setup_labels(self, date_frame, age_frame):
        """Set up labels for displaying birth date, current date, and calculated age."""
        for count, label in enumerate(["Birth Date", "Current Date"]):
            self.create_label(date_frame, label, 0, count / 2, 1, 1 / 6)

        # Birth and current date label frames
        self.birth_date_labels = self.create_date_labels(date_frame, 1 / 6, "Birth")
        self.current_date_labels = self.create_date_labels(date_frame, 2 / 3, "Current")

        # Age label frames
        self.age_labels = self.create_age_labels(age_frame)

    def create_date_labels(self, parent, rel_y, label_prefix):
        """Create label frames for displaying day, month, and year."""
        labels = {}
        for i, label in enumerate(["Date", "Month", "Year"]):
            labels[label.lower()] = self.create_label_frame(
                parent, relx=i / 3, rely=rel_y, relwidth=1 / 3, relheight=1 / 3
            )
        return labels

    def create_age_labels(self, parent):
        """Create label frames for displaying age in days, months, and years."""
        labels = {}
        for i, label in enumerate(["Day(s)", "Month(s)", "Year(s)"]):
            text_frame = self.create_label_frame(
                parent, relx=i / 3, rely=0, relwidth=1 / 3, relheight=1 / 2
            )
            value_frame = self.create_label_frame(
                parent, relx=i / 3, rely=1 / 2, relwidth=1 / 3, relheight=1 / 2
            )

            Label(text_frame, text=label, font=("times new roman", 18, "bold")).place(
                x=0, y=0, relwidth=1, relheight=1
            )
            labels[label.lower()] = value_frame
        return labels

    def create_label(self, parent, text, relx, rely, relwidth, relheight):
        """Helper to create a text label."""
        label_frame = LabelFrame(parent, bd=2, relief=RIDGE, bg="white")
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        label = Label(label_frame, text=text, font=("times new roman", 20, "bold"))
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_label_frame(self, parent, relx, rely, relwidth, relheight):
        """Create a label frame."""
        label_frame = LabelFrame(parent, bd=2, relief=RIDGE, bg="white")
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return label_frame

    def setup_time_label(self, time_frame):
        """Set up the time label in the UI."""
        self.time_label = Label(time_frame, font=("times new roman", 36, "bold"))
        self.time_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_labels(self):
        """Update the birth date, current date, and age labels."""
        self._get_dates()
        birth_date, current_date, age = self._process_dates()

        self.display_label_data(self.birth_date_labels, birth_date)
        self.display_label_data(self.current_date_labels, current_date)
        self.display_label_data(self.age_labels, age)

    def display_label_data(self, labels_dict, data_tuple):
        """Helper to display data in respective label frames."""
        for key, value in zip(labels_dict.keys(), data_tuple):
            Label(
                labels_dict[key], text=value, font=("times new roman", 30, "bold")
            ).place(x=0, y=0, relwidth=1, relheight=1)

    def _get_dates(self):
        """Retrieve the birth date from the calendar and the current date."""
        self._birth_info = self.birth_calendar.get_date()
        self._current_info = dt.now().strftime("%d%m%Y")

    def _process_dates(self):
        """Process birth and current dates to calculate age."""
        # Parse birth and current dates directly into date objects
        birth_date = dt.strptime(self._birth_info, "%d%m%Y").date()
        current_date = dt.strptime(self._current_info, "%d%m%Y").date()

        # Check if the birth date is in the future
        if current_date < birth_date:
            return (
                (birth_date.day, birth_date.month, birth_date.year),
                (current_date.day, current_date.month, current_date.year),
                ("N/A", "N/A", "N/A"),
            )

        # Calculate age using relativedelta
        age = relativedelta(current_date, birth_date)

        return (
            (birth_date.day, birth_date.month, birth_date.year),
            (current_date.day, current_date.month, current_date.year),
            (age.days, age.months, age.years),
        )

    def update_clock(self):
        """Update the clock with the current time."""
        time_now = dt.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
        self.time_label.config(text=time_now)
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = Tk()
    app = AgeFinder(root)
    root.mainloop()
