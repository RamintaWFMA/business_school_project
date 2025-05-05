# Raminta Kersulyte Order RFM Analysis Project

## Description
This project is part of the **business school project** and aims to provide solutions for actionable insights for optimizing eCommerce marketing and customer segmentation. By applying the RFM (Recency, Frequency, Monetary) model to real customer order data (from platforms like Omnisend), the goal is to help identify high-value customers, churn risks, and potential growth segments. The solution is designed to be scalable, reusable, and easy to interpret for marketing strategists and analysts. 

## Features
- RFM Segmentation: Automatically clusters customers into segments using KMeans and standardized RFM scoring.
- Custom Segment Labels: Assigns business-friendly labels like "VIP Customers", "At-Risk", or "Cold One-Timers".
- Data Visualization: Generates pair plots to help interpret customer behavior patterns.
- Exportable Output: Segmentation results are saved as a CSV file for use in other tools or campaigns.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/raminta-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd raminta-project
    ```
3. Install dependencies:
    ```bash
    npm install
    pip install -r requirements.txt
    ```

## Usage
1. Start the application:
    ```bash
    npm start
    ```
2. Open your browser and navigate to `http://localhost:3000`.
3. Export your order data as a .csv file (e.g. from Omnisend or Shopify).

4. Place the file in the project directory and name it orders_export_pp.csv.

5. Run the script:
 ```
bash
python rfm_analysis.py
 ```

6. View the output:

- A segment summary will be printed in the terminal.
- A visual chart will appear.
-A file named rfm_segmented_customers.csv will be generated.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or feedback, please contact Raminta Kersulyte at raminta@wfma.agency.