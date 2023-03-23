import sicktoolbox as sbt
lms = SickLMS()

#lidar = sbt.SickLMS('192.168.1.1') # Reemplaza la dirección IP con la dirección IP de tu sensor LiDAR SICK
if lms.Connect(port="/dev/ttyUSB0", baudrate=38400):
    print("Connected to LiDAR")
else:
    print("Connection failed")

#lidar.Connect()
while True:
    scan_data = lms.GetSickScanData()
    print(scan_data)

lms.Disconnect()