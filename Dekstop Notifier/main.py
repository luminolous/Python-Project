from plyer import notification
import os

notification.notify(
    title = "It worked!",
    message = 'Awesome!',
    app_icon = os.path.join(os.getcwd(), "nama_file"),
    timeout = 1
)
