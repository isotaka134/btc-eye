## BTC EYE : Bitcoin Wallet Information Script
BTC EYE is a Python script designed to retrieve specific details about a Bitcoin wallet. It allows users to input a wallet address once and then select various options to view information like balance, total sent, total received, number of transactions, and the wallet's web link. The script is interactive and features a user-friendly interface .


## Features
Single Wallet Input: Enter the Bitcoin wallet address once for all queries.

Option Menu: Choose from various options to view specific wallet information.

Colored Output: Output is color-coded for clarity and emphasis.

## Prerequisites

Python 3.x: Ensure you have Python 3.x installed on your system.

Required Libraries:

`requests`
`colorama`

Install the necessary libraries using pip:

````

pip install requests colorama

````
## Installation

1. Clone the Repository:

```

  git clone https://github.com/isotaka134/btc-eye.git
  cd btc-eye

```
2. Run the Script:

Execute the script using Python:

```

python btc_eye.py

```

## Usage

1. Enter Wallet Address:

* After running the script, you will be prompted to enter a Bitcoin wallet address. 

Example:
```

Enter the Bitcoin wallet address:
> 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

```

2. Select an Option:
   Choose from the following options:

   `1. Balance`: Display the balance of the wallet in BTC.
 
   `2. Total Sent` :  Show the total BTC sent from the wallet.

   `3. Total Received`:  Display the total BTC received by the wallet.

   `4. Number of Transactions` : Show the number of transactions associated with the wallet.

   `5. Wallet Website Link` : Display the web link to view the wallet on Blockchain.com.

   `6. Exit`: Exit the script.

**Example:**

```

Choose an option:
1. Balance
2. Total Sent
3. Total Received
4. Number of Transactions
5. Wallet Website Link
6. Exit
> 1

```

3. View Results:

   The selected information will be displayed in green text, preceded by a `[*]` symbol, and separated by clean lines.

4. Exit the Script:
   
   Select option `6` to exit the program.

## Example Output

```

************************ BTC EYE ************************

Enter the Bitcoin wallet address:
> 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

Choose an option:
1. Balance
2. Total Sent
3. Total Received
4. Number of Transactions
5. Wallet Website Link
6. Exit
> 1

----------------------------------------
[*] Balance: 50.0 BTC
----------------------------------------

```

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the Repository:
   Click on the "Fork" button at the top right of this page to create a copy of this repository under your GitHub account.

2. Clone Your Fork:

```

git clone https://github.com/isotaka134/btc-eye.git

```

3. Create a Branch:

```

git checkout -b your-branch-name

```

4. Make Your Changes:

   Modify the code as needed.

5. Commit Your Changes:

   ```

   git commit -m "Your commit message"

   ```

6. Push to Your Fork:

   ```

   git push origin your-branch-name

   ```

7. Submit a Pull Request:

   Go to the original repository and click "New Pull Request" to submit your changes for review.


