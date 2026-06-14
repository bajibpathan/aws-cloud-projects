# 🛠 Deployment Guide  
This guide explains how to deploy the **Serverless CRUD API** using AWS services.  
It is written for beginners learning cloud fundamentals and follows a clear, step‑by‑step flow.

---

## ✅ 1. Prerequisites

Before deploying, ensure you have:

- An AWS account   
- Basic understanding of 
    - [AWS IAM](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/identity-and-access-control.html) 
    - [Lambda](https://docs.aws.amazon.com/lambda/)
    - [API Gateway](https://docs.aws.amazon.com/apigateway/)
    - [DynamoDB](https://docs.aws.amazon.com/dynamodb/)  

---

## 🧩 2. Create IAM Policy (Least Privilege)

Create a policy named **`lambda-custom-policy`** with permissions for DynamoDB + CloudWatch Logs.
1. Open IAM service
![IAM Dashboard](./images/IAM_Policy/IAM_dashboard.png)
2. Open policies page in the IAM console
![IAM Policies](./images/IAM_Policy/IAM_Policies.png)
3. Click **"Create policy"** on top right corner
![IAM Policies](./images/IAM_Policy/IAM_CreatePolicy.png)
4. In the policy editor, click JSON, and paste the following and click **"Next"**
![IAM Policies](./images/IAM_Policy/IAM_JsonFormat.png)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "dynamodb:DeleteItem",
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:UpdateItem"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```
![IAM Policies](./images/IAM_Policy/IAM_PolicyNext.png)
5. Give name **"lambda-custom-policy"**, and click "Create policy" on botom right

![Policy Create](./images/IAM_Policy/IAM_PolicyReviewCreate.png)

---

## 🛡 3. Create IAM Role for Lambda

Create the IAM execution role that provides your Lambda function with the necessary permissions to interact with AWS resources.

To create an execution role

1. Open the roles page in the IAM console.
![IAM Role](./images/IAM_Role/IAM_Role.png)

2. Choose Create role.
![IAM Role](./images/IAM_Role/IAM_CreateRole.png)

3. Create a role with the following properties.
Select Trusted entity type as **AWS service**, then select **Lambda** from Use case and click **next**
![IAM Trusted Entity](./images/IAM_Role/IAM_TrustedEntity.png)

4. In the Permissions policies page, in the search bar, type **lambda-custom-policy**. The newly created policy should show up. Select it, and click **next**.
![IAM Role Permissions](./images/IAM_Role/IAM_RolePermissions.png)

5. Finally, update the role name under role details as **lambda-apigateway-role** and, Click on **Create role**
![IAM Create Role](./images/IAM_Role/IAM_RoleReviewCreate.png)

---
## 🧬 4. Deploy Lambda Function
1. Open **Lambda** service and Click **Create a function**:
![Create a Function](./images/Lambda/Lambda_CreateFunction.png)
Note: If you already created lambda functions, all the created lambda functions will be listed.

2. Select **"Author from scratch"**, and Enter function name as  **LambdaFunctionOverHttps**, and select **Python 3.13** as Runtime.
![Basic Info](./images/Lambda/Lambda_BasicInfo.png)

3. Under **Additional settings**, toggle **"Custom exceution role**  
![Basic Info](./images/Lambda/Lambda_executionrole.png)

4. Under Configure custom execution role section, select **lambda-apigateway-role** that we created, from the drop down and Click **save**
![Basic Info](./images/Lambda/Lambda_saverole.png)

5. Leave the remain options as it is, and click **"Create function"**
![Basic Info](./images/Lambda/Lambda_ReviewCreateFunction.png)

6. Remove the default code from code source.
![Default Source Code](./images/Lambda/Lambda_SourceCode.png)

7.Copy the Lambda function python code from [here](./../../src/lambda/handler.py) and paste it in the code source, and click **Deploy**
![Actual Source Code](./images/Lambda/Lambda_UpdatedCode.png)

---

## 🧪 5. Test the Lambda Function

Let's test our newly created function. We haven't created DynamoDB and the API yet, so we'll do a sample echo operation. The function should output whatever input we pass.

1. Click the **"Test"** tab right beside "Code" tab
![Test Button](./images/Lambda/Lambda_Test.png)

2. Give **"Event name"** as **echotest**
![Event Name](./images/Lambda/Lambda_EventName.png)

3. Paste the following JSON into the event. 
**Note:** The field "operation" dictates what the lambda function will perform. In this case, it'd simply return the payload from input event as output. Click "Save" to save
```json
{
    "operation": "echo",
    "payload": {
        "somekey1": "somevalue1",
        "somekey2": "somevalue2"
    }
}
```
![Event Json](./images/Lambda/Lambda_EventJson.png)

4. Click **"Test"**, and it will execute the test event. You should see the output in the console
![Test Lambada](./images/Lambda/Lambda_UpdateTest.png)

5. Once the **Test** is successful, it will show the details and Summary.
![Test Summary](./images/Lambda/Lambda_Summary.png)

We're all set to create DynamoDB table and an API using our lambda as backend!

---
## 🗄 4. Create DynamoDB Table

Create the DynamoDB table that the Lambda function uses.

To create a DynamoDB table

1. Open DynamoDB → Create Table:
![Create Table](./images/Dynamodb/Db_createtable.png)


2. Create a table with the following settings.
    - Table name – **lambda-apigateway**
    - Partition key – id (string)

![Table Info](./images/Dynamodb/Db_TableInfo.png)

3. Leave others as defaults and choose "Create table".
![Create Table](./images/Dynamodb/Db_Update_CreateTable.png)

---

## 🌐 6. Create REST API 

To create the REST API
1. Go to API Gateway console and Click **Create an API**
![Create API](./images/APIGateway/API_CreateAPI.png)

2. Scroll down and select "Build" for REST API
![Build API](./images/APIGateway/API_BuildAPI.png)

3. Give the API name as **"DynamoDBOperations"**, keep everything as is, click "Create API"
![Create API](./images/APIGateway/API_UpdateCreate.png)

```text
Note: Each API is collection of resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. Typically, API resources are organized in a resource tree according to the application logic. At this time you only have the root resource, but let's add a resource next. 
```

4. Click "Create Resource"
![Create API](./images/APIGateway/API_CreateResource.png)

5. Input **"DynamoDBManager"** in the Resource Name. Click **"Create Resource"**
![Create Resource](./images/APIGateway/API_UpdateCreateResource.png)

6. Next, create a POST Method for our API. With the **"/DynamoDBManager"** resource selected, click "Create Method".
![Create Method](./images/APIGateway/API_CreateMethod.png)

7. Select **"POST"** from **"Method type"** drop down.
![Choose Method](./images/APIGateway/API_ChooseMethod.png)

8. Leave the rest of settings to it's defaults and Click **"Create Method"**
![Create Method](./images/APIGateway/API_UpdateCreateMethod.png)
---
## 🚀 7. Deploy the API

In this step, you deploy the API that you created to a stage called prod.

1. Click "Deploy API" on top right
![Deploy API](./images/APIGateway/API_Deploy.png)

2.  Select "[New Stage]" for "Stage". Give **"Prod"** as "Stage name", and Click **"Deploy"**
![Deploy API](./images/APIGateway/API_StageDeploy.png)

So, Our API is successfuly deployed to Prod Stage and we're all set to run our solution! 

---

## 🧪 8. Test the API

1. To invoke our API endpoint, we need the endpoint url. In the "Stages" screen, expand the stage "Prod", keep expanding till you see "POST", select "POST" method, and copy the "Invoke URL" from screen
![Endpoint API](./images/APIGateway/API_InvokeEndpoint.png)

2. To test our API from local machine, we are going to use **Postman** and Curl command. You can choose either method based on your convenience and familiarity.

**Testing using Postman**
3. Open Postman
![Postman](./images/Postman/Postman_Open.png)

4. Exapnd Collections and Click on **"Create"** 
![Collections](./images/Postman/Postman_CreateCollection.png)

5. Give a name to the collection. Example **AWS**
![Collection Name](./images/Postman/Postman_CollectionNameUpdate.png)

6. Add request to the newly created collection
![Add Request](./images/Postman/Postman_AddRequest.png)

7. Update the below details and click **Send**
    - **Request Name**: DynamoDB
    - **Endpoint**: Endpoint Information from the Step # 1
    - **Request Body**: Copy the below Json payload and click **raw** and paste it.

        ```json
        {
            "operation": "create",
            "tableName": "lambda-apigateway",
            "payload": {
                "Item": {
                    "id": "1234ABCD",
                    "number": 5
                }
            }
        }

        ```
![Update Request](./images/Postman/Postman_Update.png)

8. Verify the Postman Response. If everything set it up correctly, you should get "200 OK" response code and the message. 
![Verify Results](./images/Postman/Postman_Response.png)

**Testing using cURL**
1. Open the Terminal (Mac / Linux) or Command Prompt / Power shell (Windows) and execute the below command. Please update the endpoint before running the command
```bash
$ curl -X POST -d "{\"operation\":\"create\",\"tableName\":\"lambda-apigateway\",\"payload\":{\"Item\":{\"id\":\"1\",\"name\":\"Bob\"}}}" $REPLACE_ENDPOINT
```
![Verify Results](./images/Postman/CURL_output.png)

---

## ## ✅ 9.Validate the Results from AWS Console
1. To validate that the item is indeed inserted into DynamoDB table, go to Dynamo console, select "lambda-apigateway" table, select "Explore table items" button from top right, and the newly inserted item should be displayed.
![Verify Results](./images/Dynamodb/DB_ExploreItems.png)
![Verify Results](./images/Dynamodb/DB_Data.png)

2. To get all the inserted items from the table, we can use the "list" operation of Lambda using the same API. Pass the following JSON to the API, and it will return all the items from the Dynamo table

```json
{
    "operation": "list",
    "tableName": "lambda-apigateway",
    "payload": {
    }
}
```
![Verify Results](./images/Postman/PostMan_AllItems.png)

We have successfully created a serverless API using API Gateway, Lambda, and DynamoDB! Your serverless CRUD API is now live and ready to use!🎉

