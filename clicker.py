from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError, WindowNotFoundError

# Path to the executable of your desktop application
app_path = r"C:\Users\Misha and Meera\AppData\Local\thinkorswim\thinkorswim.exe"

try:
    # Launch the application
    app = Application(backend="uia").start(app_path)

    # Wait for the main window of the application to load
    main_window = app.window(title_re=".*Your Application Title.*")
    main_window.wait("ready", timeout=10)

    print("Application launched successfully.")

    try:
        # Check for a pop-up window
        popup = app.window(title_re=".*Pop-up Title.*")  # Adjust title as per the actual pop-up
        popup.wait("ready", timeout=5)
        print("Pop-up detected.")

        try:
            # Look for a button labeled "Buy" within the pop-up
            buy_button = popup.child_window(title="Buy", control_type="Button")
            buy_button.click()
            print("'Buy' button clicked successfully.")

        except ElementNotFoundError:
            print("'Buy' button not found in the pop-up.")

    except WindowNotFoundError:
        print("No pop-up detected.")

except Exception as e:
    print(f"An error occurred: {e}")