# Port Scanner Tool

![Port Scanner Screenshot](screenshot.png)

A Python-based port scanner with a colorful CLI interface that supports scanning IP addresses, URLs, port numbers, and port names.

## Features

- 🔍 Scan IP port ranges (1-65535 or custom range)
- 🌐 Scan URL ports with progress bar
- 📌 Scan single port on IP or URL
- 🔢 Get service name from port number
- 📝 Get port number from service name
- ⏱️ Shows estimated scan time before scanning
- 📊 Progress bar with elapsed time during scan
- 🎨 Color-coded output (green for open, red for closed)
- 🔄 Returns to main menu after each operation

## ⚠️ تحذير قانوني / Legal Disclaimer

**المستخدم هو المسؤول الوحيد عن استخدام هذه الأداة.**

- **لا تستخدم** هذه الأداة على عناوين IP أو مواقع إلكترونية لا تملكها أو لا تملك صلاحية صريحة لفحصها.
- هذه الأداة مخصصة **للاستخدام الشخصي فقط** وفحص الأجهزة والمواقع التي تملكها شخصيًا.
- يجب استخدامها **لأغراض تأمين وأمن الممتلكات الشخصية** فقط.
- أي استخدام غير قانوني أو غير مصرح به هو **مسؤولية المستخدم بالكامل**.
- المطور غير مسؤول عن أي سوء استخدام أو أضرار ناتجة عن استخدام هذه الأداة.

---

**The user is solely responsible for using this tool.**

- **DO NOT use** this tool on IP addresses or websites you do not own or have explicit permission to scan.
- This tool is for **personal use only** and scanning devices/sites you personally own.
- Use it **for securing and protecting personal property** only.
- Any illegal or unauthorized use is **the user's full responsibility**.
- The developer is not responsible for any misuse or damages resulting from using this tool.

## Requirements

- Python 3.x
- colorama library

## Installation

### All Operating Systems (Windows, Linux, macOS)

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/i7ego/scan_Tool.git
   cd scan_Tool
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install:
   ```bash
   pip install colorama
   ```

## Usage

### Run the scanner:

```bash
python scan.py
```

Or on some systems:

```bash
python3 scan.py
```

## Menu Options

```
1] Scan Port IP (Range)      - Scan a range of ports on an IP address
2] Scan Port Number          - Get service name from port number
3] Scan Port Name            - Get port number from service name
4] Scan Port URL             - Scan ports on a URL/domain
5] Scan Single Port on IP/URL - Check if single port is open/closed
6] Exit                      - Quit the program
```

## Examples

### Scan IP port range:
```
Enter the target IP address: 192.168.1.1
Do you want to search all ports (1) or a port range (2)? 2
Enter the start port: 1
Enter the end port: 1000
```

### Scan single port on IP:
```
Enter IP or URL: 192.168.1.1
Enter port number to check: 80
```

### Scan single port on URL:
```
Enter IP or URL: google.com
Enter port number to check: 443
```

### Get port service name:
```
Enter port number : 80
Port name of 80 = http
```

### Get port number from service:
```
Enter port Name : http
Port Number of http = 80
```

## OS-Specific Notes

### Windows
- Run Command Prompt or PowerShell as Administrator for best results
- Some antivirus software may flag port scanning tools
- Use: `python scan.py`

### Linux
- May require root privileges for certain ports:
  ```bash
  sudo python3 scan.py
  ```
- Install Python if not present:
  ```bash
  sudo apt-get install python3 python3-pip
  ```

### macOS
- Install Python via Homebrew if needed:
  ```bash
  brew install python3
  ```
- Run with: `python3 scan.py`

## Troubleshooting

**Import Error:**
- Make sure colorama is installed: `pip install colorama`

**Permission Denied:**
- Run with administrator/root privileges

**Connection Timeouts:**
- The scanner uses fast timeouts (0.001s) for range scanning
- Single port check uses 1 second timeout for accuracy
- Results may vary based on network conditions

## Author

**Ahmed Hagag** - scan_Tool 2026

## License

This tool is for educational and authorized testing purposes only.
