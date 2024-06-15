# Receipt Processor

This project uses Flask to provide the API endpoints:

1. **Process Receipts** (`/receipts/process`) - Takes in a JSON receipt and returns a receipt ID.
2. **Get Points** (`/receipts/<id>/points`) - Returns the points awarded to a receipt based on its ID.

## Getting Started

Follow these instructions to get the application running on your local machine.

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/emmetthe/receipt-processor.git
cd receipt-processor
```

### Build the Docker Container

To build the Docker container, run the following command in the root directory of the project:

```bash
docker build -t receipt-processor .
```

### Run the Docker Container

After building the Docker container, you can run it with the following command:

```bash
docker run -p 8080:8080 receipt-processor
```

## Testing the Application

You can test the application using Postman. Ensure you have Postman installed on your local computer. You can download it [here](https://www.postman.com/downloads/).

### Testing the POST /receipts/process Endpoint

1. Open Postman and create a new request.
2. Set the request method to **POST**.
3. Enter the URL: `http://localhost:8080/receipts/process`.
4. Set the Body:
    - Click on the "Body" tab.
    - Select "raw".
    - Ensure the body type is JSON (application/json).
    - Enter your JSON payload. Example:
      ```json
      {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
          {
            "shortDescription": "Gatorade",
            "price": "2.25"
          },
          {
            "shortDescription": "Gatorade",
            "price": "2.25"
          },
          {
            "shortDescription": "Gatorade",
            "price": "2.25"
          },
          {
            "shortDescription": "Gatorade",
            "price": "2.25"
          }
        ],
        "total": "9.00"
      }
      ```
5. Click the "Send" button.
6. Check the response in the "Body" section. You should receive a JSON response containing the receipt ID:
    ```json
    {
      "id": "random-receipt-id"
    }
    ```

### Testing the GET /receipts/<receipt_id>/points Endpoint

1. Open Postman and create a new request.
2. Set the request method to **GET**.
3. Enter the URL: `http://localhost:8080/receipts/{receipt_id}/points`, replacing `{receipt_id}` with the actual receipt ID received from the previous step.
4. Click the "Send" button.
5. Check the response in the "Body" section. You should receive a JSON response containing the points for the given receipt ID:
    ```json
    {
      "points": 109
    }
    ```
