import pyshark

capture = pyshark.LiveCapture(interface='Intel(R) Ethernet Connection (10) I219-V', display_filter='ip.src == 169.254.39.239')
capture.sniff()


