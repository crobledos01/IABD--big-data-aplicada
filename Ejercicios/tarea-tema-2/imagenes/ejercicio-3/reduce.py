import sys

codes = {}
ips = {}

for line in sys.stdin:
    key, val = line.strip().split("\t")
    val = int(val)
    
    if key.startswith("code_"):
        code = key[5:]
        codes[code] = codes.get(code,0) + val
    
    elif key.startswith("ip_"):
        ip = key[3:]
        ips[ip] = ips.get(ip, 0) + val

print("---- Peticiones por código ----")
for k, v in codes.items():
    print(k,v)

print("\n---- Top 5 IPs ----")
for ip, total in sorted(ips.items(), key = lambda x: x[1], reverse=True)[:5]:
    print(ip, total)
