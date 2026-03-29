import time

class Microwave:
    def __init__(self):
        # State variables
        self.is_running = False
        self.time_remaining = 0  # in seconds
        self.power_level = 10    # Default 1-10
        self.turntable_on = True
        self.surface_light = False
        self.vent_on = False
        self.display = "12:00"   # Default clock display
        self.input_buffer = ""   # Stores numbers pressed before 'Start'

    def press_number(self, number):
        """Simulates pressing a number on the keypad (0-9)."""
        if not self.is_running:
            # Express Cook Logic: If 1-6 is pressed on an empty buffer, start immediately
            if len(self.input_buffer) == 0 and 1 <= number <= 6:
                print(f"--- Express Cook: {number} minute(s) ---")
                self.time_remaining = number * 60
                self.start_microwave()
            else:
                self.input_buffer += str(number)
                self.display = self.input_buffer
                print(f"Display: {self.display}")

    def press_add_30_sec(self):
        """Adds 30 seconds to the timer. Starts if not already running."""
        self.time_remaining += 30
        print("--- Added 30 Seconds ---")
        if not self.is_running:
            self.start_microwave()

    def press_start_pause(self):
        if self.is_running:
            self.is_running = False
            print("--- Microwave Paused ---")
        elif self.input_buffer or self.time_remaining > 0:
            if self.input_buffer:
                # Convert buffer (e.g., "130") to seconds (1 min 30 sec)
                # Simple logic: last two digits are seconds, others are minutes
                seconds = int(self.input_buffer[-2:] if len(self.input_buffer) >= 2 else self.input_buffer)
                minutes = int(self.input_buffer[:-2] if len(self.input_buffer) > 2 else 0)
                self.time_remaining = (minutes * 60) + seconds
                self.input_buffer = ""
            self.start_microwave()

    def start_microwave(self):
        if self.time_remaining > 0:
            self.is_running = True
            print(f"--- Microwave Started: {self.format_time(self.time_remaining)} ---")

    def press_cancel_off(self):
        if self.is_running:
            self.is_running = False
            print("--- Stopped ---")
        else:
            self.time_remaining = 0
            self.input_buffer = ""
            self.display = "12:00"
            print("--- Cleared ---")

    def toggle_vent(self):
        self.vent_on = not self.vent_on
        status = "ON" if self.vent_on else "OFF"
        print(f"Vent: {status}")

    def toggle_surface_light(self):
        self.surface_light = not self.surface_light
        status = "ON" if self.surface_light else "OFF"
        print(f"Surface Light: {status}")

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def tick(self):
        """Simulates the passage of 1 second of time."""
        if self.is_running and self.time_remaining > 0:
            self.time_remaining -= 1
            print(f"Cooking... {self.format_time(self.time_remaining)}")
            if self.time_remaining == 0:
                self.is_running = False
                print("BEEP BEEP BEEP! Cooking Complete.")

# --- Example Usage ---
my_microwave = Microwave()

# 1. Test Express Cook (Pressing '2' for 2 minutes)
my_microwave.press_number(2)

# 2. Add 30 seconds while running
my_microwave.press_add_30_sec()

# 3. Simulate 3 seconds of cooking
for _ in range(3):
    my_microwave.tick()

# 4. Turn on the light and vent
my_microwave.toggle_surface_light()
my_microwave.toggle_vent()

# 5. Stop and clear
my_microwave.press_cancel_off()