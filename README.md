# ELI5-WPS-BF

## What does this tool do?
ELI5-WPS-BF is a small, efficient WordPress brute-force tool designed to help you find the correct login credentials for a WordPress site. It performs a brute-force attack by trying multiple username and password combinations to gain access to the WordPress admin panel.

## How does it work?
The tool uses multithreading to perform concurrent login attempts, significantly speeding up the brute-force process. It reads usernames and passwords from specified wordlists and submits them to the WordPress login page. If a correct combination is found, the tool immediately prints the credentials and stops further attempts.

Key features:
- **Multithreading**: Uses up to 1000 concurrent threads to try multiple passwords simultaneously.
- **Session Reuse**: Reuses HTTP connections to improve performance.
- **Error Handling**: Continues running even if some requests fail.
- **Timeout**: Sets a timeout for each request to prevent hanging.
- **Detailed Logging**: Provides feedback on request failures and successful logins.

## How to Install It
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/sigmakader/ELI5-WPS-BF.git
   cd ELI5-WPS-BF
Install Dependencies: Ensure you have Python and pip installed. Then, install the required Python package:
sh
pip install requests
How to Use It
Prepare Wordlists: Create or obtain wordlists for usernames and passwords. For example, username.txt and password.txt.

Run the Script: Use the command line to run the script with the appropriate arguments:

sh
python ELI5-WPS-BF.py -u username.txt -p password.txt
Enter the Target URL: When prompted, enter the URL of the WordPress site you want to target. For example:

Enter the URL of the WordPress site (e.g., https://example.com): https://www.noguchi.org
View the Results: The tool will try passwords concurrently and print the correct credentials in a formatted box as soon as they are found. It will also provide statistics on the number of passwords tried and the average rate of attempts per second.

Example
sh
python ELI5-WPS-BF.py -u username.txt -p rockyou.txt
Enter the URL of the WordPress site (e.g., https://example.com): https://www.noguchi.org
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

