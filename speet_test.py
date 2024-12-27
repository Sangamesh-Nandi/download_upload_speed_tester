import speedtest

st = speedtest.Speedtest()

print("Testing download speed...")
down_speed = st.download()

print("Testing upload speed...")
up_speed = st.upload()

ping = st.results.ping

down_speed_mbps = round(down_speed / 1_000_000, 2)
up_speed_mbps = round(up_speed / 1_000_000, 2)

print("\nInternet speed test results:")
print(f"Download speed: {down_speed_mbps} Mbps")
print(f"Upload speed: {up_speed_mbps} Mbps")
print(f"Ping: {ping} ms")
