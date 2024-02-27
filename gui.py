import socket
import tkinter as tk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import threading

# Declare global variables
entry_ip = None
entry_start_port = None
entry_end_port = None
result_text = None

def scanHost():
    global entry_ip, entry_start_port  # Add these lines to declare the global variables
    root = tkinter.Tk()  # Example, make sure to create your Tkinter window properly
    
    ip = entry_ip.get()
    startPort = int(entry_start_port.get())
    endPort = int(entry_end_port.get())
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"Scanning host {ip} from port {startPort} to {endPort}...\n")
    open_ports = []
    threads = []
    for port in range(startPort, endPort + 1):
        t = threading.Thread(target=scanPort, args=(ip, port, open_ports))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    if open_ports:
        result_text.insert(tk.END, f"Open ports: {', '.join(map(str, open_ports))}\n")
    else:
        result_text.insert(tk.END, "No open ports found.\n")

def scanPort(ip, port, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
            tcp.settimeout(0.1)  # Set timeout to 0.1 seconds
            if not tcp.connect_ex((ip, port)):
                open_ports.append(port)
    except Exception:
        pass

def onScanHost():
    try:
        # Create a new thread for port scanning
        threading.Thread(target=scanHost, daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid port numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    global entry_ip, entry_start_port, entry_end_port, result_text
    
    root = tk.Tk()
    root.title("TCP Port Scanner")

    # Styling
    root.geometry('800x400')

    # Load the background image
    background_image = Image.open(r"C:\Users\ghimi\Downloads\123.jpg")  # Replace with your image file
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a Canvas to put the background image
    canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # Title label
    label_title = tk.Label(canvas, text="Port Scanner", font=("Helvetica", 20, "bold"), bg='black', fg='#4CAF50')
    label_title.place(relx=0.5, rely=0.1, anchor="center")

    label_ip = tk.Label(canvas, text="IP Address:", bg='pink', fg='black',font=("Helvetica", 10, "bold"))
    label_ip.place(relx=0.3, rely=0.25, anchor="e")

    entry_ip = tk.Entry(canvas, width=20)
    entry_ip.place(relx=0.4, rely=0.25, anchor="w")

    label_start_port = tk.Label(canvas, text="Start Port:" , bg='pink', fg='black',font=("Helvetica", 10, "bold"))
    label_start_port.place(relx=0.3, rely=0.35, anchor="e")

    entry_start_port = tk.Entry(canvas, width=10)
    entry_start_port.place(relx=0.4, rely=0.35, anchor="w")

    label_end_port = tk.Label(canvas, text="End Port:", bg='pink', fg='black',font=("Helvetica", 10, "bold"))
    label_end_port.place(relx=0.3, rely=0.45, anchor="e")

    entry_end_port = tk.Entry(canvas, width=10)
    entry_end_port.place(relx=0.4, rely=0.45, anchor="w")

    scan_button = tk.Button(canvas, height=1, width=6,text="Scan", font=("Helvetica", 10, "bold"), command=onScanHost, bg='Green', fg='white')
    scan_button.place(relx=0.5, rely=0.55, anchor="center")

    result_text = tk.Text(canvas, height=5, width=50, bg='pink', fg='black')  # Set background color for the result text
    result_text.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    main()